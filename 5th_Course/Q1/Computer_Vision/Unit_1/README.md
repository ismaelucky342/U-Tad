# Ejercicios · Unidad 1 · Fundamentos de Visión por Computador e imagen digital

Hay **dos series** de ejercicios en esta carpeta. Todas se ejecutan sin descargar nada (imágenes incluidas en scikit-image o sintéticas) y con semillas fijas.

```bash
pip install -r requirements.txt
python ej01_camara_optica.py
```

Los ejercicios que guardan figuras las escriben en `salida/` (se crea sola).

## Serie A · usada en el temario denso (verificada paso a paso)

Cada script termina con un bloque `QUÉ OBSERVAR` (solución comentada).

| # | Archivo | Dificultad | Tema | Sección del temario |
|---|---|---|---|---|
| 1 | `ej01_camara_optica.py` | ⭐ | Proyección pinhole, borrón geométrico vs difracción, lente delgada, FOV, DOF, disco de Airy | §3 |
| 2 | `ej02_imagen_digital.py` | ⭐ | Memoria de imágenes, trampas de tipos de dato, cuantización, banding, sRGB frente a lineal | §4.2, §5.3-§5.4 |
| 3 | `ej03_bayer_vs_triple.py` | ⭐⭐ | Mosaico Bayer + demosaico frente a Triple-CCD; falso color; código de OpenCV correcto | §5.1-§5.2 |
| 4 | `ej04_operaciones_puntuales.py` | ⭐⭐ | Negativo, gamma, stretching, umbralización (Otsu) | §6.2-§6.5 |
| 5 | `ej05_he_ahe_clahe.py` | ⭐⭐⭐ | HE, AHE y CLAHE desde cero, comparados con OpenCV; ruido y clip limit | §6.6-§6.8 |

### Valores de referencia

| Ejercicio | Resultado clave |
|---|---|
| 1 | Punto (0,5; 0,2; 5) m → píxel (1660; 820). Diámetro óptimo de pinhole ≈ 0,26 mm. A f/8 el disco de Airy mide 10,74 µm. |
| 2 | Full HD RGB 8 bit = 6,22 MB. Rampa a 8 bit: escalones de 4 columnas; a 4 bit, de 68. |
| 3 | Con el código de color del material un rojo puro sale azul. Demosaico propio = OpenCV (dif. máx. 1e-5). En la franja de 1 px Triple-CCD gana por ~33 dB. |
| 4 | Negativo exacto en enteros; en float el error es ~3e-8. Otsu = 102 en OpenCV y scikit-image. Gamma "en sRGB" y "en lineal" difieren hasta 21 niveles. |
| 5 | HE propia = `cv.equalizeHist` (0 píxeles distintos). CLAHE propia = OpenCV con dif. máx. 2 niveles. Con σ=2 de ruido, la zona plana pasa a σ≈5,9 con CLAHE clip 2 y a σ≈66 con clip 40. |

## Serie B · de una sesión anterior (18 oct), sin modificar

Se ejecutan sin errores ni avisos. Complementan a la serie A: incluyen Otsu implementado desde el histograma y utilidades comunes (`utils_vision.py`).

| Archivo | Dificultad | Tema |
|---|---|---|
| `ej01_representacion_digital.py` | ⭐ | Memoria, float→uint8, cuantización y banding |
| `ej01_optica_pinhole_lente.py` | ⭐ | Cámara oscura y lente delgada (enunciado y solución) |
| `ej02_optica_pinhole_lente.py` | ⭐⭐ | Pinhole, borrón, DoF, Airy |
| `ej03_bayer_demosaico.py` | ⭐⭐ | Bayer, demosaico y Triple-CCD |
| `ej04_histograma_puntuales_otsu.py` | ⭐⭐ | Operaciones puntuales y Otsu |
| `ej05_umbral_ecualizacion_clahe.py` | ⭐⭐⭐ | Otsu, HE, AHE y CLAHE desde cero |

## Ideas para ampliar

- Calcula a qué número f la difracción (disco de Airy) iguala el tamaño de píxel de tu móvil.
- Implementa el demosaico de gradiente corregido (Malvar-He-Cutler) y compara el PSNR en la franja.
- Prueba CLAHE sólo sobre el canal L de una imagen en Lab (`cv.cvtColor(..., cv.COLOR_BGR2LAB)`) para no alterar el color.
