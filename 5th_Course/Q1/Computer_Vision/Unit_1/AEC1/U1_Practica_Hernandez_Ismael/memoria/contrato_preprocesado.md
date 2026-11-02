# Contrato de preprocesado

## 1. Qué hace

`preprocesar(img)` recibe una imagen BGR de 8 bits y devuelve otra del mismo tamaño. Pasa a YCrCb, aplica CLAHE sobre Y con clip 4,0 y rejilla 4×4, y reconstruye el color sin tocar Cr y Cb. No tiene parámetros libres.

## 2. Parámetros y fila de origen

La configuración es `clahe` con `clip=4.0;tile=4x4`, tomada de la fila `IMG_05.jpg,clahe,clip=4.0;tile=4x4` de `outputs/resultados_u1.csv`, que también existe para `IMG_01.jpg`, `IMG_03.jpg` e `IMG_04.jpg`. La regla de lote declarada antes del barrido la eligió porque cumple `sat_bajo ≤ 1 %` y `sat_alto ≤ 1 %` en cuatro de las cinco imágenes y, entre esas, tiene el mayor rango medio (234,6 niveles). Falla en `IMG_02.jpg`, con un 26,36 % de píxeles quemados.

## 3. Mejora aportada

La IoU media de los cinco γ baja de 0,9760 sin normalización a 0,9686 con el contrato; el peor caso sube de 0,9439 a 0,9556, ambos en γ=0,5. En el control γ=1,0 la normalización deja la IoU en 0,9710, por debajo de 1,0, porque CLAHE cambia la imagen. La mejora es parcial: protege el extremo más luminoso (γ=0,5), pero no la media.

## 4. Dónde deja de funcionar

No recupera información quemada: en `IMG_02.jpg` el 26,36 % de píxeles con Y ≥ 253 pasa a 25,18 % y la alarma sigue encendida. Tampoco corrige dominantes: en `IMG_04.jpg` las medias RGB pasan de 104,4 / 96,9 / 118,5 a 129,2 / 121,7 / 142,9, con B−R de 13,7 niveles. El clip alto y la rejilla 4×4 amplifican el grano en zonas uniformes; en el fondo de `IMG_01.jpg` `sat_bajo` baja de 40,38 % a 0,00 % a costa de levantar ruido. La máscara HSV depende de que el objeto conserve tono y saturación dentro de H ≤ 20 o H ≥ 160, S ≥ 70 y V ≥ 30, y además incluye el reflejo rojizo de la base de la manzana.

## 5. Qué medir en producción

Tras aplicar la función, alarma si `sat_alto > 5 %` o si `rango_p1_p99 < 200` niveles. En el lote, las cuatro imágenes que cumplen quedan entre 0,00 % y 0,08 % de saturación alta, mientras la que falla salta a 25,18 %; el rango mínimo es 212 (`IMG_01.jpg`) y el máximo 249. Los dos umbrales separan con holgura esos casos y obligan a revisar la escena antes de seguir.
