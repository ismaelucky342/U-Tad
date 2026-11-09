"""Parte 1: ejercicios de programación funcional.

Todo el código usa funciones puras (sin tocar variables externas ni mutar
los argumentos) y las herramientas habituales del estilo funcional: map,
filter, reduce, lambdas, closures y funciones que reciben otras funciones.
"""
import unicodedata
from functools import reduce


# --- 1. Palíndromos ---------------------------------------------------------

def _normalizar(texto):
    """Pasa a minúsculas, quita tildes y se queda solo con letras y dígitos.

    Quitar tildes también convierte la ñ en n; para esta práctica no importa.
    """
    descompuesto = unicodedata.normalize("NFD", texto.lower())
    sin_tildes = filter(lambda c: not unicodedata.combining(c), descompuesto)
    return "".join(filter(str.isalnum, sin_tildes))


def es_palindromo(texto):
    """True si el texto se lee igual al derecho y al revés.

    Se ignoran mayúsculas, tildes, espacios y signos de puntuación. La cadena
    vacía cuenta como palíndromo.
    """
    limpio = _normalizar(texto)
    return limpio == limpio[::-1]


def palindromos(textos):
    """Devuelve una lista de booleanos, uno por cada string de entrada."""
    return list(map(es_palindromo, textos))


# --- 2. Suma de cuadrados ---------------------------------------------------

def cuadrados_sumados(n):
    """Suma de los cuadrados de los números entre 1 y n (ambos incluidos)."""
    return reduce(lambda acumulado, k: acumulado + k * k, range(1, n + 1), 0)


# --- 3. Factorial -----------------------------------------------------------

def factorial(n):
    """Factorial de n. Con reduce se evita la recursión y su límite de pila."""
    return reduce(lambda acumulado, k: acumulado * k, range(2, n + 1), 1)


# --- 4. Estudiantes aprobados -----------------------------------------------

NOTA_MINIMA = 6


def promedio(calificaciones):
    """Media de una lista de notas; 0 si la lista está vacía."""
    return sum(calificaciones) / len(calificaciones) if calificaciones else 0.0


def promedio_al_menos(minimo):
    """Fabrica el predicado 'este estudiante tiene promedio >= minimo'.

    Es una función que devuelve otra función (closure): el valor de `minimo`
    queda capturado y filter solo tiene que ir llamándola con cada estudiante.
    """
    return lambda estudiante: promedio(estudiante["calificaciones"]) >= minimo


def filtrar_aprobados(estudiantes, nota_minima=NOTA_MINIMA):
    """Estudiantes cuyo promedio es mayor o igual que la nota mínima.

    Devuelve una lista nueva; la lista original no se modifica.
    """
    return list(filter(promedio_al_menos(nota_minima), estudiantes))


# --- Ejemplos ---------------------------------------------------------------

ESTUDIANTES = [
    {"nombre": "Juan", "calificaciones": [7, 8, 6, 5]},
    {"nombre": "Ana", "calificaciones": [9, 6, 8]},
    {"nombre": "Pedro", "calificaciones": [4, 5, 3]},
    {"nombre": "Maria", "calificaciones": [10, 9, 9]},
    {"nombre": "Luis", "calificaciones": [3, 2, 5]},
]

EJEMPLOS_ES_PALINDROMO = [
    (("Anita lava la tina",), True),
    (("reconocer",), True),
    (("Átale, demoniaco Caín, o me delata",), True),
    (("A man, a plan, a canal: Panama",), True),
    (("programación funcional",), False),
    (("",), True),
]

EJEMPLOS_PALINDROMOS = [
    ((["ana", "casa", "oso"],), [True, False, True]),
    ((["Neuquén", "Python", "Somos o no somos"],), [True, False, True]),
    (([],), []),
    ((["abc", "abcba", "abccba", "abca"],), [False, True, True, False]),
    ((["Dábale arroz a la zorra el abad"],), [True]),
    ((["12321", "12345"],), [True, False]),
]

EJEMPLOS_CUADRADOS_SUMADOS = [
    ((0,), 0),
    ((1,), 1),
    ((3,), 14),
    ((5,), 55),
    ((10,), 385),
    ((100,), 338350),
]

EJEMPLOS_FACTORIAL = [
    ((0,), 1),
    ((1,), 1),
    ((5,), 120),
    ((7,), 5040),
    ((10,), 3628800),
    ((20,), 2432902008176640000),
]

EJEMPLOS_FILTRAR_APROBADOS = [
    ((ESTUDIANTES,), [ESTUDIANTES[0], ESTUDIANTES[1], ESTUDIANTES[3]]),
    (([],), []),
    (([{"nombre": "Eva", "calificaciones": [6, 6, 6]}],),
     [{"nombre": "Eva", "calificaciones": [6, 6, 6]}]),
    (([{"nombre": "Teo", "calificaciones": [5, 7]},
       {"nombre": "Noa", "calificaciones": [5, 6]}],),
     [{"nombre": "Teo", "calificaciones": [5, 7]}]),
    ((ESTUDIANTES, 9), [ESTUDIANTES[3]]),
    ((ESTUDIANTES, 0), ESTUDIANTES),
]


def comprobar(funcion, ejemplos):
    """Llama a `funcion` con cada ejemplo, lo imprime y falla si no coincide."""
    def uno(ejemplo):
        argumentos, esperado = ejemplo
        obtenido = funcion(*argumentos)
        assert obtenido == esperado, f"{funcion.__name__}{argumentos}: {obtenido} != {esperado}"
        llamada = ", ".join(map(_resumir, argumentos))
        return f"  {funcion.__name__}({llamada}) -> {_resumir(obtenido)}"

    print(f"{funcion.__name__}: {len(ejemplos)} ejemplos")
    print("\n".join(map(uno, ejemplos)))


def _resumir(valor, limite=60):
    texto = repr(valor)
    return texto if len(texto) <= limite else texto[: limite - 3] + "..."


def ejecutar_ejemplos():
    casos = [
        (es_palindromo, EJEMPLOS_ES_PALINDROMO),
        (palindromos, EJEMPLOS_PALINDROMOS),
        (cuadrados_sumados, EJEMPLOS_CUADRADOS_SUMADOS),
        (factorial, EJEMPLOS_FACTORIAL),
        (filtrar_aprobados, EJEMPLOS_FILTRAR_APROBADOS),
    ]
    list(map(lambda caso: comprobar(*caso), casos))
    print("\nTodos los ejemplos de la parte 1 son correctos.")


if __name__ == "__main__":
    ejecutar_ejemplos()
