# Ejercicios 04 — POO + Excepciones

## Checklist (TO‑DO)
- [ ] Crear clases con responsabilidades claras
- [ ] Separar parsing/normalización de indexación
- [ ] Definir excepciones propias

## Ejercicio 04.1 — Clase `Tokenizer`
Crea una clase `Tokenizer` con método `tokenize(text)` configurable (lowercase, remove_punct).

## Ejercicio 04.2 — Clase `InvertedIndex`
Implementa:
- `add_document(doc_id, text)`
- `query_and(terms)`
- `query_or(terms)`

## Ejercicio 04.3 — Excepción `EmptyQueryError`
Lanza esta excepción si `terms` está vacío.

Archivo: [04_index_oop.py](04_index_oop.py)
