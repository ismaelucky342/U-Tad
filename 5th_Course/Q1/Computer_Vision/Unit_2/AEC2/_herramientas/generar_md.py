"""Convierte la memoria HTML a Markdown para revisión y edición.

No genera PDF. El Markdown vive en memoria/informe.md y las imágenes se
enlazan con rutas relativas a outputs/figuras/.
"""

from __future__ import annotations

import html
import re
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString, Tag

RAIZ = Path(__file__).resolve().parents[1]
ENT = RAIZ / "U2_Practica_Hernandez_Ismael"
FUENTE = RAIZ / "_trabajo" / "memoria_fuente" / "informe.html"
SALIDA = ENT / "memoria" / "informe.md"


def inline(node) -> str:
    partes: list[str] = []
    for child in node.children:
        if isinstance(child, NavigableString):
            partes.append(str(child))
        elif isinstance(child, Tag):
            name = child.name
            clases = child.get("class") or []
            if name == "code" or "codigo" in clases:
                texto = child.get_text(" ", strip=True).replace("`", "\\`")
                partes.append(f"`{texto}`")
            elif name == "strong":
                partes.append("**" + inline(child) + "**")
            elif name == "em":
                partes.append("*" + inline(child) + "*")
            elif name == "a":
                partes.append("[" + inline(child) + "](" + child.get("href", "") + ")")
            elif name == "br":
                partes.append("\n")
            else:
                partes.append(inline(child))
    texto = html.unescape("".join(partes))
    texto = re.sub(r"[ \t]+", " ", texto)
    texto = re.sub(r" *\n *", "\n", texto)
    return texto.strip()


def blockquote(texto: str) -> str:
    return "\n".join("> " + linea if linea else ">" for linea in texto.splitlines())


def tabla(t: Tag) -> str:
    lineas: list[str] = []
    cap = t.find("caption")
    if cap:
        lineas += ["**" + inline(cap) + "**", ""]
    head = t.find("thead")
    rows = head.find_all("tr") if head else []
    cuerpo = t.find("tbody")
    if cuerpo:
        rows += cuerpo.find_all("tr")
    if not rows:
        rows = t.find_all("tr")
    if not rows:
        return ""

    def celdas(tr):
        return [inline(c).replace("|", "\\|").replace("\n", " ") or " " for c in tr.find_all(["th", "td"])]

    cabecera = celdas(rows[0])
    n = len(cabecera)
    lineas.append("| " + " | ".join(cabecera) + " |")
    lineas.append("| " + " | ".join(["---"] * n) + " |")
    for tr in rows[1:]:
        valores = celdas(tr)
        valores += [" "] * (n - len(valores))
        lineas.append("| " + " | ".join(valores[:n]) + " |")
    return "\n".join(lineas)


def div(d: Tag) -> str:
    clases = d.get("class") or []
    if "codigo" in clases:
        return "```\n" + d.get_text("\n", strip=False).strip() + "\n```"
    if "hallazgo" in clases:
        strong = d.find("strong")
        texto = inline(d)
        if strong:
            titulo = inline(strong)
            return "**" + titulo + "** " + texto[len(titulo):].strip()
        return texto
    if "nota" in clases:
        return blockquote(inline(d))
    partes: list[str] = []
    for child in d.children:
        if isinstance(child, Tag):
            if child.name in ("h3", "h4"):
                partes.append("**" + inline(child) + "**")
            elif child.name == "p":
                partes.append(inline(child))
            elif child.name == "ul":
                partes += ["- " + inline(li) for li in child.find_all("li", recursive=False)]
            else:
                partes.append(inline(child))
    return "\n\n".join(p for p in partes if p)


def normalizar_notion(texto: str) -> str:
    """Une las líneas partidas para que Notion no las importe como cortes."""
    lineas = texto.splitlines()
    salida: list[str] = []
    tipo = None
    bloque: list[str] = []

    def cerrar() -> None:
        nonlocal tipo, bloque
        if not bloque:
            tipo = None
            return
        if tipo == "quote":
            contenido = " ".join(x.lstrip(">").strip() for x in bloque if x.lstrip(">").strip())
            if contenido:
                salida.append("> " + contenido)
        elif tipo == "list":
            primero = bloque[0].rstrip()
            resto = " ".join(x.strip() for x in bloque[1:] if x.strip())
            salida.append(primero + ((" " + resto) if resto else ""))
        else:
            contenido = " ".join(x.strip() for x in bloque if x.strip())
            if contenido:
                salida.append(contenido)
        tipo = None
        bloque = []

    en_codigo = False
    for linea in lineas:
        if linea.strip().startswith("```"):
            cerrar()
            salida.append(linea.rstrip())
            en_codigo = not en_codigo
            continue
        if en_codigo:
            salida.append(linea)
            continue
        if not linea.strip():
            cerrar()
            if salida and salida[-1] != "":
                salida.append("")
            continue
        if linea.startswith("|"):
            cerrar()
            salida.append(linea.rstrip())
            continue
        if linea.startswith("#"):
            cerrar()
            salida.append(linea.rstrip())
            continue
        if linea.lstrip().startswith(">"):
            if tipo != "quote":
                cerrar()
                tipo = "quote"
            bloque.append(linea)
            continue
        if re.match(r"^\s*([-*+]|\d+\.)\s+", linea):
            cerrar()
            tipo = "list"
            bloque = [linea]
            continue
        if tipo == "list":
            bloque.append(linea)
            continue
        if tipo != "paragraph":
            cerrar()
            tipo = "paragraph"
        bloque.append(linea)
    cerrar()
    while salida and salida[-1] == "":
        salida.pop()
    return "\n".join(salida) + "\n"


def convertir() -> str:
    soup = BeautifulSoup(FUENTE.read_text(encoding="utf-8"), "html.parser")
    md: list[str] = []
    for ch in soup.body.find_all(recursive=False):
        if not isinstance(ch, Tag):
            continue
        name = ch.name
        clases = ch.get("class") or []
        if name == "section" and "portada" in clases:
            md += ["# " + inline(ch.find("h1")), ""]
            sub = ch.find(class_="sub")
            if sub:
                md += ["## " + inline(sub), ""]
            autor = ch.find(class_="autor")
            if autor:
                md += ["**" + inline(autor) + "**", ""]
            fecha = ch.find(class_="fecha")
            if fecha:
                md += ["*" + inline(fecha) + "*", ""]
            resumen = ch.find(class_="resumen")
            if resumen:
                md += [blockquote(inline(resumen)), ""]
        elif name == "section" and "indice" in clases:
            md += ["## Contenido", ""]
            for tr in ch.find_all("tr"):
                celdas = tr.find_all(["td", "th"])
                if len(celdas) >= 2:
                    md.append("- " + inline(celdas[0]) + ". " + inline(celdas[1]))
            md.append("")
        elif name in ("h1", "h2", "h3", "h4"):
            nivel = {"h1": "#", "h2": "##", "h3": "###", "h4": "####"}[name]
            md += [nivel + " " + inline(ch), ""]
        elif name == "p":
            md.append("*" + inline(ch) + "*" if "pie-tabla" in clases else inline(ch))
            md.append("")
        elif name == "table":
            md += [tabla(ch), ""]
        elif name == "figure":
            img = ch.find("img")
            cap = ch.find("figcaption")
            if img:
                ruta = img.get("src", "")
                if ruta.startswith("outputs/"):
                    ruta = "../" + ruta
                etiqueta = "figura"
                if cap:
                    coincidencia = re.match(r"(Figura\s+\d+)", inline(cap))
                    if coincidencia:
                        etiqueta = coincidencia.group(1)
                md += [f"![{etiqueta}]({ruta})", ""]
            if cap:
                md += ["*" + inline(cap) + "*", ""]
        elif name == "div":
            md += [div(ch), ""]
        elif name == "ul":
            md += ["- " + inline(li) for li in ch.find_all("li", recursive=False)]
            md.append("")
        else:
            texto = inline(ch)
            if texto:
                md += [texto, ""]
    texto = "\n".join(md).strip() + "\n"
    texto = re.sub(
        r"El código completo está en\s+`codigo/banco_pruebas\.py`; los tests, en\s+`_herramientas/tests`\.",
        "El código completo está en `codigo/banco_pruebas.py`; los tests internos se ejecutaron antes de empaquetar y no forman parte del zip.",
        texto,
    )
    texto = texto.replace(
        "El verificador\n`_herramientas/verificar_cifras.py` comprueba",
        "El verificador interno (no incluido en el zip) comprueba",
    )
    texto = texto.replace(
        "El verificador `_herramientas/verificar_cifras.py` comprueba",
        "El verificador interno (no incluido en el zip) comprueba",
    )
    texto = texto.replace(
        "```\n_trabajo/venv/bin/python -m pytest _herramientas/tests -q\n"
        "_trabajo/venv/bin/python _herramientas/barridos_auxiliares.py\n"
        "_trabajo/venv/bin/python _herramientas/generar_memoria.py\n"
        "_trabajo/venv/bin/python _herramientas/verificar_cifras.py --estricto\n```",
        "```\npython codigo/banco_pruebas.py\n```",
    )
    texto = texto.replace("│   ├─ informe.pdf\n", "│   ├─ informe.md\n│   ├─ informe.pdf\n")
    texto = (
        "> Documento fuente en Markdown. El PDF se genera aparte; este archivo no lo sustituye si la entrega exige PDF.\n\n"
        + texto
    )
    return texto


def main() -> None:
    SALIDA.write_text(normalizar_notion(convertir()), encoding="utf-8")
    print(SALIDA)


if __name__ == "__main__":
    main()
