# Ejercicios 06 — CSV + JSON

Datasets: `datasets/ventas.csv`, `datasets/users.json`, `datasets/docs.jsonl`

## Checklist (TO‑DO)
- [ ] Leer CSV con `csv.DictReader`
- [ ] Validar tipos y campos
- [ ] Leer JSON y extraer estructuras
- [ ] Leer JSONL (streaming línea a línea)

## Ejercicio 06.1 — Reporte anual desde CSV (sin pandas)
Archivo: [06_csv_report.py](06_csv_report.py)

Tareas:
- Lee `ventas.csv`
- Agrupa ventas por vendedor
- Imprime el top vendedor y su total

## Ejercicio 06.2 — Usuarios activos desde JSON
Archivo: [06_users_active.py](06_users_active.py)

Tareas:
- Lee `users.json`
- Filtra `active == true`
- Imprime nombres y ciudad

## Ejercicio 06.3 — Lectura de JSONL
Archivo: [06_read_jsonl_docs.py](06_read_jsonl_docs.py)

Tareas:
- Lee `docs.jsonl`
- Crea un dict `doc_id -> text`
- Muestra cuántos docs hay
