"""Comprueba que las cifras de la memoria y de hallazgos salen de los CSV.

Uso:
    _trabajo/venv/bin/python _herramientas/verificar_cifras.py
    _trabajo/venv/bin/python _herramientas/verificar_cifras.py --estricto

El modo estricto falla si encuentra un número que no esté en ningún CSV ni en la
lista de constantes estructurales. En el modo normal solo avisa.

Este script se completa en la Fase 10. En Fase 0 sirve de esqueleto: si todavía
no hay PDF, lo dice y termina sin error.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
ENT = RAIZ / "U2_Practica_Hernandez_Ismael"
OUT = ENT / "outputs"
MEM = ENT / "memoria"

# Constantes estructurales que no son resultados: tamaños, niveles, años,
# números de figura o sección, parámetros del enunciado.
PERMITIDOS = {
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 30, 40,
    45, 60, 70, 75, 80, 85, 90, 95, 100, 180, 255, 512, 768,
    2026, 20260101, 20260102,
    0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.85, 1.0, 1.25, 1.3,
    1.5, 1.6, 1.7, 2.0, 3.0, 5.0,
}

NUM_TEXTO = re.compile(r"-?\d+(?:[.,]\d+)*")
NUM_CSV = re.compile(r"-?\d+(?:[.,]\d+)?")


def normalizar_texto(token: str) -> float | None:
    """Convierte un número escrito en español a float."""
    token = token.strip()
    if re.fullmatch(r"\d{1,3}(?:\.\d{3})+", token):
        return float(token.replace(".", ""))
    token = token.replace(".", "").replace(",", ".") if token.count(",") == 1 else token.replace(",", ".")
    try:
        return float(token)
    except ValueError:
        return None


def normalizar_csv(token: str) -> float | None:
    token = token.strip().replace(",", ".")
    try:
        return float(token)
    except ValueError:
        return None


def limpiar_texto(texto: str) -> str:
    texto = re.sub(r"https?://\S+", " ", texto)
    texto = re.sub(r"[0-9a-f]{16,}", " ", texto)
    texto = re.sub(r"\d{1,2} de [a-záéíóú]+ de \d{4}", " ", texto, flags=re.IGNORECASE)
    texto = re.sub(r"20\d{2}\s*[–-]\s*20\d{2}", " ", texto)
    texto = re.sub(r"\b20\d{2}\b", " ", texto)
    texto = re.sub(r"(?i)\b(Figura|Tabla|Sección|Ecuación)\s+\d+", r"\1", texto)
    texto = re.sub(r"(?m)^\s*\d{1,3}\s*$", " ", texto)
    return texto


def texto_pdf() -> str:
    ruta = MEM / "informe.pdf"
    if not ruta.exists():
        return ""
    salida = subprocess.run(
        ["pdftotext", str(ruta), "-"],
        check=True,
        capture_output=True,
        text=True,
    )
    return salida.stdout


def valores_de_csv() -> tuple[set[float], list[str]]:
    valores: set[float] = set()
    origenes: list[str] = []
    if not OUT.exists():
        return valores, origenes
    for ruta in sorted(OUT.glob("*.csv")):
        origenes.append(ruta.name)
        df = pd.read_csv(ruta)
        for celda in df.astype("string").fillna("").to_numpy(dtype=str).ravel():
            for token in NUM_CSV.findall(celda):
                valor = normalizar_csv(token)
                if valor is not None:
                    valores.add(valor)
    return valores, origenes


def redondear(valor: float) -> float:
    return round(valor, 3)


def esta_respaldado(valor: float, valores: set[float]) -> bool:
    candidatos = {valor, valor / 100.0, valor * 100.0}
    for candidato in candidatos:
        for decimales in (0, 1, 2, 3):
            if any(abs(redondear(candidato) - redondear(v)) <= 0.5 * 10 ** (-decimales) for v in valores):
                return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--estricto", action="store_true")
    args = parser.parse_args()

    partes = []
    if (MEM / "hallazgos.md").exists():
        partes.append((MEM / "hallazgos.md").read_text(encoding="utf-8"))
    informe_md = MEM / "informe.md"
    if informe_md.exists():
        partes.append(informe_md.read_text(encoding="utf-8"))
    else:
        pdf = texto_pdf()
        if pdf:
            partes.append(pdf)
    if not partes:
        print("Todavía no hay memoria/informe.pdf ni memoria/hallazgos.md.")
        return 0

    valores, origenes = valores_de_csv()
    if not origenes:
        print("Todavía no hay CSV en outputs/.")
        return 0

    texto = limpiar_texto("\n".join(partes))
    no_respaldados: list[tuple[float, str]] = []
    total = 0
    for linea in texto.splitlines():
        for token in NUM_TEXTO.findall(linea):
            valor = normalizar_texto(token)
            if valor is None:
                continue
            total += 1
            if valor in PERMITIDOS or esta_respaldado(valor, valores):
                continue
            no_respaldados.append((valor, linea.strip()[:160]))

    print(f"CSV leídos: {len(origenes)}")
    print(f"Números encontrados: {total}")
    print(f"Sin respaldo: {len(no_respaldados)}")
    for valor, contexto in no_respaldados:
        print(f"  {valor:g}  |  {contexto}")

    if args.estricto and no_respaldados:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
