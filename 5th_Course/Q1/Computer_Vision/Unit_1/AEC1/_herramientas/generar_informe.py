from pathlib import Path
import html
import re

import pandas as pd
from weasyprint import HTML

ENT = Path("U1_Practica_Hernandez_Ismael")
OUT = ENT / "outputs"
MEM = ENT / "memoria"

diag = pd.read_csv(OUT / "diagnostico_originales.csv")
res = pd.read_csv(OUT / "resultados_u1.csv")
gan = pd.read_csv(OUT / "ganadoras_por_imagen.csv")
lote = pd.read_csv(OUT / "ganadora_lote.csv")
color = pd.read_csv(OUT / "comparacion_color.csv")
pred = pd.read_csv(OUT / "comparacion_predicciones.csv")
bayer = pd.read_csv(OUT / "bayer_fracciones.csv")
dem = pd.read_csv(OUT / "demosaico_metricas.csv")
hsv = pd.read_csv(OUT / "hsv_referencia.csv")
rob = pd.read_csv(OUT / "robustez_hsv.csv")
rres = pd.read_csv(OUT / "resumen_robustez.csv")
pre = pd.read_csv(OUT / "diagnostico_preprocesado.csv")
umb = pd.read_csv(OUT / "umbrales_contrato.csv")
aud = pd.read_csv(OUT / "resumen_auditoria.csv")

D = diag.set_index("imagen").to_dict("index")
G = gan.set_index("imagen").to_dict("index")
P = pred.set_index("imagen").to_dict("index")
C = color.set_index("via").to_dict("index")
M = dem.set_index("metrica")["valor"].to_dict()
H = hsv.iloc[0].to_dict()
RR = rres.set_index("condicion").to_dict("index")
PRE = pre.set_index("imagen").to_dict("index")
L = lote.iloc[0].to_dict()
A = aud.iloc[0].to_dict()


def f(x, d=2):
    return f"{float(x):.{d}f}".replace(".", ",")


def f0(x):
    return f"{int(round(float(x)))}"


def pct(x, d=2):
    return f"{f(x, d)} %"


def rango(a, b):
    return f"{f0(a)} → {f0(b)}"


def fila(im, op, par):
    return res[(res["imagen"] == im) & (res["operacion"] == op) & (res["parametros"] == par)].iloc[0]


def figura(archivo, pie, clase=""):
    return (
        f'<figure class="{clase}"><img src="outputs/{archivo}" alt="">'
        f"<figcaption>{pie}</figcaption></figure>"
    )


def tabla(cabeceras, filas, pie, clase=""):
    th = "".join(f"<th>{h}</th>" for h in cabeceras)
    trs = "".join(
        "<tr>" + "".join(f"<td>{c}</td>" for c in fila_) + "</tr>" for fila_ in filas
    )
    return (
        f'<table class="{clase}"><caption>{pie}</caption>'
        f"<thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table>"
    )


def md_simple(texto):
    salida = []
    buffer = []

    def volcar():
        if buffer:
            p = " ".join(buffer)
            p = html.escape(p)
            p = p.replace("&lt;=", "≤").replace("&gt;=", "≥")
            p = re.sub(r"`([^`]+)`", r"<code>\1</code>", p)
            salida.append(f"<p>{p}</p>")
            buffer.clear()

    for linea in texto.splitlines():
        if linea.startswith("## "):
            volcar()
            salida.append(f"<h3>{html.escape(linea[3:])}</h3>")
        elif linea.startswith("# "):
            volcar()
            salida.append(f"<h2>{html.escape(linea[2:])}</h2>")
        elif not linea.strip():
            volcar()
        else:
            buffer.append(linea.strip())
    volcar()
    return "\n".join(salida)


pred_md = Path("_trabajo/predicciones.md").read_text().splitlines()
pred_body = "\n".join(pred_md[1:])
crit_md = Path("_trabajo/criterio_seleccion.md").read_text().splitlines()
crit_body = "\n".join(crit_md[1:])

# ---------------------------------------------------------------------------
# Tablas
# ---------------------------------------------------------------------------
filas_fuentes = []
for _, fila_ in diag.iterrows():
    titulo = html.escape(str(fila_["titulo"]))
    url = html.escape(str(fila_["url"]))
    filas_fuentes.append([
        f"<b>{fila_['imagen']}</b>",
        html.escape(str(fila_["rol"])),
        html.escape(str(fila_["autor"])),
        html.escape(str(fila_["licencia"])),
        f"{int(fila_['ancho'])} × {int(fila_['alto'])}",
        f"{titulo}<br><a class='url' href='{url}'>{url}</a>",
    ])
tabla_fuentes = tabla(
    ["Imagen", "Papel", "Autor", "Licencia", "Tamaño", "Título y URL"],
    filas_fuentes,
    "Tabla 1. Las cinco imágenes de partida, con su papel en la práctica, autor, licencia y origen. Las URLs llevan a la ficha de Wikimedia Commons, donde consta la licencia completa.",
    "fuentes",
)

filas_diag = []
for _, fila_ in diag.iterrows():
    filas_diag.append([
        f"<b>{fila_['imagen']}</b>",
        html.escape(str(fila_["rol"])),
        f(fila_["sat_bajo"]),
        f(fila_["sat_alto"]),
        f0(fila_["rango_p1_p99"]),
        f(fila_["entropia"]),
        f(fila_["desv_tipica"], 1),
        f(fila_["R"], 1),
        f(fila_["G"], 1),
        f(fila_["B"], 1),
    ])
tabla_diag = tabla(
    ["Imagen", "Papel", "sat_bajo (%)", "sat_alto (%)", "rango p1–p99", "entropía (bits)", "desv. típica", "R", "G", "B"],
    filas_diag,
    "Tabla 2. Diagnóstico de las cinco originales. sat_bajo y sat_alto son porcentajes de píxeles con Y ≤ 2 y Y ≥ 253. La desviación típica es poblacional (ddof=0). Las tres últimas columnas son las medias de R, G y B en RGB.",
)

filas_gan = []
for _, fila_ in gan.iterrows():
    filas_gan.append([
        f"<b>{fila_['imagen']}</b>",
        "respaldo" if fila_["regla"] == "respaldo" else "normal",
        f"{fila_['operacion']} {fila_['parametros']}",
        rango(fila_["rango_original"], fila_["rango_ganadora"]),
        f"{f(fila_['sat_bajo_original'])} → {f(fila_['sat_bajo_ganadora'])}",
        f"{f(fila_['sat_alto_original'])} → {f(fila_['sat_alto_ganadora'])}",
        f"{f(fila_['entropia_original'])} → {f(fila_['entropia_ganadora'])}",
    ])
tabla_gan = tabla(
    ["Imagen", "Regla", "Configuración ganadora", "Rango p1–p99", "sat_bajo (%)", "sat_alto (%)", "Entropía (bits)"],
    filas_gan,
    "Tabla 3. Ganadoras por imagen según el criterio declarado antes del barrido. En IMG_02 ninguna configuración cumple las dos restricciones; se aplica la regla de respaldo y se elige la que minimiza max(sat_bajo, sat_alto).",
)

filas_pred = []
for _, fila_ in pred.iterrows():
    filas_pred.append([
        f"<b>{fila_['imagen']}</b>",
        html.escape(str(fila_["prediccion"])),
        f"{fila_['operacion']} {fila_['parametros']}",
        rango(fila_["rango_original"], fila_["rango_ganadora"]),
        "sí" if bool(fila_["acierto"]) else "no",
    ])
tabla_pred = tabla(
    ["Imagen", "Predicción", "Ganadora real", "Rango original → ganadora", "¿Acierto?"],
    filas_pred,
    "Tabla 4. Comparación entre la predicción que fijé antes del barrido y la configuración que eligió el criterio. Ninguna de las cinco predicciones coincide con la ganadora.",
)

filas_color = []
for _, fila_ in color.iterrows():
    etiqueta = {
        "original": "Original",
        "he_y": "HE sobre Y",
        "he_rgb": "HE por canal RGB",
    }[fila_["via"]]
    filas_color.append([
        etiqueta,
        f(fila_["R"]),
        f(fila_["G"]),
        f(fila_["B"]),
        f(fila_["B_menos_R"]),
        f(fila_["distancia"]),
    ])
tabla_color = tabla(
    ["Vía", "R", "G", "B", "B − R", "Distancia al original"],
    filas_color,
    "Tabla 5. Medias RGB de IMG_04 antes y después de dos ecualizaciones globales: sobre Y y sobre cada canal RGB por separado. La distancia es la norma euclídea del cambio de las tres medias.",
)

filas_bayer = []
for _, fila_ in bayer.iterrows():
    filas_bayer.append([
        fila_["canal"],
        f"{int(fila_['posiciones']):,}".replace(",", "."),
        f(fila_["porcentaje"]),
    ])
tabla_bayer = tabla(
    ["Canal", "Posiciones medidas", "Porcentaje del mosaico"],
    filas_bayer,
    "Tabla 6. Fracción de posiciones de cada canal en el mosaico RGGB de IMG_03, contada sobre el array y no supuesta.",
)

filas_dem = [
    ["MAE R", f"{f(M['mae_R'])} niveles"],
    ["MAE G", f"{f(M['mae_G'])} niveles"],
    ["MAE B", f"{f(M['mae_B'])} niveles"],
    ["MAE total", f"{f(M['mae_total'])} niveles"],
    ["MAE en bordes", f"{f(M['mae_bordes'])} niveles"],
    ["MAE en el resto", f"{f(M['mae_resto'])} niveles"],
    ["Cociente bordes/resto", f(M["cociente_bordes_resto"])],
    ["Píxeles de borde", f"{f(M['porcentaje_bordes'])} %"],
    ["Umbrales de Canny", f"{f0(M['umbral_canny_bajo'])} y {f0(M['umbral_canny_alto'])}"],
    ["Dilatación de la máscara de borde", f"{f0(M['dilatacion_px'])} px"],
]
tabla_dem = tabla(
    ["Métrica", "Valor"],
    filas_dem,
    "Tabla 7. Error del demosaico bilineal sobre IMG_03. Los MAE por canal están en niveles; los MAE de bordes y resto son la suma de las diferencias absolutas de los tres canales por píxel. El cociente es adimensional.",
)

piv = rob.pivot(index="gamma", columns="condicion", values="iou")
filas_rob = []
for gamma, fila_ in piv.iterrows():
    filas_rob.append([
        f(gamma, 1),
        f(fila_["sin_normalizacion"], 4),
        f(fila_["con_normalizacion"], 4),
    ])
tabla_rob = tabla(
    ["γ", "IoU sin normalización", "IoU con CLAHE 4,0 / 4×4"],
    filas_rob,
    "Tabla 8. IoU de la máscara HSV de IMG_05 frente a la referencia congelada para los cinco valores de γ. El control sin normalización (γ=1,0) vale exactamente 1,0000; con normalización vale 0,9710 porque CLAHE cambia la imagen de referencia.",
)

filas_pre = []
for _, fila_ in pre.iterrows():
    filas_pre.append([
        f"<b>{fila_['imagen']}</b>",
        f(fila_["sat_bajo"]),
        f(fila_["sat_alto"]),
        f0(fila_["rango_p1_p99"]),
        f(fila_["B_menos_R"], 1),
        f(fila_["sat_alto_original"]),
        f0(fila_["rango_original"]),
    ])
tabla_pre = tabla(
    ["Imagen", "sat_bajo (%)", "sat_alto (%)", "rango p1–p99", "B − R", "sat_alto original (%)", "rango original"],
    filas_pre,
    "Tabla 9. El contrato aplicado a las cinco imágenes. La configuración es CLAHE con clip=4,0 y tiles de 4×4 sobre Y. IMG_02 sigue por encima de la restricción de saturación alta.",
)

# ---------------------------------------------------------------------------
# Texto
# ---------------------------------------------------------------------------
p_img = {}
p_img["IMG_01.jpg"] = (
    f"IMG_01 tiene un {pct(D['IMG_01.jpg']['sat_bajo'])} de píxeles con Y ≤ 2 y una entropía de "
    f"{f(D['IMG_01.jpg']['entropia'])} bits. El rango entre percentiles es {f0(D['IMG_01.jpg']['rango_p1_p99'])}, "
    f"pero la desviación típica se queda en {f(D['IMG_01.jpg']['desv_tipica'], 1)}: hay unas flores bien "
    f"expuestas sobre un fondo que ocupa buena parte del encuadre y está prácticamente a cero. Las medias RGB "
    f"({f(D['IMG_01.jpg']['R'], 1)} / {f(D['IMG_01.jpg']['G'], 1)} / {f(D['IMG_01.jpg']['B'], 1)}) confirman "
    f"que la escena es oscura. No hay nada quemado ({pct(D['IMG_01.jpg']['sat_alto'])} en 253 o más), así que el "
    f"problema está en las sombras."
)
p_img["IMG_02.jpg"] = (
    f"IMG_02 es la imagen sobreexpuesta: un {pct(D['IMG_02.jpg']['sat_alto'])} de píxeles en 253 o más, sobre "
    f"todo la fachada blanca y el cielo. La entropía es {f(D['IMG_02.jpg']['entropia'])} bits y el rango "
    f"{f0(D['IMG_02.jpg']['rango_p1_p99'])}, pero ese rango alto convive con un {pct(D['IMG_02.jpg']['sat_bajo'])} "
    f"de negros; la desviación típica ({f(D['IMG_02.jpg']['desv_tipica'], 1)}) está inflada por el contraste "
    f"entre el edificio y la vegetación. Las medias RGB ({f(D['IMG_02.jpg']['R'], 1)} / "
    f"{f(D['IMG_02.jpg']['G'], 1)} / {f(D['IMG_02.jpg']['B'], 1)}) muestran un tono global claro. El histograma "
    f"no está comprimido: el problema es el recorte en luces, no la falta de niveles."
)
p_img["IMG_03.jpg"] = (
    f"IMG_03 tiene una entropía de {f(D['IMG_03.jpg']['entropia'])} bits, un rango de "
    f"{f0(D['IMG_03.jpg']['rango_p1_p99'])} y una desviación de {f(D['IMG_03.jpg']['desv_tipica'], 1)}. Las "
    f"medias RGB ({f(D['IMG_03.jpg']['R'], 1)} / {f(D['IMG_03.jpg']['G'], 1)} / {f(D['IMG_03.jpg']['B'], 1)}) "
    f"delatan la luz cálida de interior. El {pct(D['IMG_03.jpg']['sat_bajo'])} de píxeles en negro y el "
    f"{pct(D['IMG_03.jpg']['sat_alto'])} en blanco indican que no hay recortes: lo que falla es la distribución, "
    f"con una ventana muy brillante y el resto de la habitación en sombra. Es el caso típico para una ecualización "
    f"local."
)
p_img["IMG_04.jpg"] = (
    f"IMG_04 es la dominante de color: las medias RGB son {f(D['IMG_04.jpg']['R'], 1)} / "
    f"{f(D['IMG_04.jpg']['G'], 1)} / {f(D['IMG_04.jpg']['B'], 1)}, con el azul {f(C['original']['B_menos_R'])} "
    f"niveles por encima del rojo. La entropía es {f(D['IMG_04.jpg']['entropia'])} bits y el rango "
    f"{f0(D['IMG_04.jpg']['rango_p1_p99'])}, así que el histograma ocupa bastante y no hay recortes "
    f"({pct(D['IMG_04.jpg']['sat_bajo'])} y {pct(D['IMG_04.jpg']['sat_alto'])}). El problema no es de "
    f"luminancia, sino de balance de blancos; un procesado sobre Y no lo va a corregir, y eso se verá en el "
    f"Ejercicio 2."
)
p_img["IMG_05.jpg"] = (
    f"IMG_05 tiene un rango de {f0(D['IMG_05.jpg']['rango_p1_p99'])}, entropía {f(D['IMG_05.jpg']['entropia'])} "
    f"bits y desviación {f(D['IMG_05.jpg']['desv_tipica'], 1)}. La manzana ocupa casi la mitad del encuadre y "
    f"el fondo gris está bien separado; solo un {pct(D['IMG_05.jpg']['sat_alto'])} de píxeles está quemado y "
    f"no hay negros ({pct(D['IMG_05.jpg']['sat_bajo'])}). Las medias RGB ({f(D['IMG_05.jpg']['R'], 1)} / "
    f"{f(D['IMG_05.jpg']['G'], 1)} / {f(D['IMG_05.jpg']['B'], 1)}) reflejan el rojo dominante del objeto. Es la "
    f"imagen con menos margen de mejora y la que usaré para la segmentación."
)

# Discrepancias
p_disc = {}
p_disc["IMG_01.jpg"] = (
    f"En IMG_01 predije gamma con g=0,6. Esa configuración deja `sat_bajo` en "
    f"{pct(fila('IMG_01.jpg', 'gamma', 'g=0.6')['sat_bajo'])} y un rango de "
    f"{f0(fila('IMG_01.jpg', 'gamma', 'g=0.6')['rango_p1_p99'])}, así que el criterio la descarta por la "
    f"primera restricción. La ganadora fue CLAHE 4,0 / 8×8, con `sat_bajo` "
    f"{pct(G['IMG_01.jpg']['sat_bajo_ganadora'])} y rango {f0(G['IMG_01.jpg']['rango_ganadora'])}. El criterio "
    f"premia subir el fondo negro, pero al mirar la figura se ve que también sube el ruido del fondo. Gamma 0,6 "
    f"era más razonable fotográficamente, aunque no cumpliera la restricción que fijé."
)
p_disc["IMG_02.jpg"] = (
    f"En IMG_02 predije gamma 2,2, o un CLAHE suave. Gamma 2,2 deja `sat_alto` en "
    f"{pct(fila('IMG_02.jpg', 'gamma', 'g=2.2')['sat_alto'])} y `sat_bajo` en "
    f"{pct(fila('IMG_02.jpg', 'gamma', 'g=2.2')['sat_bajo'])}: no cumple ninguna de las dos restricciones. "
    f"La ganadora por respaldo fue HE, con `sat_alto` {pct(G['IMG_02.jpg']['sat_alto_ganadora'])} y rango "
    f"{f0(G['IMG_02.jpg']['rango_ganadora'])}. HE baja el máximo de saturación de "
    f"{pct(D['IMG_02.jpg']['sat_alto'])} a {pct(G['IMG_02.jpg']['sat_alto_ganadora'])}, pero sigue lejísimos "
    f"del 1 %: es la mejor de las malas, no una recuperación de las luces."
)
p_disc["IMG_03.jpg"] = (
    f"En IMG_03 predije CLAHE 2,0 / 8×8. Esa configuración da un rango de "
    f"{f0(fila('IMG_03.jpg', 'clahe', 'clip=2.0;tile=8x8')['rango_p1_p99'])} con `sat_bajo` "
    f"{pct(fila('IMG_03.jpg', 'clahe', 'clip=2.0;tile=8x8')['sat_bajo'])} y `sat_alto` "
    f"{pct(fila('IMG_03.jpg', 'clahe', 'clip=2.0;tile=8x8')['sat_alto'])}. La ganadora fue HE, con rango "
    f"{f0(G['IMG_03.jpg']['rango_ganadora'])} y un `sat_bajo` de {pct(G['IMG_03.jpg']['sat_bajo_ganadora'])}. "
    f"La predicción era razonable, pero HE abrió 14 niveles más el histograma y la entropía no era el primer "
    f"criterio de desempate. La habitación tiene un histograma ancho y continuo, y HE lo aprovecha bien."
)
p_disc["IMG_04.jpg"] = (
    f"En IMG_04 predije CLAHE 2,0 / 8×8, que da rango "
    f"{f0(fila('IMG_04.jpg', 'clahe', 'clip=2.0;tile=8x8')['rango_p1_p99'])}. La ganadora fue el estiramiento "
    f"p=1–99, con rango {f0(G['IMG_04.jpg']['rango_ganadora'])}, `sat_bajo` "
    f"{pct(G['IMG_04.jpg']['sat_bajo_ganadora'])} y `sat_alto` {pct(G['IMG_04.jpg']['sat_alto_ganadora'])}. "
    f"HE también llegaba a 246, pero el estiramiento conservó más entropía y ganó el desempate. La dominante "
    f"azul sigue ahí: el procesado solo toca Y, no Cr ni Cb."
)
p_disc["IMG_05.jpg"] = (
    f"En IMG_05 predije gamma 1,0, que a efectos prácticos es la original (rango "
    f"{f0(fila('IMG_05.jpg', 'gamma', 'g=1.0')['rango_p1_p99'])}). La ganadora fue CLAHE 4,0 / 4×4, con rango "
    f"{f0(G['IMG_05.jpg']['rango_ganadora'])} y `sat_bajo` {pct(G['IMG_05.jpg']['sat_bajo_ganadora'])}. "
    f"Ganó 23 niveles de rango, pero en la figura se aprecia el grano que aparece en el fondo y en la piel de "
    f"la manzana. Es la discrepancia más clara: la imagen ya era buena y el criterio prefirió exprimir el rango."
)
for _clave in p_disc:
    p_disc[_clave] = p_disc[_clave].replace("`", "")

# ---------------------------------------------------------------------------
# HTML
# ---------------------------------------------------------------------------
css = """
@page {
  size: A4;
  margin: 2.0cm 1.8cm 1.9cm 1.8cm;
  @bottom-center { content: counter(page); font-size: 8pt; color: #555; }
}
@page :first { @bottom-center { content: none; } }
body { font-family: "DejaVu Serif", serif; font-size: 10.1pt; line-height: 1.42; color: #111; }
h1, h2, h3 { font-family: "DejaVu Sans", sans-serif; color: #111; }
h1 { font-size: 24pt; line-height: 1.15; margin: 0 0 0.4cm 0; }
h2 { font-size: 14pt; margin: 0 0 8px 0; padding-bottom: 3px; border-bottom: 1px solid #999; page-break-after: avoid; }
h2.seccion { page-break-before: always; }
h3 { font-size: 11.2pt; margin: 12px 0 4px 0; page-break-after: avoid; }
h3.salto { page-break-before: always; }
p { text-align: justify; margin: 0 0 6px 0; }
code { font-family: "DejaVu Sans Mono", monospace; font-size: 8.8pt; }
table { width: 100%; border-collapse: collapse; font-family: "DejaVu Sans", sans-serif; font-size: 8.1pt; margin: 8px 0 10px 0; page-break-inside: avoid; }
caption { caption-side: top; text-align: left; font-size: 8.6pt; color: #222; margin-bottom: 3px; }
th, td { border: 0.5px solid #aaa; padding: 3px 4px; vertical-align: top; }
th { background: #eeeeee; font-weight: bold; }
table.fuentes { font-size: 7.5pt; }
.url { color: #333; font-size: 6.8pt; word-break: break-all; }
figure { margin: 10px 0 12px 0; page-break-inside: avoid; }
figure img { display: block; max-width: 100%; height: auto; margin: 0 auto; }
figure.tall img { max-height: 21.4cm; width: auto; }
figure.error img { max-width: 14cm; }
figure.salto { page-break-before: always; }
figcaption { font-size: 8.7pt; color: #222; margin-top: 4px; text-align: left; }
.portada { text-align: center; margin-top: 4.2cm; }
.portada .sub { font-size: 13pt; color: #333; margin-top: 0.3cm; }
.portada .meta { margin-top: 3.2cm; font-size: 11pt; line-height: 1.7; }
.aviso { font-size: 8.5pt; color: #333; background: #f4f4f4; padding: 6px 8px; border-left: 2px solid #888; margin: 8px 0; }
blockquote { margin: 6px 0 8px 0; padding: 6px 10px; border-left: 2px solid #999; background: #fafafa; }
blockquote p { margin: 0 0 4px 0; }
.fuente { font-size: 8.4pt; color: #333; }
"""

portada = f"""
<div class="portada">
  <h1>Del diagnóstico numérico<br>al contrato de preprocesado</h1>
  <div class="sub">Auditoría fotométrica de un lote de cinco imágenes</div>
  <div class="meta">
    Ismael Hernández<br>
    Visión por Computador · Unidad 1<br>
    U-tad · Curso 2026–2027<br>
    26 de octubre de 2026
  </div>
</div>
"""

intro = f"""
<h2 class="seccion">1. Material y decisiones de partida</h2>
<p>He usado cinco fotografías de Wikimedia Commons, una por cada situación que pedía el enunciado. La tabla 1 recoge el papel de cada una, el autor, la licencia y el enlace a la ficha original. Las cinco se copiaron a <code>data/</code> sin retocarlas y el código comprueba al arrancar su SHA-256; si un original cambia, la libreta se detiene.</p>
{tabla_fuentes}
<p>IMG_02 no es una imagen lavada en el sentido de histograma comprimido: tiene un {pct(D['IMG_02.jpg']['sat_alto'])} de píxeles en 253 o más y conserva un rango de {f0(D['IMG_02.jpg']['rango_p1_p99'])} niveles. La elegí por el recorte de luces, que es el problema que quería cubrir, y lo digo porque el diagnóstico verbal de esa imagen no encaja con la etiqueta «poco contraste».</p>
<p>La entrada y la salida de las funciones es BGR, que es lo que devuelve <code>cv2.imread</code>; las conversiones a RGB se hacen solo para mostrar o para <code>diagnostico_color</code>. El código está en <code>codigo/auditoria_fotometrica.ipynb</code>, con un <code>requirements.txt</code> de versiones fijadas, sin instalaciones dentro de la libreta y con rutas que se resuelven desde la carpeta de entrega. La libreta se ejecutó de principio a fin antes de empaquetar.</p>
<p>Para medir y para procesar uso el canal Y de YCrCb. Y pondera R, G y B como la luminancia perceptual, mientras que la media aritmética da el mismo peso al azul que al verde. Al tocar solo Y conservo Cr y Cb, así que el color de la escena no se altera por el simple hecho de cambiar el contraste. V de HSV es max(R,G,B) y mezcla saturación con brillo; por eso lo dejo para la segmentación del Ejercicio 4 y no lo uso como luminancia. La convención de gamma es Y' = 255·(Y/255)^γ: con γ &lt; 1 aclaro y con γ &gt; 1 oscurezco. La semilla es 42 y está fijada al principio. Las métricas se calculan siempre sobre el canal Y de la imagen final, después de reconstruir el color, también en la fila «original», para que las 110 filas sean comparables entre sí.</p>
{figura('diagnostico_originales.png', f"Figura 1. Las cinco imágenes originales, sin procesar, y su histograma de luminancia (Y de YCrCb). El eje vertical está en porcentaje de píxeles y en escala logarítmica para que se vean tanto el pico de IMG_01 en los negros ({pct(D['IMG_01.jpg']['sat_bajo'])}) como el de IMG_02 en 253 o más ({pct(D['IMG_02.jpg']['sat_alto'])}). El eje horizontal va de 0 a 255 en los cinco paneles.", 'tall')}
"""

ej1 = f"""
<h2 class="seccion">2. Ejercicio 1. Medir antes de tocar</h2>
<p>La tabla 2 resume el diagnóstico de las originales. Las cifras están redondeadas como en el CSV; los cálculos se hicieron con los valores completos.</p>
{tabla_diag}
<p>{p_img['IMG_01.jpg']}</p>
<p>{p_img['IMG_02.jpg']}</p>
<p>{p_img['IMG_03.jpg']}</p>
<p>{p_img['IMG_04.jpg']}</p>
<p>{p_img['IMG_05.jpg']}</p>
<h3>Predicciones que fijé antes del barrido</h3>
<p>Las siguientes predicciones se escribieron después de mirar el diagnóstico de la tabla 2 y antes de calcular ninguna configuración procesada. Las copio del documento que guardé y feché antes de generar <code>outputs/resultados_u1.csv</code>.</p>
<blockquote>{md_simple(pred_body)}</blockquote>
"""

criterio = f"""
<h3>El criterio de selección</h3>
<p>El criterio se fijó y se guardó antes del barrido. La versión que apliqué es esta:</p>
<blockquote>{md_simple(crit_body)}</blockquote>
"""

ej2 = f"""
<h2 class="seccion">3. Ejercicio 2. Barrido sistemático</h2>
{criterio}
<p>El barrido tiene {f0(A['n_imagenes'])} imágenes × {f0(A['n_configuraciones'])} configuraciones = {f0(A['n_filas_resultados'])} filas. Las operaciones son gamma (7 valores), estiramiento lineal (4), ecualización global (1), CLAHE (9 combinaciones de clip y rejilla) y la original. Todo se aplica sobre Y y se reconstruye con Cr y Cb originales. El CSV se generó con bucles, sin escribir ninguna fila a mano; la libreta comprueba que hay exactamente 22 filas por imagen, que no hay duplicados y que no hay NaN.</p>
{tabla_gan}
<p>La ganadora de IMG_02 es la mejor de las malas. Ninguna configuración procesada baja de un 1 % de saturación alta en esa imagen, así que la regla de respaldo elige la que minimiza el máximo de las dos saturaciones. HE reduce el porcentaje de píxeles quemados de {pct(D['IMG_02.jpg']['sat_alto'])} a {pct(G['IMG_02.jpg']['sat_alto_ganadora'])} y sube el rango de {f0(D['IMG_02.jpg']['rango_p1_p99'])} a {f0(G['IMG_02.jpg']['rango_ganadora'])}, pero no recupera el detalle perdido. La comparación con la original se hace con esa advertencia.</p>
<h3>Predicciones y discrepancias</h3>
{tabla_pred}
<p>No acerté ninguna de las cinco. No me parece un fallo del método, sino del orden de prioridades: mis predicciones miraban qué operación iba a quedar mejor a ojo, y el criterio premia el rango ocupado sujeto a no saturar. Las operaciones globales y locales que más abren el histograma suelen ganar, aunque no sean las más agradables. Estos son los cinco casos.</p>
<p>{p_disc['IMG_01.jpg']}</p>
<p>{p_disc['IMG_02.jpg']}</p>
<p>{p_disc['IMG_03.jpg']}</p>
<p>{p_disc['IMG_04.jpg']}</p>
<p>{p_disc['IMG_05.jpg']}</p>
"""

# Figuras del barrido
figs_barrido = []
for i in range(1, 6):
    im = f"IMG_{i:02d}.jpg"
    g = G[im]
    o = D[im]
    if im == "IMG_02.jpg":
        extra = (
            f" Es la única imagen en la que ninguna configuración cumple las restricciones; la ganadora "
            f"se eligió por la regla de respaldo y la saturación alta sigue en {pct(g['sat_alto_ganadora'])}."
        )
    else:
        extra = ""
    pie = (
        f"Figura {i + 1}. {im}: original frente a {g['operacion']} con {g['parametros']} sobre Y. "
        f"El rango entre percentiles pasa de {f0(o['rango_p1_p99'])} a {f0(g['rango_ganadora'])} niveles; "
        f"la saturación en negro pasa de {pct(o['sat_bajo'])} a {pct(g['sat_bajo_ganadora'])} y la "
        f"saturación en blanco de {pct(o['sat_alto'])} a {pct(g['sat_alto_ganadora'])}.{extra} "
        f"Los dos histogramas de cada figura comparten ejes y escala logarítmica."
    )
    figs_barrido.append(figura(f"barrido_img{i:02d}.png", pie))
figs_barrido = "\n".join(figs_barrido)

color_txt = (
    f"En IMG_04, HE sobre Y sube las tres medias hasta "
    f"{f(C['he_y']['R'])} / {f(C['he_y']['G'])} / {f(C['he_y']['B'])} y deja B − R en "
    f"{f(C['he_y']['B_menos_R'])}, prácticamente la misma relación que había. HE por canal deja las medias en "
    f"{f(C['he_rgb']['R'])} / {f(C['he_rgb']['G'])} / {f(C['he_rgb']['B'])}, con B − R = "
    f"{f(C['he_rgb']['B_menos_R'])}: la dominante azul desaparece, pero porque se han movido los canales de "
    f"color, no porque la luminancia lo pida. Es justo el efecto que el enunciado advierte, y la razón por la "
    f"que no uso la vía RGB en el resto del trabajo."
)

ej2_figs = f"""
{figs_barrido}
<h3 class="salto">La misma operación sobre Y y sobre cada canal RGB</h3>
<p>{color_txt}</p>
{tabla_color}
{figura('comparacion_luminancia_vs_rgb.png', f"Figura 7. HE global sobre Y y HE por canal RGB en IMG_04. Las medias RGB pasan de {f(C['original']['R'])} / {f(C['original']['G'])} / {f(C['original']['B'])} en la original a {f(C['he_y']['R'])} / {f(C['he_y']['G'])} / {f(C['he_y']['B'])} con HE sobre Y, y a {f(C['he_rgb']['R'])} / {f(C['he_rgb']['G'])} / {f(C['he_rgb']['B'])} con HE por canal. B − R pasa de {f(C['original']['B_menos_R'])} a {f(C['he_y']['B_menos_R'])} y a {f(C['he_rgb']['B_menos_R'])}.")}
"""

ej3 = f"""
<h2 class="seccion">4. Ejercicio 3. Mosaico de Bayer y demosaico</h2>
<p>Elegí IMG_03 por los azulejos, las molduras y la ventana: tiene bordes nítidos y texturas finas, que es donde el demosaico debería notarse. La imagen original es de 3691 × 6048; recorté una columna para dejarla en 3690 × 6048, sin interpolar, porque el patrón RGGB necesita dimensiones pares. Uso el RGB original, no una imagen procesada.</p>
<p>El mosaico se construyó con la función del enunciado: R en (par, par), G en (par, impar) y (impar, par), B en (impar, impar). La tabla 6 muestra las fracciones contadas sobre el array. El verde se lleva la mitad de las posiciones porque el ojo humano es más sensible a esa parte del espectro y porque el verde aporta la mayor parte de la luminancia; el sensor reparte más fotositos donde más información útil hay.</p>
{tabla_bayer}
<p>El demosaico es propio, sin <code>cv2.cvtColor</code> con códigos Bayer. Para cada canal construyo su máscara de posiciones medidas, convoluciono el mosaico enmascarado con el núcleo bilineal correspondiente y normalizo. Uso el núcleo [[0,1,0],[1,4,1],[0,1,0]]/4 para el verde y [[1,2,1],[2,4,2],[1,2,1]]/4 para el rojo y el azul, con borde reflejado. Después reinyecto los valores medidos en sus posiciones para que se conserven exactamente, también en los bordes. Las pruebas de la libreta comprueban que una imagen constante se reconstruye sin error en el interior y que cada píxel medido conserva su valor original.</p>
{figura('demosaico_visual.png', f"Figura 8. Recorte de {f0(M['lado_recorte'])} × {f0(M['lado_recorte'])} píxeles de IMG_03: original RGB, mosaico RGGB y reconstrucción bilineal con núcleos [[0,1,0],[1,4,1],[0,1,0]]/4 para el verde y [[1,2,1],[2,4,2],[1,2,1]]/4 para el rojo y el azul, con borde reflejado. El MAE total es {f(M['mae_total'])} niveles; el verde, con el doble de muestras, es el canal que mejor se reconstruye ({f(M['mae_G'])}).", 'salto')}
{tabla_dem}
<p>El cociente de {f(M['cociente_bordes_resto'])} sostiene la afirmación de que el demosaico falla sobre todo en los bordes: el error medio en la máscara de Canny es casi el triple que en las zonas planas. La comparación tiene una limitación que conviene no esconder: el JPEG de partida ya viene demosaicado y comprimido, así que estoy midiendo mi interpolador contra una imagen que a su vez es el resultado de otra interpolación. La cifra sirve para comparar el comportamiento relativo, no como error absoluto de un sensor real.</p>
{figura('error_demosaico.png', f"Figura 9. Mapa de error del demosaico, suma de las diferencias absolutas de los tres canales en falso color y escala logarítmica. La máscara de borde se obtuvo con Canny {f0(M['umbral_canny_bajo'])}/{f0(M['umbral_canny_alto'])} sobre la luminancia y una dilatación de {f0(M['dilatacion_px'])} px; cubre el {f(M['porcentaje_bordes'])} % de los píxeles. El MAE en bordes es {f(M['mae_bordes'])} frente a {f(M['mae_resto'])} en el resto, un cociente de {f(M['cociente_bordes_resto'])}.", 'error')}
"""

ej4 = f"""
<h2 class="seccion">5. Ejercicio 4. Robustez de la segmentación HSV</h2>
<p>La imagen del objeto es IMG_05. El rojo cae en la costura del tono, así que uso dos ventanas: H ≤ 20 o H ≥ 160. Exijo S ≥ 70 para descartar el fondo gris y V ≥ 30 para no perder la sombra de la manzana. Después de la máscara me quedo con la componente conexa mayor, que elimina las motas de JPEG. Los valores quedaron congelados antes de medir la robustez; el CSV de referencia tiene {f0(H['area_pixeles'])} píxeles, el {pct(H['area_porcentaje'])} de la imagen.</p>
{figura('mascara_referencia_visual.png', f"Figura 10. IMG_05 y la máscara de referencia superpuesta. Los rangos congelados son H ≤ {f0(H['hue_alto'])} o H ≥ {f0(H['hue_bajo'])}, S ≥ {f0(H['sat_min'])} y V ≥ {f0(H['val_min'])}, con la componente conexa mayor. La máscara cubre el {pct(H['area_porcentaje'])} de la imagen; incluye el reflejo rojizo de la base, que comparte tono y saturación con la manzana.")}
<p>Perturbé la luminancia con γ ∈ {{0,5; 0,7; 1,0; 1,4; 2,0}} y apliqué exactamente los mismos rangos. Para la intervención usé la ganadora de IMG_05 en el barrido, CLAHE con clip 4,0 y rejilla 4×4, sobre la imagen ya perturbada. La referencia sigue siendo la máscara de la imagen original. La tabla 8 resume los diez valores del CSV; el control sin normalización vale exactamente 1,0000 y la libreta lo comprueba con un <code>assert</code>.</p>
{tabla_rob}
{figura('robustez_hsv.png', f"Figura 11. IoU de la máscara HSV frente a γ, sin normalización y con CLAHE 4,0 / 4×4 sobre Y. La IoU media baja de {f(RR['sin_normalizacion']['iou_media'], 4)} a {f(RR['con_normalizacion']['iou_media'], 4)}; el peor caso sube de {f(RR['sin_normalizacion']['iou_peor'], 4)} a {f(RR['con_normalizacion']['iou_peor'], 4)}. En el control γ=1,0 la normalización da {f(RR['con_normalizacion']['iou_control'], 4)}, no 1, porque CLAHE también cambia la imagen.")}
<p>El resultado es mixto y conviene decirlo sin adornos. La media empeora: {f(RR['sin_normalizacion']['iou_media'], 4)} sin normalización frente a {f(RR['con_normalizacion']['iou_media'], 4)} con ella. El peor caso mejora: {f(RR['sin_normalizacion']['iou_peor'], 4)} frente a {f(RR['con_normalizacion']['iou_peor'], 4)}, y el mínimo se queda en γ=0,5. La intervención ayuda en los extremos (γ=0,5 y γ=2,0) porque devuelve parte del área que la perturbación había comprimido, pero estropea los casos intermedios: en γ=0,7, γ=1,0 y γ=1,4 la imagen ya estaba cerca de la referencia y CLAHE la mueve fuera de los rangos congelados. El control con normalización, {f(RR['con_normalizacion']['iou_control'], 4)}, es la prueba de que la propia operación cambia la imagen aun sin perturbación.</p>
<p>La explicación que me parece más plausible es que CLAHE redistribuye el valor y la saturación de forma local. En los extremos, la escena está tan comprimida que esa redistribución acerca los píxeles al rango de la referencia; en el centro, en cambio, los separa. No puedo descartar que con otra rejilla o un clip más bajo la media también mejorase, pero eso ya sería otro contrato y no el que fijé antes de medir.</p>
"""

ej5 = f"""
<h2 class="seccion">6. Ejercicio 5. Contrato de preprocesado</h2>
<p>El contrato completo está en <code>memoria/contrato_preprocesado.md</code>. La función <code>preprocesar</code> aplica la configuración del lote, CLAHE con <code>clip=4.0</code> y <code>tile=4x4</code> sobre Y, sin parámetros libres. La regla de lote la eligió porque cumple las dos restricciones en {f0(L['imagenes_que_cumplen'])} de las {f0(A['n_imagenes'])} imágenes y, entre las que cumplen en cuatro, tiene el mayor rango medio ({f(L['rango_medio'], 1)} niveles). La única imagen que falla es {L['imagenes_falla']}, la de las luces quemadas.</p>
{tabla_pre}
<p>La función reproduce exactamente su fila del CSV en las cinco imágenes: la libreta compara <code>sat_bajo</code>, <code>sat_alto</code>, rango, entropía y desviación típica después de aplicar <code>preprocesar</code> y los hace coincidir con los valores redondeados del CSV. La mejora medida en el Ejercicio 4 es la misma que la del contrato, porque la ganadora de IMG_05 y la configuración del lote coinciden: la media baja y el peor caso sube. El contrato se adopta por la regla declarada, no porque la IoU media lo haga indiscutible.</p>
<p>El apartado 4 del contrato es el que más me importa: la función no recupera luces quemadas, no corrige dominantes de color y amplifica el grano en zonas uniformes. En producción, la alarma sería <code>sat_alto &gt; {f(umb[umb['metrica'] == 'sat_alto']['umbral'].iloc[0], 1)} %</code> o <code>rango_p1_p99 &lt; {f0(umb[umb['metrica'] == 'rango_p1_p99']['umbral'].iloc[0])}</code> niveles; en este lote, las cuatro imágenes que cumplen quedan entre {pct(pre.loc[pre['imagen'] != 'IMG_02.jpg', 'sat_alto'].min())} y {pct(pre.loc[pre['imagen'] != 'IMG_02.jpg', 'sat_alto'].max())} de saturación alta, mientras IMG_02 salta a {pct(PRE['IMG_02.jpg']['sat_alto'])}.</p>
"""

limit = f"""
<h2 class="seccion">7. Limitaciones</h2>
<p>El lote tiene cinco imágenes y una sola tarea de segmentación. Las conclusiones sobre qué operación gana no se pueden generalizar a cualquier escena, y menos con una imagen por situación. La perturbación del Ejercicio 4 es gamma sobre Y; no simula ruido de sensor, cambios de exposición reales, movimiento ni luces mezcladas. La comparación de Bayer se hace contra un JPEG que ya pasó por un demosaico y una compresión, así que el error absoluto está contaminado por ese proceso. La máscara HSV se congeló para una manzana roja concreta e incluye su reflejo en la base; un objeto de otro color o una dominante extrema pueden caer fuera de las dos ventanas.</p>
<p>El criterio de selección maximiza el rango entre percentiles sujeto a no saturar, y eso tiene una consecuencia clara: premia operaciones que abren mucho el histograma, aunque levanten ruido. Se ve en IMG_01 y en IMG_05, donde CLAHE 4,0 mejora las métricas pero deja un fondo más granoso. No he medido ese ruido con una cifra propia, y por eso no lo uso para cambiar el criterio; lo dejo como una limitación del criterio y como una línea de trabajo. Con más datos añadiría una métrica de ruido en zonas planas y una validación visual repetible, además de más imágenes y un objeto distinto para la segmentación.</p>
<p>Las predicciones fallaron las cinco. No las he retocado después de ver los resultados; sirven para mostrar que el barrido encontró configuraciones que mi intuición no habría probado, y que el criterio declarado tiene más peso que la impresión inicial.</p>
"""

html_doc = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Del diagnóstico numérico al contrato de preprocesado</title>
<meta name="author" content="Ismael Hernández">
<meta name="description" content="Práctica individual de Visión por Computador, Unidad 1. Auditoría fotométrica de cinco imágenes.">
<style>{css}</style>
</head>
<body>
{portada}
{intro}
{ej1}
{ej2}
{ej2_figs}
{ej3}
{ej4}
{ej5}
{limit}
</body>
</html>
"""

Path("_trabajo/informe.html").write_text(html_doc, encoding="utf-8")
HTML(string=html_doc, base_url=str(ENT.resolve())).write_pdf(MEM / "informe.pdf")
print("PDF generado:", MEM / "informe.pdf")
