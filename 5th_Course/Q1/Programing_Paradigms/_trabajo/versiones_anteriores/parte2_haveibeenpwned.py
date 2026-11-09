"""Parte 2: comprobador de contraseñas y dominios con Have I Been Pwned.

Dos modos que elige el usuario:
  1. Contraseñas: API pwnedpasswords, búsqueda por rango (SHA1 o NTLM).
  2. Dominios: API v3 de brechas, filtrada por dominio.

Uso:
    python parte2_haveibeenpwned.py             modo interactivo (usa la red)
    python parte2_haveibeenpwned.py --ejemplos  ejemplos sin red, con respuestas simuladas

Decisiones de estilo funcional:
  - Los tres puntos de decisión (modo, formato de hash, tratamiento de cada
    código HTTP) son callbacks que se eligen en una tabla con `despachar`.
  - Las funciones no leen ni escriben nada por su cuenta: la entrada, la
    salida y las peticiones HTTP llegan en un `Entorno`, y los modos devuelven
    el mensaje en lugar de imprimirlo. Por eso se pueden probar sin red.
"""
import getpass
import hashlib
import sys
from collections import namedtuple
from functools import partial, reduce, wraps
from types import SimpleNamespace
from urllib.parse import urlparse

import requests
from Crypto.Hash import MD4

URL_RANGO = "https://api.pwnedpasswords.com/range/{prefijo}"
URL_BRECHAS = "https://haveibeenpwned.com/api/v3/breaches"

# La API de brechas devuelve 403 si falta el User-Agent.
CABECERAS_BASE = {"User-Agent": "practica-programacion-funcional"}
# Add-Padding hace que todas las respuestas tengan un tamaño parecido; las
# entradas de relleno traen contador 0 y no afectan al recuento.
CABECERAS_RANGO = {**CABECERAS_BASE, "Add-Padding": "true"}

Formato = namedtuple("Formato", "nombre hashear parametros")
Resultado = namedtuple("Resultado", "ok dato")
Entorno = namedtuple("Entorno", "pedir pedir_secreto mostrar http_get")


# --- Callbacks de selección ---------------------------------------------------

def despachar(tabla, clave, por_defecto):
    """Devuelve el callback asociado a `clave`, o `por_defecto` si no existe."""
    return tabla.get(clave, por_defecto)


# --- Formatos de hash ---------------------------------------------------------

def hash_sha1(contrasena):
    return hashlib.sha1(contrasena.encode("utf-8")).hexdigest().upper()


def hash_ntlm(contrasena):
    # NTLM es el MD4 de la contraseña codificada en UTF-16 little endian.
    # hashlib ya no incluye MD4 en muchas instalaciones, de ahí pycryptodome.
    return MD4.new(contrasena.encode("utf-16-le")).hexdigest().upper()


FORMATOS = {
    "1": Formato("SHA1", hash_sha1, {}),
    "2": Formato("NTLM", hash_ntlm, {"mode": "ntlm"}),
}


# --- Callbacks para cada código HTTP -----------------------------------------

MSG_403 = "El servidor ha rechazado la petición (HTTP 403)."
MSG_503 = "El servicio no está disponible ahora mismo. Inténtalo más tarde."
MSG_400_DOMINIO = "El dominio no tiene un formato válido."
MSG_LIMITE = "Se ha superado el límite de peticiones."
MSG_FORMATO = "El servidor ha devuelto una respuesta con un formato que no se reconoce."


def error(mensaje):
    """Fabrica un callback que ignora la respuesta y devuelve ese error."""
    return lambda _respuesta: Resultado(False, mensaje)


def error_limite(respuesta):
    espera = respuesta.headers.get("Retry-After")
    return Resultado(False, MSG_LIMITE + (f" Vuelve a intentarlo en {espera} s." if espera else ""))


def error_inesperado(respuesta):
    return Resultado(False, f"Respuesta inesperada del servidor (HTTP {respuesta.status_code}).")


def contar_filtraciones(sufijo, respuesta):
    """Suma las veces que aparece `sufijo` en un cuerpo con líneas SUFIJO:CUENTA."""
    lineas = filter(str.strip, respuesta.text.splitlines())
    pares = map(lambda linea: linea.strip().split(":"), lineas)
    del_sufijo = filter(lambda par: par[0].upper() == sufijo, pares)
    return Resultado(True, reduce(lambda total, par: total + int(par[1]), del_sufijo, 0))


def resumir_brecha(brecha):
    return {
        "titulo": brecha.get("Title") or brecha.get("Name", "?"),
        "fecha": brecha.get("BreachDate", ""),
        "cuentas": brecha.get("PwnCount", 0),
        "datos": tuple(brecha.get("DataClasses", ())),
    }


def listar_brechas(respuesta):
    """Brechas de la respuesta JSON, resumidas y ordenadas por fecha."""
    brechas = respuesta.json()
    if not isinstance(brechas, list):
        return Resultado(False, MSG_FORMATO)
    return Resultado(True, sorted(map(resumir_brecha, brechas), key=lambda b: b["fecha"]))


def manejadores_rango(sufijo):
    return {
        200: partial(contar_filtraciones, sufijo),
        403: error(MSG_403),
        429: error_limite,
        503: error(MSG_503),
    }


MANEJADORES_DOMINIO = {
    200: listar_brechas,
    400: error(MSG_400_DOMINIO),
    403: error(MSG_403),
    404: lambda _respuesta: Resultado(True, []),  # sin brechas para ese dominio
    429: error_limite,
    503: error(MSG_503),
}


def gestionar_respuesta(respuesta, manejadores):
    """Aplica a la respuesta el callback que corresponde a su código HTTP."""
    return despachar(manejadores, respuesta.status_code, error_inesperado)(respuesta)


# --- Errores de red -----------------------------------------------------------

# El orden importa: ConnectTimeout es a la vez Timeout y ConnectionError, y se
# toma la primera clase de la tabla que encaje.
ERRORES_RED = {
    requests.Timeout: "La petición ha tardado demasiado. Revisa la conexión e inténtalo de nuevo.",
    requests.ConnectionError: "No se ha podido conectar con el servidor. Revisa la conexión.",
    requests.exceptions.JSONDecodeError: "El servidor ha devuelto una respuesta que no se puede leer.",
    requests.RequestException: "La petición ha fallado.",
}


def protegida(llamada):
    """Decorador: convierte las excepciones de requests en un Resultado de error."""
    @wraps(llamada)
    def envuelta(*args, **kwargs):
        try:
            return llamada(*args, **kwargs)
        except requests.RequestException as excepcion:
            tipo = next(filter(lambda t: isinstance(excepcion, t), ERRORES_RED))
            return Resultado(False, ERRORES_RED[tipo])
    return envuelta


# --- Consultas ----------------------------------------------------------------

@protegida
def comprobar_contrasena(http_get, formato, contrasena):
    """Consulta el rango de la contraseña. Solo salen 5 caracteres del hash."""
    huella = formato.hashear(contrasena)
    prefijo, sufijo = huella[:5], huella[5:]
    respuesta = http_get(
        URL_RANGO.format(prefijo=prefijo), params=formato.parametros, headers=CABECERAS_RANGO
    )
    return gestionar_respuesta(respuesta, manejadores_rango(sufijo))


@protegida
def comprobar_dominio(http_get, dominio):
    respuesta = http_get(URL_BRECHAS, params={"Domain": dominio}, headers=CABECERAS_BASE)
    return gestionar_respuesta(respuesta, MANEJADORES_DOMINIO)


# --- Presentación -------------------------------------------------------------

def miles(n):
    return f"{n:,}".replace(",", ".")


def presentar_contrasena(formato, resultado):
    if not resultado.ok:
        return resultado.dato
    if resultado.dato == 0:
        return f"Tu contraseña ({formato.nombre}) no aparece en ninguna filtración conocida por Have I Been Pwned."
    veces = "vez" if resultado.dato == 1 else "veces"
    return f"Tu contraseña ({formato.nombre}) aparece {miles(resultado.dato)} {veces} en filtraciones conocidas. Cámbiala."


def formatear_brecha(brecha):
    datos = ", ".join(brecha["datos"]) or "sin detalle"
    return f"- {brecha['titulo']} ({brecha['fecha']}): {miles(brecha['cuentas'])} cuentas. Datos expuestos: {datos}."


def presentar_dominio(dominio, resultado):
    if not resultado.ok:
        return resultado.dato
    brechas = resultado.dato
    if not brechas:
        return f"No hay filtraciones registradas para {dominio}."
    asociadas = "filtración asociada" if len(brechas) == 1 else "filtraciones asociadas"
    return "\n".join([f"{len(brechas)} {asociadas} a {dominio}:", *map(formatear_brecha, brechas)])


def limpiar_dominio(texto):
    """Deja solo el dominio: sin esquema, ruta, www ni mayúsculas."""
    t = texto.strip().lower()
    return urlparse(t if "//" in t else "//" + t).netloc.removeprefix("www.")


# --- Modos --------------------------------------------------------------------

def modo_contrasenas(entorno):
    opcion = entorno.pedir("Formato de hash: [1] SHA1 (estándar)  [2] NTLM (Windows): ").strip()
    formato = despachar(FORMATOS, opcion, None)
    if formato is None:
        return "Opción de formato no válida."
    contrasena = entorno.pedir_secreto("Contraseña (no se muestra al escribir): ")
    resultado = comprobar_contrasena(entorno.http_get, formato, contrasena)
    return presentar_contrasena(formato, resultado)


def modo_dominios(entorno):
    dominio = limpiar_dominio(entorno.pedir("Dominio a comprobar (por ejemplo ejemplo.com): "))
    if not dominio:
        return "No has indicado ningún dominio."
    return presentar_dominio(dominio, comprobar_dominio(entorno.http_get, dominio))


def modo_invalido(_entorno):
    return "Modo no válido. Elige 1 o 2."


MODOS = {"1": modo_contrasenas, "2": modo_dominios}


def ejecutar(entorno):
    opcion = entorno.pedir("Modo: [1] comprobar contraseña  [2] comprobar dominio: ").strip()
    mensaje = despachar(MODOS, opcion, modo_invalido)(entorno)
    entorno.mostrar(mensaje)
    return mensaje


def entorno_real():
    return Entorno(
        pedir=input,
        pedir_secreto=getpass.getpass,
        mostrar=print,
        http_get=partial(requests.get, timeout=10),
    )


# --- Ejemplos sin red ---------------------------------------------------------
# Respuestas simuladas con la forma que describe la documentación de la API.
# Las marcas "ejemplo" son inventadas; no representan filtraciones reales.

def respuesta(codigo, texto="", datos=None, cabeceras=None):
    def como_json():
        if datos is None:
            raise requests.exceptions.JSONDecodeError("sin JSON", "", 0)
        return datos
    return SimpleNamespace(status_code=codigo, text=texto, headers=cabeceras or {}, json=como_json)


def http_que_devuelve(resp, url=None, params=None):
    """Falso http_get: comprueba la petición recibida y devuelve `resp`."""
    def http_get(url_real, params=None, headers=None, **_resto):
        assert url is None or url_real == url, url_real
        assert esperados is None or params == esperados, params
        assert "User-Agent" in headers
        return resp
    esperados = params
    return http_get


def http_que_falla(excepcion):
    def http_get(_url, **_resto):
        raise excepcion
    return http_get


def entorno_de_prueba(entradas, secreto="", http_get=None):
    """Entorno cuyas respuestas del usuario salen de la lista `entradas`."""
    pendientes = iter(entradas)
    return Entorno(
        pedir=lambda _texto: next(pendientes),
        pedir_secreto=lambda _texto: secreto,
        mostrar=lambda _mensaje: None,
        http_get=http_get,
    )


SHA1 = FORMATOS["1"]
NTLM = FORMATOS["2"]

BRECHA_1 = {"Name": "EjemploUno", "Title": "Ejemplo Uno", "Domain": "ejemplo.com",
            "BreachDate": "2014-03-02", "PwnCount": 1234567,
            "DataClasses": ["Correos electrónicos", "Contraseñas"]}
BRECHA_2 = {"Name": "EjemploDos", "Title": "Ejemplo Dos", "Domain": "ejemplo.com",
            "BreachDate": "2011-09-20", "PwnCount": 980,
            "DataClasses": ["Correos electrónicos"]}
RESUMEN_1 = {"titulo": "Ejemplo Uno", "fecha": "2014-03-02", "cuentas": 1234567,
             "datos": ("Correos electrónicos", "Contraseñas")}
RESUMEN_2 = {"titulo": "Ejemplo Dos", "fecha": "2011-09-20", "cuentas": 980,
             "datos": ("Correos electrónicos",)}

# Hashes de "password": SHA1 = 5BAA6|1E4C9B93F3F0682250B6CF8331B7EE68FD8
#                       NTLM = 8846F|7EAEE8FB117AD06BDD830B7586C
SUFIJO_SHA1 = "1E4C9B93F3F0682250B6CF8331B7EE68FD8"
SUFIJO_NTLM = "7EAEE8FB117AD06BDD830B7586C"
CUERPO_SHA1 = f"0018A45C4D1DEF81644B54AB7F969B88D65:1\r\n{SUFIJO_SHA1}:3\r\nFFFF0000FFFF0000FFFF0000FFFF0000FFF:7"
CUERPO_NTLM = f"00000000000000000000000000A:0\r\n{SUFIJO_NTLM}:52256\r\n"

EJEMPLOS_HASH_SHA1 = [
    (("",), "DA39A3EE5E6B4B0D3255BFEF95601890AFD80709"),
    (("abc",), "A9993E364706816ABA3E25717850C26C9CD0D89D"),
    (("password",), "5BAA61E4C9B93F3F0682250B6CF8331B7EE68FD8"),
    (("123456",), "7C4A8D09CA3762AF61E59520943DC26494F8941B"),
    (("hello",), "AAF4C61DDCC5E8A2DABEDE0F3B482CD9AEA9434D"),
]

EJEMPLOS_HASH_NTLM = [
    (("",), "31D6CFE0D16AE931B73C59D7E0C089C0"),
    (("password",), "8846F7EAEE8FB117AD06BDD830B7586C"),
    (("123456",), "32ED87BDB5FDC5E9CBA88547376818D4"),
    (("admin",), "209C6174DA490CAEB422F3FA5A7AE634"),
    (("Password1",), "64F12CDDAA88057E06A81B54E73B949B"),
]

EJEMPLOS_DESPACHAR = [
    (({"1": "uno"}, "1", None), "uno"),
    (({"1": "uno"}, "2", None), None),
    (({}, "x", "por defecto"), "por defecto"),
    (({"a": len}, "a", None), len),
    (({1: "x"}, 1, 0), "x"),
]

EJEMPLOS_LIMPIAR_DOMINIO = [
    (("ejemplo.com",), "ejemplo.com"),
    (("https://www.Ejemplo.com/ruta?x=1",), "ejemplo.com"),
    (("  EJEMPLO.COM  ",), "ejemplo.com"),
    (("http://sub.ejemplo.com",), "sub.ejemplo.com"),
    (("www.ejemplo.com",), "ejemplo.com"),
    (("",), ""),
]

EJEMPLOS_CONTAR_FILTRACIONES = [
    (("ABC", respuesta(200, "ABC:12\r\nDEF:3\r\n")), Resultado(True, 12)),
    (("ZZZ", respuesta(200, "ABC:12\r\nDEF:3")), Resultado(True, 0)),
    (("ABC", respuesta(200, "ABC:0\r\nDEF:5")), Resultado(True, 0)),  # relleno
    (("DEF", respuesta(200, "ABC:1\nDEF:3\nGHI:9\n")), Resultado(True, 3)),
    (("ABC", respuesta(200, "")), Resultado(True, 0)),
    (("ABC", respuesta(200, "abc:7")), Resultado(True, 7)),
]

EJEMPLOS_LISTAR_BRECHAS = [
    ((respuesta(200, datos=[]),), Resultado(True, [])),
    ((respuesta(200, datos=[BRECHA_1]),), Resultado(True, [RESUMEN_1])),
    ((respuesta(200, datos=[BRECHA_1, BRECHA_2]),), Resultado(True, [RESUMEN_2, RESUMEN_1])),
    ((respuesta(200, datos={"mensaje": "no es una lista"}),), Resultado(False, MSG_FORMATO)),
    ((respuesta(200, datos=[{"Name": "Sin datos", "BreachDate": "2020-01-01"}]),),
     Resultado(True, [{"titulo": "Sin datos", "fecha": "2020-01-01", "cuentas": 0, "datos": ()}])),
]

MANEJADORES_PRUEBA = {200: lambda r: Resultado(True, "bien"), 404: lambda r: Resultado(True, "nada")}
EJEMPLOS_GESTIONAR_RESPUESTA = [
    ((respuesta(200), MANEJADORES_PRUEBA), Resultado(True, "bien")),
    ((respuesta(404), MANEJADORES_PRUEBA), Resultado(True, "nada")),
    ((respuesta(418), MANEJADORES_PRUEBA), Resultado(False, "Respuesta inesperada del servidor (HTTP 418).")),
    ((respuesta(429, cabeceras={"Retry-After": "2"}), MANEJADORES_DOMINIO),
     Resultado(False, MSG_LIMITE + " Vuelve a intentarlo en 2 s.")),
    ((respuesta(429), MANEJADORES_DOMINIO), Resultado(False, MSG_LIMITE)),
    ((respuesta(503), MANEJADORES_DOMINIO), Resultado(False, MSG_503)),
]

EJEMPLOS_COMPROBAR_CONTRASENA = [
    ((http_que_devuelve(respuesta(200, CUERPO_SHA1), URL_RANGO.format(prefijo="5BAA6"), {}), SHA1, "password"),
     Resultado(True, 3)),
    ((http_que_devuelve(respuesta(200, CUERPO_NTLM), URL_RANGO.format(prefijo="8846F"), {"mode": "ntlm"}), NTLM, "password"),
     Resultado(True, 52256)),
    ((http_que_devuelve(respuesta(200, CUERPO_SHA1)), SHA1, "otra contraseña distinta"), Resultado(True, 0)),
    ((http_que_devuelve(respuesta(429, cabeceras={"Retry-After": "5"})), SHA1, "password"),
     Resultado(False, MSG_LIMITE + " Vuelve a intentarlo en 5 s.")),
    ((http_que_falla(requests.Timeout()), SHA1, "password"), Resultado(False, ERRORES_RED[requests.Timeout])),
    ((http_que_falla(requests.ConnectionError()), NTLM, "password"),
     Resultado(False, ERRORES_RED[requests.ConnectionError])),
]

EJEMPLOS_COMPROBAR_DOMINIO = [
    ((http_que_devuelve(respuesta(200, datos=[BRECHA_1]), URL_BRECHAS, {"Domain": "ejemplo.com"}), "ejemplo.com"),
     Resultado(True, [RESUMEN_1])),
    ((http_que_devuelve(respuesta(200, datos=[])), "limpio.org"), Resultado(True, [])),
    ((http_que_devuelve(respuesta(404)), "limpio.org"), Resultado(True, [])),
    ((http_que_devuelve(respuesta(400)), "no es un dominio"), Resultado(False, MSG_400_DOMINIO)),
    ((http_que_devuelve(respuesta(200)), "ejemplo.com"),
     Resultado(False, ERRORES_RED[requests.exceptions.JSONDecodeError])),
    ((http_que_falla(requests.ConnectionError()), "ejemplo.com"),
     Resultado(False, ERRORES_RED[requests.ConnectionError])),
]

EJEMPLOS_PRESENTAR_CONTRASENA = [
    ((SHA1, Resultado(True, 0)),
     "Tu contraseña (SHA1) no aparece en ninguna filtración conocida por Have I Been Pwned."),
    ((SHA1, Resultado(True, 1)), "Tu contraseña (SHA1) aparece 1 vez en filtraciones conocidas. Cámbiala."),
    ((NTLM, Resultado(True, 1234567)),
     "Tu contraseña (NTLM) aparece 1.234.567 veces en filtraciones conocidas. Cámbiala."),
    ((SHA1, Resultado(False, MSG_503)), MSG_503),
    ((NTLM, Resultado(False, MSG_403)), MSG_403),
]

LINEA_1 = "- Ejemplo Uno (2014-03-02): 1.234.567 cuentas. Datos expuestos: Correos electrónicos, Contraseñas."
LINEA_2 = "- Ejemplo Dos (2011-09-20): 980 cuentas. Datos expuestos: Correos electrónicos."
EJEMPLOS_PRESENTAR_DOMINIO = [
    (("ejemplo.com", Resultado(True, [])), "No hay filtraciones registradas para ejemplo.com."),
    (("ejemplo.com", Resultado(True, [RESUMEN_1])), f"1 filtración asociada a ejemplo.com:\n{LINEA_1}"),
    (("ejemplo.com", Resultado(True, [RESUMEN_2, RESUMEN_1])),
     f"2 filtraciones asociadas a ejemplo.com:\n{LINEA_2}\n{LINEA_1}"),
    (("ejemplo.com", Resultado(False, MSG_LIMITE)), MSG_LIMITE),
    (("x.org", Resultado(True, [{"titulo": "Sin datos", "fecha": "", "cuentas": 5, "datos": ()}])),
     "1 filtración asociada a x.org:\n- Sin datos (): 5 cuentas. Datos expuestos: sin detalle."),
]

EJEMPLOS_MODO_CONTRASENAS = [
    ((entorno_de_prueba(["1"], "password", http_que_devuelve(respuesta(200, CUERPO_SHA1))),),
     "Tu contraseña (SHA1) aparece 3 veces en filtraciones conocidas. Cámbiala."),
    ((entorno_de_prueba(["2"], "password", http_que_devuelve(respuesta(200, CUERPO_NTLM))),),
     "Tu contraseña (NTLM) aparece 52.256 veces en filtraciones conocidas. Cámbiala."),
    ((entorno_de_prueba(["2"], "otra", http_que_devuelve(respuesta(200, CUERPO_NTLM))),),
     "Tu contraseña (NTLM) no aparece en ninguna filtración conocida por Have I Been Pwned."),
    ((entorno_de_prueba(["9"]),), "Opción de formato no válida."),
    ((entorno_de_prueba(["1"], "x", http_que_falla(requests.Timeout())),), ERRORES_RED[requests.Timeout]),
    ((entorno_de_prueba(["1"], "x", http_que_devuelve(respuesta(503))),), MSG_503),
]

EJEMPLOS_MODO_DOMINIOS = [
    ((entorno_de_prueba(["https://www.Ejemplo.com/login"],
                        http_get=http_que_devuelve(respuesta(200, datos=[BRECHA_1]), URL_BRECHAS, {"Domain": "ejemplo.com"})),),
     f"1 filtración asociada a ejemplo.com:\n{LINEA_1}"),
    ((entorno_de_prueba(["   "]),), "No has indicado ningún dominio."),
    ((entorno_de_prueba(["limpio.org"], http_get=http_que_devuelve(respuesta(404))),),
     "No hay filtraciones registradas para limpio.org."),
    ((entorno_de_prueba(["raro"], http_get=http_que_devuelve(respuesta(400))),), MSG_400_DOMINIO),
    ((entorno_de_prueba(["ejemplo.com"], http_get=http_que_falla(requests.ConnectionError())),),
     ERRORES_RED[requests.ConnectionError]),
]

EJEMPLOS_EJECUTAR = [
    ((entorno_de_prueba(["1", "1"], "password", http_que_devuelve(respuesta(200, CUERPO_SHA1))),),
     "Tu contraseña (SHA1) aparece 3 veces en filtraciones conocidas. Cámbiala."),
    ((entorno_de_prueba([" 2 ", "limpio.org"], http_get=http_que_devuelve(respuesta(404))),),
     "No hay filtraciones registradas para limpio.org."),
    ((entorno_de_prueba(["3"]),), "Modo no válido. Elige 1 o 2."),
    ((entorno_de_prueba([""]),), "Modo no válido. Elige 1 o 2."),
    ((entorno_de_prueba(["2", "ejemplo.com"], http_get=http_que_devuelve(respuesta(200, datos=[BRECHA_1, BRECHA_2]))),),
     f"2 filtraciones asociadas a ejemplo.com:\n{LINEA_2}\n{LINEA_1}"),
]


def comprobar(funcion, ejemplos):
    """Llama a `funcion` con cada ejemplo y falla si el resultado no coincide."""
    def uno(ejemplo):
        argumentos, esperado = ejemplo
        obtenido = funcion(*argumentos)
        assert obtenido == esperado, f"{funcion.__name__}: {obtenido!r} != {esperado!r}"
        return f"  caso correcto -> {_resumir(obtenido)}"

    print(f"{funcion.__name__}: {len(ejemplos)} ejemplos")
    print("\n".join(map(uno, ejemplos)))


def _resumir(valor, limite=90):
    texto = repr(valor).replace("\n", " ")
    return texto if len(texto) <= limite else texto[: limite - 3] + "..."


def ejecutar_ejemplos():
    casos = [
        (hash_sha1, EJEMPLOS_HASH_SHA1),
        (hash_ntlm, EJEMPLOS_HASH_NTLM),
        (despachar, EJEMPLOS_DESPACHAR),
        (limpiar_dominio, EJEMPLOS_LIMPIAR_DOMINIO),
        (contar_filtraciones, EJEMPLOS_CONTAR_FILTRACIONES),
        (listar_brechas, EJEMPLOS_LISTAR_BRECHAS),
        (gestionar_respuesta, EJEMPLOS_GESTIONAR_RESPUESTA),
        (comprobar_contrasena, EJEMPLOS_COMPROBAR_CONTRASENA),
        (comprobar_dominio, EJEMPLOS_COMPROBAR_DOMINIO),
        (presentar_contrasena, EJEMPLOS_PRESENTAR_CONTRASENA),
        (presentar_dominio, EJEMPLOS_PRESENTAR_DOMINIO),
        (modo_contrasenas, EJEMPLOS_MODO_CONTRASENAS),
        (modo_dominios, EJEMPLOS_MODO_DOMINIOS),
        (ejecutar, EJEMPLOS_EJECUTAR),
    ]
    list(map(lambda caso: comprobar(*caso), casos))
    print("\nTodos los ejemplos de la parte 2 son correctos (sin usar la red).")


if __name__ == "__main__":
    if "--ejemplos" in sys.argv[1:]:
        ejecutar_ejemplos()
    else:
        ejecutar(entorno_real())
