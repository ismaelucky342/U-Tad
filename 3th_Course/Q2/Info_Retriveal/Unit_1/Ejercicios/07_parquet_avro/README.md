# Ejercicios 07 — Parquet + Avro (opcional por dependencias)

> Nota: Parquet/Avro requieren librerías externas (por ejemplo `pyarrow` para Parquet, `fastavro` para Avro).

## Checklist (TO‑DO)
- [ ] Instalar `pyarrow` (si procede)
- [ ] Exportar a Parquet desde Pandas
- [ ] Leer Parquet y comparar tamaño vs CSV
- [ ] (Opcional) serializar Avro con esquema

## Ejercicio 07.1 — CSV vs Parquet
1. Carga `datasets/ventas.csv` en Pandas.
2. Exporta a `ventas.parquet`.
3. Compara el tamaño de fichero en disco.

## Ejercicio 07.2 — JSONL a Parquet
1. Lee `datasets/docs.jsonl`.
2. Convierte a DataFrame.
3. Exporta a Parquet.

## Ejercicio 07.3 — Avro (teoría + práctica)
- Define un esquema simple para `users`.
- Serializa y deserializa.
