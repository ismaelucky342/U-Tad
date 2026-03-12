# Ejercicios 02 — Estructuras de datos (listas/dicts/sets) aplicadas a IR

## Checklist (TO‑DO)
- [ ] Dominar `dict.get` para contadores
- [ ] Usar `set` para operaciones booleanas (AND/OR)
- [ ] Representar postings lists
- [ ] Entender complejidad temporal aproximada (O(1) dict/set)

## Ejercicio 02.1 — Contador de tokens
A partir de una lista de tokens, crea:
- `tf`: dict token->frecuencia
- `df`: dict token->número de documentos donde aparece

## Ejercicio 02.2 — Posting list mínima
Implementa un índice invertido básico:
`index[token] = set(doc_ids)`

Archivo: [02_inverted_index_sets.py](02_inverted_index_sets.py)

## Ejercicio 02.3 — Posting list con TF
Sube el nivel:
`index[token] = {doc_id: tf}`

Archivo: [02_inverted_index_tf.py](02_inverted_index_tf.py)
