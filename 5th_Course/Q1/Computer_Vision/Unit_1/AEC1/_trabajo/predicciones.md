# Predicciones antes del barrido

Fecha: 26 de octubre de 2026. Escritas después de mirar el diagnóstico de las originales
y antes de calcular ninguna configuración procesada.

## IMG_01 (subexpuesta)

El 40,38 % de los píxeles tiene Y <= 2, la entropía es 4,98 bits y la desviación típica
32,8. La información está apelotonada en la zona oscura y no hay nada quemado. Espero que
gamma con g=0,6 sea la ganadora: debería liberar sombras sin llevar demasiados píxeles al
blanco. Gamma 0,45 también puede funcionar, pero me da miedo que aplane el fondo y baje la
entropía al juntar los grises.

## IMG_02 (sobreexpuesta)

Tiene un 26,36 % de píxeles en 253 o más, con una entropía de 6,63 bits y un rango de 238
niveles. Es una imagen con luces claramente quemadas, así que ninguna operación puntual
puede recuperar el detalle perdido. Espero que el criterio de respaldo acabe eligiendo una
configuración que no empeore aún más el blanco, probablemente gamma 2,2 o un CLAHE suave
con clip=1,0. No me sorprendería que la mejora frente a la original fuese nula.

## IMG_03 (iluminación desigual)

El rango entre percentiles es 192, la entropía 7,37 bits y la desviación 46,4, con solo un
0,23 % de píxeles en negro. Hay una ventana muy luminosa y una habitación en sombra en el
mismo encuadre. Aquí espero que CLAHE con clip=2,0 y bloques de 8×8 gane al estiramiento
global, porque necesita tratar de forma distinta las dos zonas. La dominante cálida de la
escena (medias RGB 98,4 / 74,6 / 53,5) no la corregirá un procesado sobre Y, y eso no me
preocupa para este ejercicio.

## IMG_04 (dominante de color)

La media del canal B (118,5) supera a la de R (104,4) y a la de G (96,9): la escena tira a
azul. La entropía es 7,32 bits y el rango 198, así que el histograma ya ocupa bastante. No
espero que el procesado arregle la dominante, porque trabajo solo sobre luminancia.
Predicción: CLAHE con clip=2,0 y bloques de 8×8 mejorará algo el contraste local, o quizá
HE si el histograma es suficientemente continuo.

## IMG_05 (objeto saturado)

El rango es 210, la entropía 6,73 bits y solo un 0,05 % de píxeles está quemado. La manzana
llena el encuadre y el fondo gris está bien separado. Es la imagen con menos margen de
mejora. Espero que gane gamma 1,0, que a efectos prácticos es la original, o un estiramiento
suave p=1–99. Si gana una operación más agresiva, miraré si el criterio está premiando el
rango a costa de inventar contraste en el fondo.
