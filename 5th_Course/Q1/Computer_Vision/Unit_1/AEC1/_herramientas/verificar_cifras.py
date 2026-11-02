from pathlib import Path
import re
import subprocess

import pandas as pd

ENT = Path("U1_Practica_Hernandez_Ismael")
OUT = ENT / "outputs"
MEM = ENT / "memoria"

# Extraer texto del PDF
txt_pdf = subprocess.run(
    ["pdftotext", str(MEM / "informe.pdf"), "-"],
    check=True, capture_output=True, text=True
).stdout
txt_contrato = (MEM / "contrato_preprocesado.md").read_text()

# Quitar fechas, cursos y números de página antes de buscar cifras
def limpiar(texto):
    texto = re.sub(r"\d{1,2} de [a-záéíóú]+ de \d{4}", " ", texto)
    texto = re.sub(r"20\d{2}\s*[–-]\s*20\d{2}", " ", texto)
    texto = re.sub(r"\b20\d{2}\b", " ", texto)
    texto = texto.replace("SHA-256", "SHA")
    texto = re.sub(r"(?i)\b(Figura|Tabla)\s+\d+", r"\1", texto)
    # números de página: una línea que solo contiene un número
    texto = re.sub(r"(?m)^\s*\d{1,3}\s*$", " ", texto)
    return texto

pdf = limpiar(txt_pdf)
contrato = limpiar(txt_contrato)

# Valores de todos los CSV de outputs
valores = set()
textos_csv = []
for ruta in sorted(OUT.glob("*.csv")):
    df = pd.read_csv(ruta)
    for celda in df.astype(str).to_numpy().ravel():
        textos_csv.append(celda)
        for token in re.findall(r"-?\d+(?:[.,]\d+)?", celda):
            try:
                valores.add(float(token.replace(",", ".")))
            except ValueError:
                pass

# Añadir enteros con separador de miles tal como aparecen en la memoria
for celda in textos_csv:
    for token in re.findall(r"\d{1,3}(?:\.\d{3})+", celda):
        try:
            valores.add(float(token.replace(".", "")))
        except ValueError:
            pass

def norm(token):
    return float(token.replace(".", "").replace(",", ".")) if re.fullmatch(r"\d{1,3}(?:\.\d{3})+", token) else float(token.replace(",", "."))

def respaldado(token):
    try:
        v = norm(token)
    except ValueError:
        return True
    decimales = len(token.split(",")[1]) if "," in token and "." not in token else (
        len(token.split(".")[1]) if "." in token and token.count(".") == 1 else 0
    )
    if decimales == 0:
        tol = 0.5
    elif decimales == 1:
        tol = 0.05
    elif decimales == 2:
        tol = 0.005
    else:
        tol = 10 ** (-decimales) / 2
    return any(abs(v - x) <= tol for x in valores)

patron = re.compile(r"-?\d{1,3}(?:\.\d{3})+(?:,\d+)?|-?\d+(?:[.,]\d+)?")
faltan = []
for nombre, texto in [("informe.pdf", pdf), ("contrato", contrato)]:
    for m in patron.finditer(texto):
        token = m.group(0)
        # Los enteros de una cifra son números de sección o de listas
        if re.fullmatch(r"-?\d", token):
            continue
        if not respaldado(token):
            ini = max(0, m.start() - 60)
            fin = min(len(texto), m.end() + 60)
            faltan.append((nombre, token, " ".join(texto[ini:fin].split())))

if faltan:
    print("Cifras sin respaldo directo en los CSV:")
    for nombre, token, contexto in faltan:
        print(f"  [{nombre}] {token}: ...{contexto}...")
    raise SystemExit(1)
print("Todas las cifras con más de una cifra están respaldadas por algún CSV.")
