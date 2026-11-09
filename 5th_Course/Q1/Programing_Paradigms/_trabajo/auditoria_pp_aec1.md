# Auditoría de la práctica de Programación Funcional (AEC1)

## Veredicto

La práctica está completa y se puede entregar. He unificado el código en un único archivo, he revisado el PDF y he añadido un README con la estructura, la ejecución y la relación con la rúbrica. Los ejemplos de las dos partes pasan sin errores y el PDF sigue teniendo una sola página.

## Revisión de la rúbrica

| Criterio | Evidencia | Valoración |
| --- | --- | --- |
| Criterio 1: parte 1 completa | `es_palindromo`, `palindromos`, `cuadrados_sumados`, `factorial` y `filtrar_aprobados`; seis ejemplos por función. | Cubierto. |
| Criterio 2: parte 2 funcional | Callbacks para modo, hash y códigos HTTP; `despachar`, `partial`, closures, `Entorno` y tablas de manejadores. | Cubierto. |
| Uso real del paradigma | Sin `for` ni `while`; `map`, `filter`, `reduce`, lambdas y funciones de orden superior. | Cubierto. |
| Ejemplos | `--ejemplos` ejecuta las dos partes con respuestas simuladas; más de cinco casos por función. | Cubierto. |
| Explicación | `explicacion_programacion_funcional.pdf`, una página, con el uso del paradigma en cada bloque. | Cubierto. |
| Entrega | ZIP con código, `requirements.txt`, PDF y README. | Preparado. |

## Comprobaciones realizadas

- `practica_programacion_funcional.py --ejemplos`: todas las comprobaciones de la parte 1 y de la parte 2 pasan.
- Dependencias instaladas en un directorio temporal: `requests==2.34.2` y `pycryptodome==4.3.0` existen y permiten ejecutar los ejemplos.
- No hay bucles `for` ni `while` en la lógica.
- El PDF tiene una página y sigue siendo legible.
- El README explica la estructura, la instalación, la ejecución, el diseño funcional y la fuente de los ejercicios.
- La parte 1 se presenta como inspirada en katas clásicas de Codewars, reescritas desde cero; no se copia código de la plataforma.

## Cambios de organización

- Se eliminó la separación en `parte1_funciones.py` y `parte2_haveibeenpwned.py`.
- Todo el código vive en `practica_programacion_funcional.py`, con dos secciones internas y un único punto de entrada.
- Los archivos antiguos se conservan en `_trabajo/versiones_anteriores/` por si hace falta comparar.
- El PDF se regeneró para referirse al archivo único y a Codewars como fuente de la parte 1.

## Observaciones menores

- La API real no se ha consultado en la auditoría; los ejemplos cubren respuestas 200, 400, 403, 404, 429, 503 y errores de red. Es suficiente para corregir sin depender de internet.
- Los `if` de validación y presentación se mantienen porque no sustituyen la lógica funcional: las decisiones de modo, formato y error se resuelven con callbacks.
- NTLM necesita `pycryptodome`; está en `requirements.txt` con versión fijada.
- El 404 de dominios se interpreta como «sin filtraciones», que es la decisión documentada en el README y en el PDF.
