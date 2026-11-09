# Práctica de Programación Funcional (Unidades 1 y 2)

**Autor:** Ismael Hernández  
**Asignatura:** Programación, paradigmas  
**Curso:** 5.º de Ingeniería Informática · U-tad

## Descripción

La práctica implementa, en un único archivo de Python, los cuatro ejercicios de la parte 1 y el comprobador de contraseñas y dominios de Have I Been Pwned de la parte 2. El objetivo no es solo que el código funcione, sino que cada decisión se apoye en las herramientas del paradigma funcional: funciones puras, `map`, `filter`, `reduce`, lambdas, closures, funciones de orden superior y callbacks.

## Estructura

```text
AEC1/
├── practica_programacion_funcional.py   # código completo, partes 1 y 2
├── requirements.txt                     # dependencias con versiones fijadas
├── explicacion_programacion_funcional.pdf
└── README.md
```

La entrega se comprime como `AEC1_ProgramacionFuncional_IsmaelHernandez.zip` e incluye estos cuatro archivos.

## Requisitos e instalación

Se recomienda un entorno virtual:

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Dependencias principales:

- `requests`, para las peticiones HTTP.
- `pycryptodome`, para calcular NTLM mediante MD4, ya que `hashlib` no incluye MD4 en todas las instalaciones.

## Ejecución

Desde la carpeta de la práctica:

```bash
# Ejemplos de las dos partes, sin usar la red
python practica_programacion_funcional.py --ejemplos

# Solo los ejemplos de la parte 1
python practica_programacion_funcional.py --parte1

# Modo interactivo de la parte 2 (contraseñas y dominios)
python practica_programacion_funcional.py --parte2

# Sin argumentos: abre directamente el modo interactivo de la parte 2
python practica_programacion_funcional.py
```

En el modo de contraseñas se elige SHA1 o NTLM y se escribe la contraseña con `getpass`, de modo que no se muestra en pantalla. En el modo de dominios se acepta un dominio o una URL y se normaliza antes de consultar la API.

## Organización del código

### Parte 1. Ejercicios funcionales

- `es_palindromo` y `palindromos`: normalización con `filter`, comparación con la cadena invertida y `map` sobre la lista.
- `cuadrados_sumados`: acumulación con `reduce` sobre `range(1, n + 1)`.
- `factorial`: `reduce` con valor inicial 1; se evita la recursión.
- `promedio_al_menos` y `filtrar_aprobados`: closure que fabrica el predicado y `filter` para devolver una lista nueva.

Cada función tiene al menos cinco ejemplos de comprobación. Los ejemplos se ejecutan con `assert` y se imprimen en el terminal.

### Parte 2. Have I Been Pwned

- `despachar`: selecciona un callback a partir de una tabla y una clave.
- `FORMATOS`: tabla que asocia cada opción con su función de hash y sus parámetros de petición.
- `MANEJADORES_DOMINIO` y `manejadores_rango`: tablas de callbacks por código HTTP.
- `error`, `partial` y `protegida`: funciones de orden superior para construir respuestas de error y envolver las peticiones.
- `Entorno`: `namedtuple` que inyecta entrada, salida y `http_get`; así los modos se prueban sin red.
- `MODOS`: tabla de callbacks para elegir entre contraseñas y dominios.

Las consultas envían únicamente los cinco primeros caracteres del hash en el modo de contraseñas. Las respuestas de los ejemplos son simuladas y están marcadas como inventadas.

## Uso del paradigma funcional

| Concepto | Dónde se aplica |
| --- | --- |
| Funciones puras | Normalización, palíndromos, factorial, suma de cuadrados y filtrado. |
| `map` | Lista de palíndromos, resumen de brechas y presentación de ejemplos. |
| `filter` | Normalización de texto, filtrado de aprobados y selección de líneas del rango. |
| `reduce` | Suma de cuadrados, factorial y recuento de filtraciones. |
| Lambdas | Predicados, acumuladores y callbacks sencillos. |
| Closures | `promedio_al_menos` captura la nota mínima; `error` captura el mensaje. |
| Funciones de orden superior | `despachar`, `protegida`, `partial` y las tablas de manejadores. |
| Callbacks | Selección de modo, formato de hash y tratamiento de códigos HTTP. |
| Separación de efectos | `Entorno` inyecta `input`, `getpass`, `print` y `requests.get`. |

No se utilizan bucles `for` ni `while` en la lógica de la práctica. Las estructuras imperativas se sustituyen por composición de funciones.

## Relación con la rúbrica

| Criterio | Evidencia |
| --- | --- |
| Criterio 1: parte 1 completa | Las cuatro funciones están implementadas y tienen seis ejemplos cada una. |
| Criterio 2: parte 2 funcional | Callbacks para modo, hash y errores; `despachar`, `partial`, closures y `Entorno`. |
| Ejemplos | `--ejemplos` ejecuta más de cinco casos por función sin usar la red. |
| Explicación | `explicacion_programacion_funcional.pdf`, de una página, explica el uso del paradigma en cada bloque. |
| Entrega | ZIP con código, `requirements.txt`, PDF y este README. |

## Fuente de los ejercicios

La parte 1 está inspirada en katas clásicas de la plataforma **Codewars** (<https://www.codewars.com/>): detección de palíndromos, suma de cuadrados, factorial y filtrado de estudiantes. Las soluciones se han reescrito desde cero con el enfoque funcional de la asignatura; no se copia código de la plataforma. La parte 2 sigue la documentación oficial de Have I Been Pwned:

- Pwned Passwords, búsqueda por rango: <https://haveibeenpwned.com/API/v3#PwnedPasswords>
- Breaches, consulta por dominio: <https://haveibeenpwned.com/API/v3#Breaches>

## Decisiones y limitaciones

- NTLM se calcula como MD4 de la contraseña en UTF-16 little endian; por eso se usa `pycryptodome`.
- La API de contraseñas solo recibe el prefijo del hash; el resto se compara en local.
- La cabecera `Add-Padding` reduce diferencias de tamaño entre respuestas.
- Un `404` en la consulta de dominio se interpreta como “sin filtraciones”, no como error.
- Los ejemplos de la parte 2 no hacen peticiones reales; usan respuestas simuladas para que la corrección sea reproducible.
- No se gestionan excepciones por tipos incorrectos, tal como indica el enunciado.
- La disponibilidad y el límite de peticiones dependen de la API externa.
