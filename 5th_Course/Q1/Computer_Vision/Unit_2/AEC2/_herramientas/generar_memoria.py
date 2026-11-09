from __future__ import annotations

import html
from pathlib import Path

import pandas as pd
from weasyprint import HTML

RAIZ = Path(__file__).resolve().parents[1]
ENT = RAIZ / "U2_Practica_Hernandez_Ismael"
OUT = ENT / "outputs"
FIG = OUT / "figuras"
MEM = ENT / "memoria"
FUENTE = RAIZ / "_trabajo" / "memoria_fuente"

CSS = """
@page {
  size: A4;
  margin: 20mm 18mm 18mm 18mm;
  @bottom-center {
    content: "Medir el filtrado y la repetibilidad · Ismael Hernández · " counter(page);
    font-size: 8pt;
    color: #666;
  }
}
@page :first { @bottom-center { content: ""; } }
body { font-family: "DejaVu Serif", Georgia, serif; font-size: 10.2pt; line-height: 1.42; color: #1d1d1d; }
h1, h2, h3 { font-family: "DejaVu Sans", Arial, sans-serif; color: #123c5a; }
h1 { font-size: 25pt; line-height: 1.12; margin: 0 0 4mm 0; }
h2 { font-size: 16pt; margin: 0 0 4mm 0; padding-bottom: 1.5mm; border-bottom: 1.2pt solid #123c5a; }
h3 { font-size: 12pt; margin: 6mm 0 2mm 0; }
h4 { font-size: 10.5pt; margin: 4mm 0 1.5mm 0; color: #123c5a; }
p { margin: 0 0 2.6mm 0; text-align: justify; }
ul, ol { margin: 0 0 3mm 5mm; padding-left: 4mm; }
li { margin-bottom: 1.2mm; }
.portada { height: 245mm; display: flex; flex-direction: column; justify-content: center; }
.portada .kicker { font-family: "DejaVu Sans", Arial, sans-serif; font-size: 10pt; letter-spacing: 1.8pt; color: #a33a2b; text-transform: uppercase; }
.portada .sub { font-family: "DejaVu Sans", Arial, sans-serif; font-size: 13pt; color: #333; margin: 4mm 0 18mm 0; }
.portada .autor { font-family: "DejaVu Sans", Arial, sans-serif; font-size: 12pt; }
.portada .fecha { color: #666; font-size: 10pt; margin-top: 2mm; }
.portada .linea { width: 42mm; height: 1.5mm; background: #a33a2b; margin: 6mm 0 12mm 0; }
.resumen { background: #f4f1ea; border-left: 4pt solid #a33a2b; padding: 4mm 5mm; margin: 10mm 0 0 0; font-size: 10pt; }
.indice { margin-top: 8mm; }
.indice table { width: 100%; border: none; font-size: 10.5pt; }
.indice td { border: none; padding: 1.8mm 0; }
.indice .num { width: 12mm; color: #a33a2b; font-weight: bold; }
.ejercicio { page-break-before: auto; page-break-after: avoid; margin-top: 7mm; }
figure { margin: 4mm 0 5mm 0; page-break-inside: avoid; text-align: center; }
figure img { max-width: 100%; max-height: 178mm; }
figcaption { font-size: 8.8pt; color: #444; margin-top: 2mm; text-align: justify; }
.figs2 { display: flex; gap: 4mm; align-items: flex-start; }
.figs2 figure { flex: 1; }
table.tabla { width: 100%; border-collapse: collapse; margin: 3mm 0 4mm 0; font-family: "DejaVu Sans", Arial, sans-serif; font-size: 8.1pt; page-break-inside: auto; }
table.tabla th { background: #123c5a; color: white; padding: 1.5mm 1.2mm; text-align: left; vertical-align: bottom; font-weight: bold; }
table.tabla td { border-bottom: 0.35pt solid #c9c9c9; padding: 1.2mm 1.2mm; vertical-align: top; }
table.tabla tr:nth-child(even) td { background: #f5f7f8; }
table.tabla tr { page-break-inside: avoid; }
table.tabla td.num, table.tabla th.num { text-align: right; white-space: nowrap; }
.pie-tabla { font-size: 8.6pt; color: #444; margin: -2mm 0 4mm 0; }
.caja { background: #f4f1ea; border: 0.6pt solid #d8d1c4; padding: 3.5mm 4.5mm; margin: 4mm 0; page-break-inside: avoid; }
.caja h3 { margin-top: 0; }
.codigo { font-family: "DejaVu Sans Mono", monospace; font-size: 8.2pt; background: #f7f7f7; border-left: 2pt solid #999; padding: 2.5mm 3mm; white-space: pre-wrap; }
.nota { font-size: 9pt; color: #555; }
.hallazgo { border-left: 3pt solid #a33a2b; padding: 1mm 0 1mm 4mm; margin: 4mm 0; page-break-inside: avoid; }
.hallazgo .fuente { font-size: 8.5pt; color: #555; }
.salto { page-break-before: always; }
"""


def fmt(valor, decimales=3):
    if pd.isna(valor):
        return "—"
    if isinstance(valor, str):
        return valor
    if isinstance(valor, bool):
        return "sí" if valor else "no"
    try:
        numero = float(valor)
    except (TypeError, ValueError):
        return str(valor)
    if numero.is_integer() and decimales == 0:
        return str(int(numero))
    texto = f"{numero:.{decimales}f}"
    return texto.replace(".", ",")


def tabla(df, columnas, cabeceras, decimales=None, clases_num=None):
    decimales = decimales or {}
    clases_num = set(clases_num or [])
    filas = []
    for _, fila in df.iterrows():
        celdas = []
        for col in columnas:
            valor = fila[col]
            texto = fmt(valor, decimales.get(col, 3))
            clase = ' class="num"' if col in clases_num else ""
            celdas.append(f"<td{clase}>{html.escape(str(texto))}</td>")
        filas.append("<tr>" + "".join(celdas) + "</tr>")
    cabecera = "".join(f"<th>{html.escape(c)}</th>" for c in cabeceras)
    return (
        '<table class="tabla"><thead><tr>'
        + cabecera
        + "</tr></thead><tbody>"
        + "".join(filas)
        + "</tbody></table>"
    )


def figura(nombre, pie, clase=""):
    ruta = FIG / nombre
    return (
        f'<figure class="{clase}"><img src="outputs/figuras/{nombre}" alt="{html.escape(nombre)}">'
        f"<figcaption>{pie}</figcaption></figure>"
    )


def pivote_repetibilidad():
    df = pd.read_csv(OUT / "repetibilidad.csv")
    claves = [
        ("rotacion", 0.0, "rot0"),
        ("rotacion", 45.0, "rot45"),
        ("rotacion", 90.0, "rot90"),
        ("escala", 0.5, "esc0.5"),
        ("escala", 1.0, "esc1"),
        ("escala", 2.0, "esc2"),
        ("iluminacion", 0.6, "gam0.6"),
        ("iluminacion", 1.7, "gam1.7"),
    ]
    filas = []
    for (imagen, detector), grupo in df.groupby(["imagen", "detector"], sort=False):
        fila = {"imagen": imagen, "detector": detector}
        for transformacion, valor, etiqueta in claves:
            sub = grupo[(grupo["transformacion"] == transformacion) & (grupo["valor"] == valor)]
            fila[etiqueta] = float(sub["repetibilidad"].iloc[0]) if len(sub) else float("nan")
        filas.append(fila)
    return pd.DataFrame(filas)


def perfiles_img01():
    p = pd.read_csv(OUT / "perfiles_frecuencia.csv")
    orden = ["caja_3", "caja_5", "caja_9", "gaussiano_0.8", "gaussiano_1.6", "gaussiano_3.0"]
    filas = []
    for caso in orden:
        img = p[(p["imagen"] == "IMG_01.jpg") & (p["caso"] == caso) & (p["fuente"] == "imagen_filtrada")].iloc[0]
        res = p[(p["imagen"] == "IMG_01.jpg") & (p["caso"] == caso) & (p["fuente"] == "respuesta_filtro")].iloc[0]
        filas.append(
            {
                "caso": caso,
                "parametros": img["parametros"],
                "f_imagen": img["f_corte"],
                "rebotes_imagen": img["rebotes"],
                "f_respuesta": res["f_corte"],
                "rebotes_respuesta": res["rebotes"],
                "ssim": img["ssim_vs_original"],
            }
        )
    return pd.DataFrame(filas)


def real_img03():
    a = pd.read_csv(OUT / "analisis_ruido_real.csv")
    sub = a[(a["imagen"] == "IMG_03.jpg") & (a["tipo_ruido"] == "gaussiano") & (a["nivel"] == 20.0)]
    return sub[
        [
            "filtro",
            "parametros",
            "sigma_laplaciano_entrada",
            "sigma_laplaciano_salida",
            "reduccion_sigma",
            "mad_cambio",
            "brillo_medio",
        ]
    ]


def main():
    MEM.mkdir(parents=True, exist_ok=True)
    FUENTE.mkdir(parents=True, exist_ok=True)

    e1w = pd.read_csv(OUT / "tabla_e1_ganadores.csv")
    e1mv = pd.read_csv(OUT / "tabla_e1_medianas_vs_medias.csv")
    e1bil = pd.read_csv(OUT / "tabla_e1_bilateral.csv")
    ruido = pd.read_csv(OUT / "ruido_fraccion_real.csv")
    real = real_img03()
    perfiles = perfiles_img01()
    parejas_resp = pd.read_csv(OUT / "parejas_caja_gaussiano_respuesta.csv")
    canny = pd.read_csv(OUT / "barrido_canny.csv")
    estab = pd.read_csv(OUT / "estabilidad_canny.csv")
    transf = pd.read_csv(OUT / "transferencia_canny.csv")
    rep = pivote_repetibilidad()
    medio = pd.read_csv(OUT / "repetibilidad_control_medio_pixel.csv")
    reg = pd.read_csv(OUT / "registro_parametros.csv")

    e1_sel = reg[reg["parametro"].isin(
        [
            "truncada_k",
            "truncada_alpha",
            "bilateral_A_d",
            "bilateral_A_sigma_color",
            "bilateral_A_sigma_space",
            "bilateral_B_d",
            "bilateral_B_sigma_color",
            "bilateral_B_sigma_space",
        ]
    )]

    img02 = ruido[ruido["imagen"] == "IMG_02.jpg"]
    img03 = ruido[ruido["imagen"] == "IMG_03.jpg"]

    tabla_e1w = tabla(
        e1w,
        ["imagen", "tipo_ruido", "nivel", "metrica", "filtro", "parametros", "valor", "tiempo_ms"],
        ["Imagen", "Ruido", "Nivel", "Métrica", "Filtro", "Parámetros", "Valor", "Tiempo (ms)"],
        decimales={"nivel": 2, "valor": 3, "tiempo_ms": 3},
        clases_num={"nivel", "valor", "tiempo_ms"},
    )
    tabla_e1mv = tabla(
        e1mv[["imagen", "tipo_ruido", "nivel", "k", "delta_psnr", "delta_ssim"]],
        ["imagen", "tipo_ruido", "nivel", "k", "delta_psnr", "delta_ssim"],
        ["Imagen", "Ruido", "Nivel", "k", "ΔPSNR", "ΔSSIM"],
        decimales={"nivel": 2, "k": 0, "delta_psnr": 3, "delta_ssim": 3},
        clases_num={"nivel", "k", "delta_psnr", "delta_ssim"},
    )
    tabla_e1b = tabla(
        e1bil,
        ["imagen", "tipo_ruido", "nivel", "bilateral", "delta_ssim", "delta_psnr", "razon_tiempo"],
        ["Imagen", "Ruido", "Nivel", "Bilateral", "ΔSSIM", "ΔPSNR", "Tiempo relativo"],
        decimales={"nivel": 2, "delta_ssim": 3, "delta_psnr": 3, "razon_tiempo": 3},
        clases_num={"nivel", "delta_ssim", "delta_psnr", "razon_tiempo"},
    )
    tabla_sel = tabla(
        e1_sel,
        ["parametro", "valor", "criterio"],
        ["Parámetro", "Valor", "Criterio"],
        decimales={"valor": 3},
        clases_num={"valor"},
    )
    tabla_ruido02 = tabla(
        img02,
        ["tipo_ruido", "nivel", "fraccion_alterada", "sigma_empirico", "fraccion_recortada"],
        ["Ruido", "Nivel", "Fracción alterada", "σ empírico", "Fracción recortada"],
        decimales={"nivel": 2, "fraccion_alterada": 3, "sigma_empirico": 3, "fraccion_recortada": 3},
        clases_num={"nivel", "fraccion_alterada", "sigma_empirico", "fraccion_recortada"},
    )
    tabla_ruido03 = tabla(
        img03,
        ["tipo_ruido", "nivel", "fraccion_alterada", "sigma_empirico", "fraccion_recortada"],
        ["Ruido", "Nivel", "Fracción alterada", "σ empírico", "Fracción recortada"],
        decimales={"nivel": 2, "fraccion_alterada": 3, "sigma_empirico": 3, "fraccion_recortada": 3},
        clases_num={"nivel", "fraccion_alterada", "sigma_empirico", "fraccion_recortada"},
    )
    tabla_real = tabla(
        real,
        ["filtro", "parametros", "sigma_laplaciano_entrada", "sigma_laplaciano_salida", "reduccion_sigma", "mad_cambio", "brillo_medio"],
        ["Filtro", "Parámetros", "σ entrada", "σ salida", "Reducción", "MAD cambio", "Brillo salida"],
        decimales={c: 3 for c in ["sigma_laplaciano_entrada", "sigma_laplaciano_salida", "reduccion_sigma", "mad_cambio", "brillo_medio"]},
        clases_num={"sigma_laplaciano_entrada", "sigma_laplaciano_salida", "reduccion_sigma", "mad_cambio", "brillo_medio"},
    )
    tabla_perf = tabla(
        perfiles,
        ["caso", "parametros", "f_imagen", "rebotes_imagen", "f_respuesta", "rebotes_respuesta", "ssim"],
        ["Caso", "Parámetros", "Corte imagen", "Rebotes imagen", "Corte respuesta", "Rebotes respuesta", "SSIM"],
        decimales={"f_imagen": 6, "f_respuesta": 6, "ssim": 3},
        clases_num={"f_imagen", "rebotes_imagen", "f_respuesta", "rebotes_respuesta", "ssim"},
    )
    tabla_parejas = tabla(
        parejas_resp,
        ["imagen", "caja", "gaussiano", "f_corte_caja", "f_corte_gaussiano", "delta_ssim"],
        ["Imagen", "Caja", "Gaussiano", "Corte caja", "Corte gauss", "ΔSSIM"],
        decimales={"f_corte_caja": 6, "f_corte_gaussiano": 6, "delta_ssim": 3},
        clases_num={"f_corte_caja", "f_corte_gaussiano", "delta_ssim"},
    )
    tabla_canny = tabla(
        canny,
        ["percentil_alto", "fraccion_baja", "umbral_alto", "umbral_bajo", "precision", "recall", "f1", "px_borde"],
        ["Percentil", "Fracción", "Alto", "Bajo", "Precisión", "Exhaustividad", "F1", "Píxeles"],
        decimales={"percentil_alto": 0, "fraccion_baja": 2, "umbral_alto": 0, "umbral_bajo": 0, "precision": 4, "recall": 4, "f1": 4, "px_borde": 0},
        clases_num={"percentil_alto", "fraccion_baja", "umbral_alto", "umbral_bajo", "precision", "recall", "f1", "px_borde"},
    )
    tabla_estab = tabla(
        estab,
        ["realizacion", "regla", "precision", "recall", "f1", "umbral_alto", "umbral_bajo", "px_borde"],
        ["Realización", "Regla", "Precisión", "Exhaustividad", "F1", "Alto", "Bajo", "Píxeles"],
        decimales={"realizacion": 0, "precision": 4, "recall": 4, "f1": 4, "umbral_alto": 0, "umbral_bajo": 0, "px_borde": 0},
        clases_num={"realizacion", "precision", "recall", "f1", "umbral_alto", "umbral_bajo", "px_borde"},
    )
    tabla_transf = tabla(
        transf,
        ["imagen", "regla", "umbral_alto", "umbral_bajo", "px_borde", "frac_borde"],
        ["Imagen", "Regla", "Alto", "Bajo", "Píxeles", "Fracción"],
        decimales={"umbral_alto": 0, "umbral_bajo": 0, "px_borde": 0, "frac_borde": 6},
        clases_num={"umbral_alto", "umbral_bajo", "px_borde", "frac_borde"},
    )
    tabla_rep = tabla(
        rep,
        ["imagen", "detector", "rot0", "rot45", "rot90", "esc0.5", "esc1", "esc2", "gam0.6", "gam1.7"],
        ["Imagen", "Detector", "0°", "45°", "90°", "Esc. 0,5", "Esc. 1", "Esc. 2", "γ=0,6", "γ=1,7"],
        decimales={c: 3 for c in ["rot0", "rot45", "rot90", "esc0.5", "esc1", "esc2", "gam0.6", "gam1.7"]},
        clases_num={"rot0", "rot45", "rot90", "esc0.5", "esc1", "esc2", "gam0.6", "gam1.7"},
    )
    tabla_medio = tabla(
        medio,
        ["imagen", "detector", "centro", "repetibilidad", "n_orig", "n_trans", "n_validos"],
        ["Imagen", "Detector", "Centro", "Repetibilidad", "Original", "Transformada", "Válidos"],
        decimales={"repetibilidad": 3, "n_orig": 0, "n_trans": 0, "n_validos": 0},
        clases_num={"repetibilidad", "n_orig", "n_trans", "n_validos"},
    )
    tabla_reg = tabla(
        reg,
        ["parametro", "valor", "criterio", "barrido"],
        ["Parámetro", "Valor", "Criterio", "Barrido"],
        decimales={"valor": 6},
        clases_num={"valor"},
    )

    html_doc = f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8"><title>Medir el filtrado y la repetibilidad</title>
<style>{CSS}</style></head><body>

<section class="portada">
  <div class="kicker">Visión por Computador · Unidad 2 · Práctica individual</div>
  <h1>Medir el filtrado y la repetibilidad de los detectores</h1>
  <div class="linea"></div>
  <div class="sub">Del barrido con criterio declarado a la cifra que se puede defender</div>
  <div class="autor">Ismael Hernández</div>
  <div class="fecha">Grado en Ingeniería Informática · U-tad · 8 de noviembre de 2026</div>
  <div class="resumen">
    <strong>Resumen.</strong> He montado un banco de pruebas con tres fotografías y una escena sintética.
    En el primer ejercicio comparo diez filtros en seis condiciones de ruido; en el segundo enseño que el
    corte de la imagen filtrada no sirve para emparejar filtros y que hay que mirar la respuesta; en el
    tercero cuantifico lo que se pierde al usar la regla de percentiles de Canny; en el cuarto mido la
    repetibilidad de FAST, ORB y SIFT con rotación, escala e iluminación. Todas las cifras están en los CSV
    de <span class="codigo">outputs/</span> y salen de una semilla fija y de criterios que sellé antes de medir.
  </div>
</section>

<section class="indice">
  <h2>Contenido</h2>
  <table>
    <tr><td class="num">1</td><td>Método, materiales y decisiones</td></tr>
    <tr><td class="num">2</td><td>Ejercicio 1: rejilla de denoising</td></tr>
    <tr><td class="num">3</td><td>Ejercicio 2: lectura cuantitativa del espectro</td></tr>
    <tr><td class="num">4</td><td>Ejercicio 3: Canny con umbrales por evidencia</td></tr>
    <tr><td class="num">5</td><td>Ejercicio 4: repetibilidad de keypoints</td></tr>
    <tr><td class="num">6</td><td>Hallazgos y límites</td></tr>
    <tr><td class="num">7</td><td>Reproducibilidad y cierre</td></tr>
    <tr><td class="num">A</td><td>Anexo: registro de parámetros y tablas de apoyo</td></tr>
  </table>
</section>

<h2 class="ejercicio">1. Método, materiales y decisiones</h2>
<p>Empecé por la parte menos visible del trabajo: dejar el material quieto y escribir qué iba a medir antes de tocar nada. No
quería elegir un filtro porque la figura resultara atractiva y luego buscarle una justificación. Por eso sellé
<span class="codigo">criterios_declarados.md</span> y <span class="codigo">predicciones.md</span> con un hash
criptográfico antes de generar los resultados. Si algún parámetro cambia, el registro y el hash lo delatan.</p>

<h3>1.1 Imágenes y versiones de trabajo</h3>
<p>He usado tres fotografías de Wikimedia Commons. Cada una cubre un problema distinto y ninguna está
retocada: los originales viven en <span class="codigo">data/</span> y el código comprueba su hash al arrancar.
La tabla de créditos sigue el formato que usé en mi memoria de la AEC1 de la Unidad 1; me parece más claro
tener autor, licencia y ficha a la vista que esconderlos en un JSON.</p>
<table class="tabla"><caption>Créditos de las imágenes. Las fichas enlazan a Wikimedia Commons, donde está la licencia completa.</caption>
<thead><tr><th>Imagen</th><th>Papel</th><th>Autor</th><th>Licencia</th><th>Ficha</th></tr></thead>
<tbody>
<tr><td>IMG_01.jpg</td><td>Follaje con textura fina</td><td>A S M Jobaer</td><td>CC BY-SA 4.0</td><td><a href="https://commons.wikimedia.org/wiki/File:Close_up_of_dense_green_foliage_hedge.jpg">Wikimedia Commons</a></td></tr>
<tr><td>IMG_02.jpg</td><td>Manzana sobre fondo blanco saturado</td><td>Karl Thomas Moore (Karlfonza)</td><td>CC BY-SA 4.0</td><td><a href="https://commons.wikimedia.org/wiki/File:Apple_With_White_Background.jpg">Wikimedia Commons</a></td></tr>
<tr><td>IMG_03.jpg</td><td>Ruido real en baja luz</td><td>Rodrigo.Argenton</td><td>CC BY-SA 4.0</td><td><a href="https://commons.wikimedia.org/wiki/File:Image_noise_in_low_light_sample_(Canon_100D)_at_ISO_6400.jpg">Wikimedia Commons</a></td></tr>
</tbody></table>
<p>IMG_01 es la textura: hojas, ramas y detalle fino. La uso como referencia limpia en el primer ejercicio y
como imagen texturada en los demás. IMG_02 es la manzana; tiene regiones amplias y un fondo blanco que ya
está saturado, así que el ruido gaussiano se recorta y eso se nota en las cifras. IMG_03 es una foto con
ruido real de sensor; no tengo una versión limpia, de modo que no la uso como <em>ground truth</em>: en
denoising la analizo sin PSNR ni SSIM y en el resto la describo.</p>
<p>Las paso a gris y las reduzco a un lado mayor de 512 px con <span class="codigo">INTER_AREA</span>. Los
originales no se tocan. En el cuarto ejercicio recorto un cuadrado central para que rotación y escala tengan
el mismo encuadre; sin ese recorte, el warp y el recorte de keypoints se mezclan y la comparación deja de ser
limpia.</p>

<h3>1.2 Semillas, repeticiones y métricas</h3>
<p>La semilla principal es <span class="codigo">20260101</span> y la auxiliar de los barridos es
<span class="codigo">20260102</span>. Cada celda de ruido tiene su propia secuencia,
<span class="codigo">SeedSequence([semilla, idx_imagen, idx_condicion])</span>, para que añadir una imagen no
me cambie el ruido de las anteriores. Los tiempos son la mediana de varias repeticiones y descarto la primera
llamada; en el cuarto ejercicio no hay ruido que repetir porque los detectores son deterministas.</p>
<p>Mido PSNR y SSIM contra la referencia; perfil radial normalizado, frecuencia de corte y rebotes; precisión,
exhaustividad y F1 con tolerancia de 2 px; y repetibilidad proyectando keypoints y recortando los que se salen
del encuadre. La línea base de azar del cuarto ejercicio es
<span class="codigo">1-(1-π·tol²/lado²)^n_trans</span>. Es una aproximación de puntos uniformes y la trato como
eso, no como una verdad exacta.</p>

<h3>1.3 Decisiones que hubo que cerrar antes de medir</h3>
<p>El enunciado habla de nueve filtros, pero al contar la media 5×5 salen diez; implementé los diez. La
«mediana truncada» no es una función estándar de OpenCV y me obligó a tomar una decisión: la resolví como media recortada con
máscara, dejé una versión literal de mediana como control y comparé las dos. La elegida fue la media recortada
con <span class="codigo">k=7</span> y <span class="codigo">alpha=0,2</span>.</p>
<p>En el segundo ejercicio el enunciado pide cinco casos y luego enumera siete filtros. Medí los siete y
conservé el original como referencia. La rotación la definí con centro de píxeles y el control de medio píxel
lo reporto aparte; en las transformaciones uso <span class="codigo">BORDER_CONSTANT</span> y en los filtros
espaciales, <span class="codigo">REFLECT_101</span>. El emparejamiento caja-gaussiano lo hago por el corte de
la respuesta, no por el de la imagen filtrada; el criterio literal queda como control porque su degeneración
es justo una de las cosas que quiero enseñar.</p>
<div class="caja">
  <h3>Qué se puede auditar</h3>
  <p>Los cuatro CSV obligatorios, los barridos auxiliares, el registro de parámetros y las figuras están en
  <span class="codigo">outputs/</span>. El código completo está en
  <span class="codigo">codigo/banco_pruebas.py</span>; los tests, en
  <span class="codigo">_herramientas/tests</span>. El registro conserva el criterio y el barrido del que sale
  cada valor. No hay ninguna cifra escrita a mano en las tablas.</p>
</div>

<h2 class="ejercicio">2. Ejercicio 1: rejilla de denoising</h2>
<p>La rejilla tiene diez filtros, tres imágenes y seis condiciones: sal y pimienta al 5 %, 10 % y 30 %, y
gaussiano con σ de 10, 20 y 40. Son 180 celdas con PSNR, SSIM y tiempo. La genero con semilla fija y compruebo
que hay 60 filas por imagen, 10 por condición y las columnas exactas. Si el CSV se desvía de eso, el
<code>assert</code> me para antes de mirar los resultados.</p>

<h3>2.1 Parámetros elegidos por barrido</h3>
<p>La mediana truncada y los dos bilaterales salieron de barridos auxiliares, no de la rejilla final. La
truncada maximiza el SSIM medio en las tres imágenes con ruido gaussiano; los bilaterales los separé por SSIM
y por PSNR para que no fueran la misma configuración con otro nombre. Aquí apareció un problema: al principio el
bilateral usaba índices que se desplazaban después de un <span class="codigo">reset_index</span> y comparaba
filas que no eran. Lo corregí y repetí el barrido; las cifras que quedan son las de después.</p>
{tabla_sel}
<p class="pie-tabla">Tabla 1. Parámetros del Ejercicio 1 y criterio declarado; fuente:
<span class="codigo">outputs/registro_parametros.csv</span> y los barridos auxiliares.</p>

<h3>2.2 Ganadores por condición</h3>
<p>La tabla siguiente contesta la primera pregunta: para cada imagen, tipo de ruido y nivel, qué filtro gana
en PSNR y cuál en SSIM. Cuando no coinciden, no lo escondo: el texto de después explica qué mide cada métrica.</p>
{tabla_e1w}
<p class="pie-tabla">Tabla 2. Ganadores de PSNR y SSIM por condición; fuente:
<span class="codigo">outputs/tabla_e1_ganadores.csv</span>. El tiempo es el de la ejecución medida.</p>

<h4>Lectura de la tabla</h4>
<p>En sal y pimienta la mediana gana en las dos métricas en las condiciones con referencia. A 5 % y 10 %
suele bastar <span class="codigo">k=3</span>; al 30 % conviene <span class="codigo">k=5</span> porque hay más
impulsos y un vecindario mayor los cubre. Es el resultado más esperable: la mediana está hecha para
esto.</p>
<p>En gaussiano, PSNR y SSIM no siempre coinciden. En IMG_01 con σ=20, el mejor PSNR es el gaussiano σ=1,0
(30,002) y el mejor SSIM es el bilateral B (0,850); el bilateral conserva estructura y el gaussiano minimiza
el error cuadrático. En IMG_02 con σ=20, el mejor PSNR es la mediana 5×5 (34,732) y el mejor SSIM el gaussiano
σ=2,0 (0,962): la mediana aprovecha las regiones uniformes para el error cuadrático, pero deja una textura de
mesetas que SSIM penaliza. No es un fallo de las métricas; PSNR castiga el error medio por píxel y SSIM mira
luminancia, contraste y estructura local.</p>

{figura('e1_heatmap_psnr.png', 'Figura 1. PSNR de los diez filtros en las seis condiciones. Las filas son filtros y las columnas, condiciones; la barra de color es común y va de 10 a 45 dB. Fuente: <span class="codigo">outputs/resultados_denoising.csv</span>.')}
{figura('e1_heatmap_ssim.png', 'Figura 2. SSIM de los diez filtros en las seis condiciones, con la misma organización que la figura anterior y escala común de 0 a 1. La comparación directa entre PSNR y SSIM muestra las condiciones en las que el ganador cambia.')}

<h3>2.3 Mediana frente a media en ruido impulsivo</h3>
<p>Quería comprobar que la ventaja de la mediana sobre la media no era un efecto de un solo nivel. En IMG_01
el ΔPSNR es 9,409, 10,948 y 9,368 al 5 %, 10 % y 30 %; el ΔSSIM sube de 0,282 a 0,442. En IMG_02 el ΔPSNR es
20,550, 18,799 y 22,953, y el ΔSSIM pasa de 0,501 a 0,661. La ventaja no desaparece; en SSIM crece con el
porcentaje, porque la media reparte cada impulso entre todo el vecindario y la mediana lo descarta.</p>
{tabla_e1mv}
<p class="pie-tabla">Tabla 3. Diferencia mediana − media para k=3 y k=5; fuente:
<span class="codigo">outputs/tabla_e1_medianas_vs_medias.csv</span>. Un Δ positivo favorece a la mediana.</p>
<p>El tamaño óptimo cambia con el nivel: a 5 % y 10 % la mediana 3×3 conserva más detalle; al 30 % la 5×5
cubre más impulsos. En IMG_02, con fondo blanco saturado, la mediana 5×5 es la que mejor PSNR obtiene al 10 % y
al 30 %; el SSIM prefiere k=3 al 10 %, señal de que el vecindario grande empieza a alisar.</p>

<h3>2.4 La mediana sobre ruido gaussiano</h3>
<p>En gaussiano la mediana deja de ser la mejor opción en SSIM. En IMG_01 con σ=40 la mediana 5×5 obtiene
PSNR 25,643 y SSIM 0,654, mientras que la media 5×5 obtiene 26,017 y 0,712; el gaussiano σ=2,0 sube a 0,746
de SSIM. En IMG_02 la mediana 5×5 sí gana PSNR (34,732 frente a 30,055 de la media en σ=20), pero pierde SSIM
(0,878 frente a 0,930 de la media y 0,962 del gaussiano σ=2,0). La explicación más consistente es que el ruido
gaussiano no es disperso: no hay impulsos aislados que eliminar, sino una perturbación en todos los píxeles.
La mediana selecciona un orden estadístico y descarta información; con ruido denso produce mesetas y no reduce
el error de forma tan eficiente como un promedio o un gaussiano. Su ventaja en PSNR sobre fondos uniformes no
implica mejor estructura local.</p>

<h3>2.5 Bilateral frente a gaussiano: coste y compensación</h3>
<p>Comparé el bilateral B con el gaussiano σ=2,0, que es el suavizado comparable de la rejilla. En IMG_01
con σ=20, el bilateral B gana 0,039 de SSIM (0,850 frente a 0,811) pero tarda 8,171 ms frente a 0,441 ms. En
σ=40 la ventaja se invierte: 0,612 frente a 0,746 de SSIM, con 7,358 ms frente a 0,264 ms. En IMG_02 el
bilateral B pierde SSIM en σ=20 (−0,021) y en σ=40 (−0,147). La conclusión es que el bilateral conserva mejor
los bordes en el régimen moderado de IMG_01, pero el coste no se compensa cuando el ruido es alto y, en una
imagen con regiones amplias, el gaussiano ofrece mejor SSIM.</p>
{tabla_e1b}
<p class="pie-tabla">Tabla 4. Bilateral frente al gaussiano comparable: diferencias de SSIM/PSNR y tiempo
relativo; fuente: <span class="codigo">outputs/tabla_e1_bilateral.csv</span>. El tiempo relativo es el cociente
medido, no una estimación.</p>

<h3>2.6 Caso visual y ruido real</h3>
<p>En los casos con referencia no encuentro un ganador métrico claramente peor que la elección visual: en
IMG_01 con sal al 30 %, la mediana 5×5 gana PSNR y SSIM y también es la opción visual razonable; la truncada
alisa más y pierde detalle. En IMG_03 no hay referencia y no se puede puntuar; la mediana deja grano, el
bilateral A conserva el borde del asa y el gaussiano σ=2,0 alisa en exceso. Por eso declaro que la discrepancia
observada es entre métricas (PSNR frente a SSIM), no un caso demostrado de métrica frente a la impresión visual.</p>
<p>IMG_02 es el caso problemático para el ruido gaussiano: una parte importante del fondo está saturada, de
modo que la perturbación se recorta. Con σ nominal 10, 20 y 40 el σ empírico medido es 7,091, 13,430 y 26,254,
y la fracción recortada es 0,390, 0,424 y 0,441. En sal, la fracción realmente alterada es 0,040, 0,079 y
0,213, por debajo de la nominal por impactos repetidos en los mismos píxeles. Estas cifras acompañan a la
rejilla y evitan leer el PSNR como si el ruido inyectado fuera exactamente el nominal.</p>
{tabla_ruido02}
<p class="pie-tabla">Tabla 5. Ruido efectivo en IMG_02; fuente:
<span class="codigo">outputs/ruido_fraccion_real.csv</span>. La fracción recortada solo tiene sentido en
gaussiano; los impactos repetidos explican la diferencia en sal.</p>

<p>Analizo el efecto de los filtros sobre IMG_03 sin referencia. La σ del laplaciano de entrada es 6,4245;
con gaussiano σ=20 la entrada sube a 20,509. La mediana 3×3 la reduce a 0,4942 (reducción 0,9231), la mediana
5×5 y el gaussiano σ=2,0 a 0,2471 (0,9615), y el bilateral B a 0,9884 (0,8462). El brillo medio se mantiene
alrededor de 103,0. La lectura es descriptiva: la mediana elimina grano, el bilateral conserva mejor el borde
pero deja más rugosidad; sin verdad de referencia no declaro un ganador.</p>
{tabla_real}
<p class="pie-tabla">Tabla 6. Análisis sin referencia sobre IMG_03 con gaussiano σ=20; fuente:
<span class="codigo">outputs/analisis_ruido_real.csv</span>. La entrada es la imagen ruidosa, no una referencia
limpia.</p>
{figura('e1_heatmap_rugosidad_IMG_03.png', 'Figura 3. Rugosidad (σ del laplaciano) de los filtros sobre IMG_03 sin referencia; la escala de color es común y va de 0,4942 a 6,4245. No se interpreta como PSNR.')}
{figura('e1_recortes_IMG_01.png', 'Figura 4. Recortes de IMG_01 con sal al 30 %: limpia, ruidosa, mediana 3×3, mediana 5×5, bilateral B y gaussiano σ=2,0. La mediana 5×5 gana en PSNR y SSIM; la truncada alisa más.')}
{figura('e1_recortes_IMG_03.png', 'Figura 5. Recortes de IMG_03 sin referencia: limpia, ruidosa, mediana, bilateral A, gaussiano σ=2,0 y truncada. La σ del laplaciano baja de 0,4942 (mediana 3) a 0,9884 (bilateral B); la comparación es visual y descriptiva, sin PSNR.')}

<h2 class="ejercicio">3. Ejercicio 2: lectura cuantitativa del espectro</h2>
<p>Al principio interpreté este ejercicio como una variante del anterior con otra métrica, y no lo es. Calculo el
perfil radial del espectro de la imagen filtrada y el de la respuesta del filtro. La frecuencia de corte es el
radio al que el perfil normalizado cae por debajo de 0,5; los rebotes cuentan las veces que vuelve a subir
después de haber bajado. Elegí el ε de rebotes como el menor que da cero en los tres gaussianos:
<span class="codigo">0,000236</span>.</p>

<h3>3.1 El corte de la imagen filtrada no distingue filtros</h3>
<p>En IMG_01 el corte de la imagen filtrada vale 0,002426 en los siete filtros; en IMG_02, 0,002139; en
IMG_03, 0,001714. El perfil de la imagen está dominado por la cola del espectro de la propia fotografía y el
corte cae en la zona de baja energía, así que no separa un filtro de otro. Cuando vi que salía el mismo valor
en los siete, pensé que había un error en el bucle; repetí el cálculo y volvió a salir. El corte de la
respuesta sí distingue: caja 3/5/9 = 0,213002/0,123554/0,067413; gaussiano 0,8/1,6/3,0 =
0,233092/0,116006/0,061449. Los rebotes confirman la diferencia: las cajas dan 17, 25 y 23 en IMG_01 y los
gaussianos, cero.</p>
{tabla_perf}
<p class="pie-tabla">Tabla 7. Perfiles de IMG_01: corte y rebotes de la imagen filtrada y de la respuesta;
fuente: <span class="codigo">outputs/perfiles_frecuencia.csv</span>. La columna SSIM es frente a la original.</p>
{figura('e2_perfiles_imagen.png', 'Figura 6. Perfiles radiales normalizados de la imagen filtrada. La escala es logarítmica y común; el corte se queda en 0,002426 y las curvas se separan poco, que es la degeneración que motiva usar la respuesta. ε=0,000236.')}
{figura('e2_respuesta_filtros.png', 'Figura 7. Respuesta de los filtros: caja y gaussiano con su corte y sus rebotes. Las cajas dan cortes 0,213/0,124/0,067 y rebotes; los gaussianos, 0,233/0,116/0,061 y cero rebotes.')}

<h3>3.2 Emparejamiento y SSIM</h3>
<p>El emparejamiento literal por el corte de la imagen elige siempre <span class="codigo">gaussiano_0.8</span>
para las tres cajas; el ΔSSIM es −0,012044, −0,117044 y −0,336154 en IMG_01. Es un emparejamiento degenerado:
las tres cajas tienen el mismo corte de imagen, así que la comparación no mide suavizado. Al emparejar por la
respuesta, caja 3 va con gaussiano 0,8, caja 5 con 1,6 y caja 9 con 3,0; el ΔSSIM baja a −0,012044, −0,000990
y −0,013382. En las tres imágenes el ΔSSIM es negativo: a igualdad de suavizado medido en frecuencia, el
gaussiano conserva algo mejor la estructura; la caja deja lóbulos laterales y cierto <em>ringing</em>. La
diferencia es pequeña entre caja 5 y gaussiano 1,6; no la elijo por impresión, la dejo escrita con la cifra
delante.</p>
{tabla_parejas}
<p class="pie-tabla">Tabla 8. Parejas caja-gaussiano por corte de respuesta y ΔSSIM; fuente:
<span class="codigo">outputs/parejas_caja_gaussiano_respuesta.csv</span>. El ΔSSIM se calcula como caja −
gaussiano; un valor negativo favorece al gaussiano.</p>
{figura('e2_parejas_caja_gaussiano.png', 'Figura 8. Comparación visual de las parejas por respuesta. Cada pareja iguala el corte de la respuesta, no el de la imagen; el ΔSSIM va de −0,336 con el criterio literal a −0,013 con la respuesta.')}

<h2 class="ejercicio">4. Ejercicio 3: Canny con umbrales por evidencia</h2>
<p>La escena sintética de 512×512 contiene rectángulos, círculos y segmentos con contrastes distintos. Genero
la referencia por código a partir de las primitivas, no aplicando Canny. Añado ruido gaussiano σ=15 solo a la
imagen. Elegí el suavizado previo en un barrido auxiliar: σ=1,5, el de mayor F1, dentro de la predicción
1,0–1,5. La rejilla es de 24 combinaciones: percentiles 70, 75, 80, 85, 90 y 95; fracciones 0,3, 0,4, 0,5 y
0,6.</p>

<h3>4.1 Óptimo, regla de la unidad y pérdida</h3>
<p>El mejor F1 de la rejilla es p95/f0,6: umbrales 48/28, precisión 0,999664, exhaustividad 0,996875,
F1 0,998268 y 2978 píxeles. La regla de la unidad p85/f0,5 da 20/10, precisión 0,054049, exhaustividad 1,0,
F1 0,102554 y 55 561 píxeles. La pérdida absoluta es 0,895713 y la relativa, 0,897268. La regla de la unidad
falla en esta escena: el umbral alto 20 es demasiado bajo y deja pasar el grano; el óptimo sube a 48.</p>
<div class="caja">
  <p><strong>El óptimo está en el borde de la rejilla.</strong> Con p95/f0,5 el F1 es 0,997933; con p95/f0,4,
  0,997265; con p95/f0,3, 0,989645. Las diferencias entre las filas p95 son pequeñas, pero el salto desde p90
  es grande. No amplío la rejilla porque estaba sellada: declaro que el óptimo está en el borde y que la
  conclusión es válida para esta rejilla.</p>
</div>
{tabla_canny}
<p class="pie-tabla">Tabla 9. Las 24 combinaciones del barrido de Canny; fuente:
<span class="codigo">outputs/barrido_canny.csv</span>. La tolerancia es de 2 px; el F1 se calcula sobre píxeles
de borde.</p>
{figura('e3_escena.png', 'Figura 9. Escena sintética de 512×512 con ruido σ=15, referencia de bordes generada por código y versión suavizada. La referencia no se obtiene con Canny.')}
{figura('e3_barrido_f1.png', 'Figura 10. Mapa de F1 de la rejilla: percentil alto frente a fracción baja. El óptimo p95/f0,6 (F1 0,998268) y la regla de la unidad p85/f0,5 (F1 0,102554) están marcados.')}
{figura('e3_curvas_pr.png', 'Figura 11. Curva precisión-exhaustividad recorriendo el percentil alto para f=0,5 y f=0,6. Al subir el percentil, la precisión crece y la exhaustividad apenas baja; el codo está en p95, con F1 0,998268.')}

<h3>4.2 Estabilidad y transferencia</h3>
<p>Medí la estabilidad con diez realizaciones de ruido. El F1 del óptimo va de 0,993673 a 0,999666; el de la
unidad, de 0,100110 a 0,102369. La unidad es estable, pero estable en un valor malo: el problema no es la
varianza, sino el sesgo del umbral. El óptimo también es estable, con variaciones pequeñas de los umbrales
(48/28 o 49/29).</p>
{tabla_estab}
<p class="pie-tabla">Tabla 10. Estabilidad en diez realizaciones; fuente:
<span class="codigo">outputs/estabilidad_canny.csv</span>. La regla óptima y la de la unidad se evalúan en las
mismas realizaciones.</p>
{figura('e3_estabilidad.png', 'Figura 12. Precisión, exhaustividad y F1 por regla en las diez realizaciones. La escala es común; el óptimo queda en F1 0,998020 y la unidad en 0,101176.')}

<p>No puedo puntuar la transferencia a las imágenes reales sin referencia, pero sí describirla. Las
fracciones de píxeles de borde son:</p>
{tabla_transf}
<p class="pie-tabla">Tabla 11. Transferencia de las reglas a las imágenes reales; fuente:
<span class="codigo">outputs/transferencia_canny.csv</span>. El óptimo y la unidad sintéticos usan umbrales
absolutos; las reglas locales usan percentiles de cada imagen.</p>
<p>Los umbrales absolutos no transfieren bien: en IMG_01 el óptimo 48/28 marca 0,121987 y la unidad 20/10,
0,150608; el percentil óptimo local 125/75 marca 0,050461 y el percentil unidad local 84/42, 0,095617. En
IMG_03 el óptimo absoluto se queda en 0,004623 y la unidad local 8/4 dispara a 0,112885: el grano se convierte
en borde. El percentil local se adapta mejor, pero la regla de la unidad local es el peor caso. La lección
profesional es que un umbral ajustado en una escena no se traslada sin comprobar el contenido. En esta parte
tuve que corregir un conteo: estaba usando <span class="codigo">det.sum()</span> sobre una máscara de 0/255 y
luego cambié a <span class="codigo">np.count_nonzero</span>; con la máscara dilatada la diferencia se notaba.</p>
{figura('e3_transferencia_IMG_01.png', 'Figura 13. Transferencia a IMG_01: fracciones 0,121987, 0,150608, 0,050461 y 0,095617 para el óptimo sintético, la unidad sintética y los percentiles local óptimo y local unidad. La textura hace que los umbrales absolutos marquen de más.')}
{figura('e3_transferencia_IMG_02.png', 'Figura 14. Transferencia a IMG_02: fracciones 0,008087, 0,013385, 0,004439 y 0,008168. Las regiones amplias y el fondo saturado cambian la densidad de bordes; el percentil local se adapta mejor.')}
{figura('e3_transferencia_IMG_03.png', 'Figura 15. Transferencia a IMG_03: fracciones 0,004623, 0,008308, 0,008102 y 0,112885. El ruido real hace que la unidad local 8/4 convierta el grano en bordes.')}

<h2 class="ejercicio">5. Ejercicio 4: repetibilidad de keypoints</h2>
<p>El cuarto ejercicio fue el más difícil de interpretar. Proyecto los keypoints de la imagen original con la
homografía y cuento cuántos tienen un vecino a menos de 3 px en la transformada. Solo cuento los proyectados
que siguen dentro del encuadre. La línea base de azar la calculo por densidad y la dibujo discontinua. La
rejilla principal tiene 171 filas: tres imágenes, tres detectores y diecinueve transformaciones; las tres
transformaciones son rotación, escala e iluminación.</p>

<h3>5.1 Tests y control de la homografía</h3>
<p>El warp de 90° coincide con <span class="codigo">np.rot90</span>; la identidad (escala 1,0 y gamma 1,0) da
repetibilidad 1,0; el control de medio píxel produce una imagen distinta y lo reporto. La repetibilidad a 90°
con la homografía coincide con la calculada sobre <span class="codigo">np.rot90</span>. Ejecuto los tests con
<span class="codigo">pytest</span> y pasan. Ese test me sirvió para no seguir con una duda que me habría
contaminado todas las curvas.</p>

<h3>5.2 Pregunta 1: FAST y escala</h3>
<p><strong>Refuto la invariancia a escala de FAST.</strong> En IMG_01, FAST da 0,925401 a escala 0,5,
1,000000 a 1,0 y 0,340000 a 2,0. En IMG_02: 0,641509, 1,000000 y 0,480769. En IMG_03: 0,750000, 1,000000 y
0,000000; este último no tiene keypoints transformados, así que no es una tasa comparable. La caída al
ampliar es clara; el valor a 0,5 es más alto de lo que predecía (0,3–0,6), sobre todo en IMG_01: el detector
básico conserva esquinas cuando la imagen se reduce porque el test de anillo sigue encontrando estructura,
pero no ocurre lo mismo al ampliar. La línea base de azar a 2,0 en IMG_01 es 0,052325, muy por debajo de
0,340000; la tasa sigue teniendo señal, pero no invariancia.</p>
{tabla_rep}
<p class="pie-tabla">Tabla 12. Repetibilidad en valores seleccionados de la rejilla principal; fuente:
<span class="codigo">outputs/repetibilidad.csv</span>. Los valores completos, con n_orig, n_trans, n_validos y
azar, están en el CSV.</p>
{figura('e4_escala.png', 'Figura 16. Repetibilidad frente a escala para FAST, ORB y SIFT en las tres imágenes. En IMG_01 FAST da 0,925401, 1,000000 y 0,340000; la línea discontinua es el azar y el eje y va de 0 a 1.')}

<h3>5.3 Pregunta 2: estructura de la rotación</h3>
<p>La rotación no es plana. FAST da 1,000000 a 0°, 0,807692 a 45° y 1,000000 a 90° en IMG_01; en IMG_02,
1,000000, 0,415094 y 1,000000; en IMG_03, 1,000000, 0,500000 y 1,000000. ORB y SIFT también tienen un valle
intermedio y un pico en 90°: ORB pasa de 0,905826 a 45° a 0,998257 a 90° en IMG_01; SIFT, de 0,830283 a
0,942879. El pico se explica por el anillo de 16 píxeles de FAST: su disposición tiene simetría de 90° y, al
girar 90°, la rejilla de píxeles vuelve a alinearse; a 45° el anillo no cae sobre los mismos píxeles y la
interpolación del warp desplaza las respuestas. El test proyecta y busca un vecino a 3 px, de modo que la
estructura del detector y la rejilla se ven en la curva. El pico no es perfecto en SIFT/ORB porque la
detección en la imagen girada no es exactamente la misma, aunque el warp sí lo sea.</p>
{figura('e4_rotacion.png', 'Figura 17. Repetibilidad frente a rotación. En IMG_01 FAST da 1,000000, 0,807692 y 1,000000 a 0°, 45° y 90°; el valle intermedio aparece en los tres detectores.')}

<h3>5.4 Pregunta 3: detector multiescala</h3>
<p>Con ORB y SIFT en la misma gráfica se ve la diferencia. A escala 0,5/1,0/2,0, ORB da 0,994273/1,000000/
0,418320 en IMG_01, 0,865815/1,000000/0,504983 en IMG_02 y 0,971429/1,000000/0,000000 en IMG_03. SIFT da
0,594821/1,000000/0,747881, 0,533333/1,000000/0,844444 y 0,310345/1,000000/1,000000. El 1,000000 de SIFT en
IMG_03 a 2,0 sale de un solo keypoint válido: no es evidencia de invariancia, sino de muestra pequeña. ORB
explora una pirámide y mejora a FAST al reducir; SIFT conserva mejor la ampliación en IMG_01/02. En IMG_03,
ORB no encuentra keypoints a 1,25, 1,5 y 2,0 y su tasa cae a 0; el grano y el tamaño pequeño de la estructura
explican esa muestra. La comparación es la demostración empírica de por qué existen los detectores multiescala:
FAST básico no basta, ORB ayuda en la reducción y SIFT mantiene más rango en la ampliación.</p>
{figura('e4_sens_fast.png', 'Figura 18. Sensibilidad de FAST al umbral 10/25/50 en el barrido de escala. El 25 es el principal; la curva no se elige por impresión visual después de ver el resultado.')}
{figura('e4_sens_orb.png', 'Figura 19. Sensibilidad de ORB a la pirámide (nlevels 1, 4 y 8) en escala. La pirámide mejora frente a nlevels=1; 4 y 8 quedan cerca.')}
{figura('e4_sens_tol.png', 'Figura 20. Sensibilidad a la tolerancia de FAST 1/2/3/5 en rotación y escala. La tasa crece con tol; el trazo grueso es tol=3,0, el valor principal.')}
{figura('e4_iluminacion.png', 'Figura 21. Repetibilidad frente a iluminación (gamma 0,6/0,8/1,0/1,3/1,7). La homografía es la identidad; la curva mide solo la sensibilidad al cambio de intensidad.')}

<h3>5.5 Línea base, muestras pequeñas y control de medio píxel</h3>
<p>La línea base de azar no es despreciable: en IMG_01/ORB llega a 0,633629 y la repetibilidad observada a 90°
es 0,998257; la diferencia es real, pero mucho menor que en IMG_02, donde el azar es 0,073292. En IMG_03 el
azar es casi cero porque hay pocos keypoints, pero también hay pocos puntos: FAST tiene 4, ORB 35 y SIFT 29.
Las tasas de IMG_03 son gruesas; no las uso para afirmar diferencias finas. La tabla de control de medio píxel
reporta el warp con centro de píxeles y con medio píxel: ORB baja de 0,998257 a 0,981325 en IMG_01, de 0,974441
a 0,955272 en IMG_02 y de 1,000000 a 0,971429 en IMG_03; SIFT baja de 0,942879 a 0,941356, de 0,933333 a
0,911111 y queda igual en IMG_03; FAST no cambia por la tolerancia y el número de keypoints.</p>
{tabla_medio}
<p class="pie-tabla">Tabla 13. Control de centro de píxeles frente a medio píxel a 90°; fuente:
<span class="codigo">outputs/repetibilidad_control_medio_pixel.csv</span>. El test comprueba que el warp de
medio píxel es distinto; la tasa puede coincidir si la tolerancia absorbe el desplazamiento.</p>
{figura('e4_medio_pixel.png', 'Figura 22. Repetibilidad a 90° con centro de píxeles y con medio píxel. En ORB baja de 0,998257 a 0,981325; las barras comparan los tres detectores.')}

<h2 class="ejercicio">6. Hallazgos y límites</h2>
<p>He comprobado los cinco hallazgos completos, con su fuente y su límite, y los dejo en
<span class="codigo">memoria/hallazgos.md</span>. Los resumo aquí para cerrar la lectura:</p>
<div class="hallazgo"><strong>1. La mediana 5×5 domina a la media en sal al 30 %.</strong> PSNR 29,236 frente a
19,868 y SSIM 0,896 frente a 0,454 en IMG_01; el tiempo pasa de 0,14 a 60,39 ms.<br>
<span class="fuente">Fuente: resultados_denoising.csv, índices pandas 25 y 21. Límite: IMG_01, 512 px, sal al 30 %, una
semilla.</span></div>
<div class="hallazgo"><strong>2. El bilateral B solo compensa en el régimen moderado.</strong> En IMG_01 con
σ=20 gana 0,039 de SSIM con 8,171 ms frente a 0,441 ms; con σ=40 pierde 0,134 de SSIM.<br>
<span class="fuente">Fuente: resultados_denoising.csv, índices pandas 49, 43, 59 y 53. Límite: IMG_01, ruido sintético,
dos niveles.</span></div>
<div class="hallazgo"><strong>3. El corte de la imagen filtrada no empareja filtros; el de la respuesta sí.</strong>
En IMG_01 el corte de imagen es 0,002426 en los siete filtros; el literal elige gaussiano_0,8 y llega a
ΔSSIM −0,336; la respuesta reduce el ΔSSIM a −0,013.<br>
<span class="fuente">Fuente: perfiles_frecuencia.csv y parejas_caja_gaussiano*.csv. Límite: tres imágenes,
perfil radial y ε declarado.</span></div>
<div class="hallazgo"><strong>4. La regla de la unidad de Canny falla.</strong> F1 0,102554 (p85/f0,5) frente
a 0,998268 (p95/f0,6); pérdida 0,895713 absoluta y 0,897268 relativa.<br>
<span class="fuente">Fuente: barrido_canny.csv, índices pandas 14 y 23; registro_parametros.csv. Límite: escena
sintética, σ=15, tolerancia 2 px y rejilla sellada.</span></div>
<div class="hallazgo"><strong>5. FAST básico no es invariante a escala.</strong> En IMG_01, 0,925401 a 0,5,
1,000000 a 1,0 y 0,340000 a 2,0; el azar a 2,0 es 0,052325.<br>
<span class="fuente">Fuente: repetibilidad.csv, índices pandas 7, 10 y 13. Límite: IMG_01, 512 px, tol=3; IMG_03
solo tiene 4 keypoints FAST.</span></div>

<h2 class="ejercicio">7. Reproducibilidad y cierre</h2>
<p>Dejo el cuaderno ejecutado en <span class="codigo">codigo/banco_pruebas.ipynb</span> y el script fuente en
<span class="codigo">codigo/banco_pruebas.py</span>; las versiones fijadas están en
<span class="codigo">codigo/requirements.txt</span>. No instalo nada dentro del cuaderno. Las rutas son
relativas a la carpeta de la práctica. Los tests cubren las medianas, PSNR/SSIM, la escena, la rotación de 90°,
la identidad, el medio píxel y la repetibilidad con <span class="codigo">np.rot90</span>; los ejecuto con
<span class="codigo">pytest</span>.</p>
<p>La ejecución limpia regenera los CSV y las figuras. El verificador
<span class="codigo">_herramientas/verificar_cifras.py</span> comprueba que cada número de esta memoria y de
<span class="codigo">hallazgos.md</span> aparece en algún CSV; el resultado es cero números sin respaldo. El
ruido es reproducible por la semilla y las secuencias por celda. La entrega incluye las tres imágenes
originales, los cuatro CSV obligatorios, las figuras, el registro, la memoria y el código.</p>
<p>Para el tono y la tabla de créditos me he fijado en mi memoria de la AEC1 de la Unidad 1; aquí he cambiado
los ejercicios, no la forma de contar lo que hice. Si algo no cuadra, prefiero que se vea en el texto y en los
CSV antes que esconderlo en una frase bonita.</p>
<div class="caja">
  <h3>Límites declarados</h3>
  <ul>
    <li>IMG_03 no tiene referencia limpia: sus cifras de denoising son descriptivas, no PSNR/SSIM.</li>
    <li>IMG_02 tiene saturación: el σ nominal no es el efectivo; se reporta el empírico y la fracción recortada.</li>
    <li>El óptimo de Canny está en el borde p95/f0,6 de la rejilla; no se amplía después de ver el resultado.</li>
    <li>IMG_03 tiene pocos keypoints para FAST; sus curvas de repetibilidad son gruesas y no se sobreinterpretan.</li>
    <li>La línea base de azar es una aproximación de puntos uniformes; se declara y se dibuja, no se usa como verdad exacta.</li>
  </ul>
</div>

<h2 class="ejercicio">Anexo: registro de parámetros y tablas de apoyo</h2>
<h3>A.1 Registro completo</h3>
{tabla_reg}
<p class="pie-tabla">Tabla A1. Registro de parámetros con criterio y barrido; fuente:
<span class="codigo">outputs/registro_parametros.csv</span>. Es la trazabilidad de cada valor elegido.</p>
<h3>A.2 Repetibilidad completa</h3>
<p>La rejilla principal tiene 171 filas y la de sensibilidad 294; la de control de medio píxel, 18. Los CSV
completos están en <span class="codigo">outputs/repetibilidad.csv</span>,
<span class="codigo">outputs/repetibilidad_sensibilidad.csv</span> y
<span class="codigo">outputs/repetibilidad_control_medio_pixel.csv</span>.</p>
<h3>A.3 Cómo regenerar</h3>
<div class="codigo">_trabajo/venv/bin/python -m pytest _herramientas/tests -q
_trabajo/venv/bin/python _herramientas/barridos_auxiliares.py
_trabajo/venv/bin/python _herramientas/generar_memoria.py
_trabajo/venv/bin/python _herramientas/verificar_cifras.py --estricto</div>
<p class="nota">El banco completo se ejecuta desde <span class="codigo">codigo/banco_pruebas.py</span> o desde
el cuaderno convertido; las funciones están separadas por ejercicio y comparten el núcleo.</p>

<h3>A.4 Estructura de la entrega</h3>
<div class="codigo">U2_Practica_Hernandez_Ismael.zip
├─ memoria/
│   ├─ informe.md
│   ├─ informe.pdf (opcional, si se genera)
│   └─ hallazgos.md
├─ codigo/
│   ├─ banco_pruebas.ipynb
│   ├─ banco_pruebas.py
│   └─ requirements.txt
├─ data/
│   ├─ IMG_01.jpg
│   ├─ IMG_02.jpg
│   └─ IMG_03.jpg
└─ outputs/
    ├─ resultados_denoising.csv
    ├─ perfiles_frecuencia.csv
    ├─ barrido_canny.csv
    ├─ repetibilidad.csv
    └─ figuras/</div>
<p class="nota">El paquete conserva las rutas relativas y no incluye el entorno virtual ni los archivos de
trabajo. La comprobación final se hace en un directorio temporal, comparando los CSV salvo
<span class="codigo">tiempo_ms</span>.</p>

<h3>Cierre de la entrega</h3>
<div class="nota">Cierro con tres comprobaciones: el verificador no deja ninguna cifra sin respaldo; los tests
del núcleo pasan; y la ejecución limpia reproduce los CSV y las figuras. El zip conserva las rutas
relativas y la carpeta <span class="codigo">data/</span> no se toca.</div>

</body></html>"""

    ruta_html = FUENTE / "informe.html"
    ruta_html.write_text(html_doc, encoding="utf-8")
    HTML(string=html_doc, base_url=str(ENT)).write_pdf(MEM / "informe.pdf")
    print(MEM / "informe.pdf")


if __name__ == "__main__":
    main()
