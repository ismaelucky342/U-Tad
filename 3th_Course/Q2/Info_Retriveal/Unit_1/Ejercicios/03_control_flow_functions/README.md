# Ejercicios 03 — Control de flujo + funciones

## Checklist (TO‑DO)
- [ ] `if/elif/else` con validación
- [ ] `for` + `enumerate`
- [ ] Funciones puras (sin side-effects) vs funciones con IO
- [ ] `argparse` (opcional)

## Ejercicio 03.1 — Validador de entrada
Implementa una función `parse_int(value: str) -> int` que:
- convierta a int
- lance un error con mensaje claro si no es válido

## Ejercicio 03.2 — CLI simple para consultas
Crea un script que reciba términos y muestre documentos recuperados.

Archivo: [03_cli_query.py](03_cli_query.py)

Requisitos:
- si faltan términos, imprime ayuda
- si el modo es `and`, usa intersección
- si el modo es `or`, usa unión
