# Ejercicios 08 — Pandas

Dataset sugerido: `datasets/ventas.csv`

## Checklist (TO‑DO)
- [ ] `read_csv`, `head`, `info`, `describe`
- [ ] Selección de columnas
- [ ] Filtros por condición
- [ ] Columnas derivadas
- [ ] `groupby` + agregaciones
- [ ] `merge` / `concat`
- [ ] Exportación a CSV/JSON/Parquet

## Ejercicio 08.1 — EDA mínima
Archivo: [08_eda_ventas.py](08_eda_ventas.py)

Tareas:
- Carga el CSV
- Imprime `shape`, `head`, `info`
- Calcula ventas totales por ciudad
- Top 2 vendedores por ventas

## Ejercicio 08.2 — Limpieza
- Convierte `ventas` a numérico si viniera como string
- Detecta valores vacíos y rellena con 0

## Ejercicio 08.3 — Exportación
- Guarda un CSV con ventas por ciudad
- Guarda un JSON con ventas por vendedor
