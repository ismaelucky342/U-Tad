# U1 · Resumen de estudio — Visión por Computador

Repaso rápido para examen. Detalle, ejemplos y código: [temario denso](U1_temario_denso.md). Ejercicios: [`ejercicios/`](ejercicios/README.md).

---

## 1. Key concepts

**Visión física y biológica** → [§2](U1_temario_denso.md#2-visión-física-y-biológica)
- Ver = cadena escena → óptica → sensor → ADC → ISP → imagen digital → preprocesado.
- Luz y materia: $\rho+\alpha+\tau=1$ (reflejada + absorbida + transmitida). Cada material tiene una **firma espectral**.
- Visible ≈ 380-780 nm (según el material). Fuera: UV, IR (NIR para materiales, LWIR para termografía).
- Ojo: **bastones** (poca luz, sin color), **conos** S/M/L (color, fóvea). Daltonismo = fallo de algún tipo de cono.

**Modelos de cámara** → [§3](U1_temario_denso.md#3-modelos-de-cámara)
- *Pinhole*: imagen nítida y oscura; agujero grande = borrón geométrico, agujero muy pequeño = difracción.
- Lente delgada: más luz, pero solo un plano enfocado (profundidad de campo).
- $N=f/D$: la luz recibida escala con $1/N^2$. Cerrar diafragma → más DOF, más difracción.

**Sensores y pipeline** → [§4](U1_temario_denso.md#4-sensores-de-imagen-y-pipeline-de-formación-ccd-vs-cmos)
- Fotón → carga (fotodiodo) → tensión → **ADC** (muestreo + cuantización) → RAW → ISP.
- **CCD** (*Charge*-Coupled): la carga se transfiere hasta una salida común; muy uniforme, más consumo.
- **CMOS**: amplificador por píxel, ADC por columna, lectura rápida; *rolling* o *global shutter*.
- ISP: RAW lineal → demosaico → balance de blancos → corrección de color → gamma → compresión.

**Imagen digital y color** → [§5](U1_temario_denso.md#5-imagen-digital-y-gestión-del-color)
- Triple-CCD: 3 valores medidos por píxel. **Bayer RGGB**: 1 medido + 2 interpolados (demosaico).
- Demosaico: artefactos de **falso color** en detalles de 1 píxel.
- Memoria: $W\cdot H\cdot C\cdot b/8$ bytes.
- sRGB está **codificado con gamma**; promediar, mezclar o iluminar bien exige **luz lineal**.
- Espacios: RGB (captura/pantalla), HSV (matiz), YCbCr/Lab (separan luminancia de color).

**Operaciones por histograma** → [§6](U1_temario_denso.md#6-operaciones-puntuales-basadas-en-histograma)
- Histograma = diagnóstico antes de actuar. Operación puntual = LUT $s=T(r)$.
- Negativo, gamma, stretching, umbral/Otsu, HE (global), AHE (local), CLAHE (local limitada).
- En color: operar sobre **luminancia**, no por canal RGB.

---

## 2. Fórmulas esenciales

| Tema | Fórmula | Símbolos |
|---|---|---|
| Luz y materia | $\rho+\alpha+\tau=1$ | reflejada, absorbida, transmitida |
| Pinhole | $u=f_x\dfrac{X}{Z}+c_x,\; v=f_y\dfrac{Y}{Z}+c_y$ | $(X,Y,Z)$ punto 3D, $(c_x,c_y)$ centro óptico |
| Lente delgada | $\dfrac1f=\dfrac1{d_o}+\dfrac1{d_i}$ | $d_o$ objeto, $d_i$ imagen |
| Ampliación | $m=-d_i/d_o$ | signo − = imagen invertida |
| FOV | $2\arctan\dfrac{w}{2f}$ | $w$ ancho del sensor |
| Número f | $N=f/D$ | luz $\propto1/N^2$ |
| Hiperfocal | $H=\dfrac{f^2}{Nc}+f$ | $c$ círculo de confusión |
| Disco de Airy | $\approx2{,}44\,\lambda N$ | diámetro del primer cero |
| Cuantización | $\Delta=V/2^b,\;\sigma^2=\Delta^2/12$ | SQNR ≈ $6{,}02\,b+6{,}02$ dB |
| Memoria | $W\cdot H\cdot C\cdot b/8$ | Full HD RGB 8 bit ≈ 6,22 MB |
| sRGB → lineal | $x\le0{,}04045:\;x/12{,}92$; si no, $\big(\tfrac{x+0{,}055}{1{,}055}\big)^{2{,}4}$ | $x\in[0,1]$ |
| Luma | Rec.601: $0{,}299R+0{,}587G+0{,}114B$; Rec.709: $0{,}2126R+0{,}7152G+0{,}0722B$ | pesos distintos |
| Negativo | $s=(L-1)-r$ | involución |
| Gamma | $s=r^\gamma$ | $\gamma<1$ aclara, $>1$ oscurece |
| Stretching | $s=\dfrac{r-a}{b-a}(L-1)$ en $(a,b)$ | satura fuera |
| Otsu | $\sigma_B^2=\omega_0\omega_1(\mu_0-\mu_1)^2$ | maximizar sobre $t$ |
| HE | $s_k=\mathrm{round}\Big((L-1)\dfrac{\mathrm{cdf}(k)-\mathrm{cdf}_{\min}}{N-\mathrm{cdf}_{\min}}\Big)$ | CDF del histograma |
| CLAHE | $\text{clip\_count}=\max(\lfloor\text{clip}\cdot A/256\rfloor,1)$ | deducido del comportamiento de OpenCV |

---

## 3. ¿Cuándo usar qué?

**Cámara**

| Necesito… | Uso |
|---|---|
| Modelo geométrico simple (calibración) | Pinhole |
| Más luz y nitidez realista | Lente delgada |
| Mucha profundidad de campo | Diafragma cerrado (¡sin pasarse: difracción!) |

**Sensor**

| Prioridad | Sensor |
|---|---|
| Uniformidad, bajo ruido (aplicaciones científicas clásicas) | CCD |
| Velocidad, consumo, coste, integración | CMOS |
| Sin distorsión por movimiento | Global shutter |
| Máxima fidelidad de color | Triple-CCD (caro) |
| Coste/tamaño razonables | Bayer + demosaico |

**Preprocesado por histograma**

| Diagnóstico | Operación |
|---|---|
| Subexpuesta / lavada | Gamma $<1$ / $>1$ |
| Rango estrecho | Stretching (percentiles si hay ruido) |
| Contraste global pobre | HE |
| Iluminación desigual | CLAHE (clip 2-4) |
| Objeto sobre fondo (bimodal) | Otsu |
| Fondo desigual | Umbral adaptativo o corregir iluminación antes |
| Polaridad invertida | Negativo |

---

## 4. Checklist: debo saber…

- [ ] Describir la cadena de formación de imagen de la escena a la matriz de píxeles.
- [ ] Proyectar un punto 3D con la matriz $K$ y explicar $c_x,c_y,f_x,f_y$.
- [ ] Explicar el compromiso *pinhole*: borrón geométrico frente a difracción.
- [ ] Usar $1/f=1/d_o+1/d_i$, FOV, $N=f/D$ y su efecto en luz y DOF.
- [ ] Explicar muestreo y cuantización y calcular $\Delta$ y el SQNR.
- [ ] Comparar CCD y CMOS (arquitectura, ventajas, *rolling shutter*).
- [ ] Explicar Bayer, demosaico y por qué aparece falso color.
- [ ] Calcular memoria de una imagen y detectar los fallos de `uint8` (*wraparound*).
- [ ] Justificar por qué se promedia en luz lineal y no en sRGB.
- [ ] Interpretar un histograma y elegir la operación adecuada.
- [ ] Aplicar a mano negativo, gamma, stretching y HE a una imagen pequeña.
- [ ] Calcular $\sigma_B^2$ de Otsu para un histograma pequeño.
- [ ] Distinguir HE, AHE y CLAHE y explicar el papel de `clipLimit`.
- [ ] Explicar por qué en color se ecualiza la luminancia y no cada canal RGB.

---

## 5. Errores típicos de examen

- Confundir **reflectancia** con transmitancia o decir que la suma $\rho+\alpha+\tau$ puede superar 1.
- Escribir "Change-Coupled" (es *Charge*-Coupled).
- Decir que un agujero más pequeño siempre da más nitidez (la difracción lo impide).
- Olvidar que $v$ crece hacia **abajo** y $Z>0$ en la proyección.
- Asumir que Bayer mide los tres canales en cada píxel.
- Olvidar que OpenCV usa **BGR** y que sus nombres Bayer se leen "al revés" (RGGB ↔ `BayerBG2RGB`).
- Operar con `uint8` sin cuidado (`200+100=44`; `-x` en `uint8` da la vuelta).
- Aplicar gamma directamente en sRGB sin saber que no equivale a hacerlo en luz lineal.
- Usar stretching min-max con un píxel "caliente": no estira nada. Usar percentiles.
- Esperar que stretching o HE **creen información**: solo la redistribuyen (la entropía no sube con stretching).
- Ecualizar R, G y B por separado (cambia el matiz).
- Creer que CLAHE por defecto en OpenCV es suave (`clipLimit=40`).
- En Otsu, olvidar los **empates** si hay niveles vacíos.

---

## 6. Autoevaluación

1. ¿Qué tres cosas puede hacer un fotón al llegar a una superficie y qué relación cumplen?
2. ¿Por qué los conos L no son "rojos" estrictamente?
3. ¿Qué dos efectos opuestos fijan el tamaño óptimo del agujero en un *pinhole*?
4. Si cierras el diafragma de $f/4$ a $f/8$, ¿cuánta luz entra (en proporción) y qué ganas y pierdes?
5. ¿Qué error de cuantización (varianza) tiene un ADC de paso $\Delta$?
6. Diferencia esencial entre CCD y CMOS en cómo se lee la carga.
7. En un patrón Bayer RGGB, ¿qué fracción de píxeles mide cada color?
8. ¿Por qué un trazo blanco de 1 píxel sobre negro genera falso color con Bayer?
9. ¿Cuántos bytes ocupa una imagen RGB de 1920×1080 a 8 bit?
10. ¿Por qué promediar blanco y negro en sRGB da un gris más oscuro de lo esperado físicamente?
11. Dado el histograma $[10,20,5,0,0,5,25,35]$ (3 bits), ¿qué umbral de Otsu devuelve el algoritmo estándar y por qué hay empate?
12. Aplica HE a la imagen 3 bit $[[0,1,1,2],[1,2,2,3],[2,3,3,3],[3,3,4,5]]$: ¿cuál es la LUT?
13. ¿En qué se diferencia CLAHE de AHE y qué evita?
14. ¿Qué hace $\gamma<1$ con el histograma?
15. ¿Por qué ecualizar por canal RGB altera el color?

<details>
<summary><strong>Respuestas</strong></summary>

1. Reflejarse, absorberse o transmitirse: $\rho+\alpha+\tau=1$.
2. Su pico está ≈ 560 nm (amarillo-verdoso); "rojo" es una simplificación del material; se perciben rojos por la comparación L/M.
3. Borrón geométrico (crece con el diámetro) y difracción (crece al reducirlo): el óptimo equilibra ambos, $\approx1{,}9\sqrt{\lambda f}$.
4. Un cuarto de la luz ($1/N^2$): ganas profundidad de campo, pierdes luz y, a partir de cierto punto, nitidez por difracción.
5. $\sigma^2=\Delta^2/12$ (error uniforme en $[-\Delta/2,\Delta/2]$).
6. CCD: la carga se transfiere píxel a píxel hasta una salida común. CMOS: cada píxel convierte a tensión y se lee por filas/columnas.
7. 50 % verde, 25 % rojo, 25 % azul.
8. El detalle cae en un único canal de la malla; el demosaico interpola los otros desde vecinos que no lo contienen, y aparece un color erróneo (p. ej. magenta).
9. $1920\cdot1080\cdot3=6\,220\,800$ B ≈ 6,22 MB.
10. sRGB está codificado con gamma: el valor 127 no es "mitad de luz". En luz lineal el promedio da ≈ 0,735 en sRGB (más claro que 0,5).
11. $t=2$; los niveles 3 y 4 están vacíos, así que $t=2,3,4$ dan el mismo $\sigma_B^2=7{,}146$ y se devuelve el primero.
12. LUT $=[0,1,3,6,7,7,7,7]$ (con $\mathrm{cdf}_{\min}=1$, $N=16$).
13. CLAHE recorta el histograma local (reparte el exceso) y interpola entre baldosas: evita el ruido amplificado y los saltos de frontera.
14. Lo desplaza hacia niveles altos (aclara sombras sin tocar 0 ni 1).
15. Cambia las proporciones entre R, G y B, y por tanto el matiz; se opera sobre la luminancia.

</details>
