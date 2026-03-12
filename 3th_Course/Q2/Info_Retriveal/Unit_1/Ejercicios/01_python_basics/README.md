# Ejercicios 01 — Python basics

## Checklist (TO‑DO)
- [ ] Variables, prints, f-strings
- [ ] Strings: slicing, split, join
- [ ] Lectura de entrada y validación
- [ ] Funciones pequeñas y reutilizables

## Ejercicio 01.1 — Normalizador de texto (IR básico)
Implementa una función `normalize(text: str) -> str` que:
- pase a minúsculas
- elimine espacios repetidos
- elimine signos simples (`.,;:!?()[]{}"'`) sustituyéndolos por espacio

Archivo: [01_normalize.py](01_normalize.py)

## Ejercicio 01.2 — Tokenizador
Implementa `tokenize(text: str) -> list[str]` que use `normalize` y devuelva tokens.

## Ejercicio 01.3 — Frecuencias
Implementa `term_frequencies(tokens) -> dict[str, int]`.
