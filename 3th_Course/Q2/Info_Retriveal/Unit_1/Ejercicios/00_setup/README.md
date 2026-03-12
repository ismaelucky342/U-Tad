# Ejercicios 00 — Setup del entorno

## Objetivo
Asegurar que tu entorno Python es reproducible y que sabes diagnosticar qué intérprete y qué `pip` estás usando.

## Checklist (TO‑DO)
- [ ] Verificar versión de Python
- [ ] Verificar ejecutable real (`sys.executable`)
- [ ] Crear `.venv` y activarlo
- [ ] Instalar una librería y confirmar que queda en el venv
- [ ] Exportar dependencias con `pip freeze`

## Ejercicio 00.1 — Diagnóstico del intérprete
Ejecuta [00_check_env.py](00_check_env.py) y guarda su salida en un fichero `output_env.txt`.

## Ejercicio 00.2 — Venv reproducible
1. Crea un venv en la raíz de `Unit_1` (recomendado `.venv`).
2. Instala `pandas` dentro del venv.
3. Genera un `requirements.txt`.

## Ejercicio 00.3 — Pip correcto
Repite la instalación usando `python -m pip` y explica (en 4-6 líneas) por qué es más seguro.
