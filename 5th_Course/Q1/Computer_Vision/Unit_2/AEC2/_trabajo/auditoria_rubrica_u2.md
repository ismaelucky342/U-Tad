# Auditoría de la rúbrica U2 y herencia de la AEC1

## Qué he comprobado

He cruzado la rúbrica de la Unidad 2 con lo que hay en `outputs/`, en el código y en la memoria. También he revisado los comentarios de la AEC1 para ver qué problemas podían repetirse en la U2. La documentación de trabajo queda en `memoria/informe.md`; no he vuelto a generar el PDF.

## Rúbrica U2

| Criterio | Evidencia en la U2 | Estado |
| --- | --- | --- |
| Cuatro rejillas completas | `resultados_denoising.csv` (180), `perfiles_frecuencia.csv` (42), `barrido_canny.csv` (24), `repetibilidad.csv` (171). Los `assert` comprueban filas y columnas. | Cubierto. |
| Mediana híbrida y truncada propias | `mediana_hibrida`, `media_recortada` y `mediana_truncada_literal`; tests contra implementación ingenua. | Cubierto. |
| Perfil radial correcto | `perfil_radial`, `frecuencia_corte`, `contar_rebotes`; test con cajas y gaussianos. | Cubierto. |
| Escena sintética con referencia por código | `crear_escena_sintetica`; la referencia sale de las primitivas, no de Canny. | Cubierto. |
| Repetibilidad con recorte fuera de encuadre | `repetibilidad` proyecta con la homografía y descarta los puntos fuera; test de 90° contra `np.rot90`. | Cubierto. |
| Parámetros de barrido con criterio declarado | `registro_parametros.csv` y `_trabajo/criterios_declarados.md`; truncada, bilaterales, ε, σ de Canny, umbrales y detectores. | Cubierto. |
| Pérdida de la regla general | F1 0,102554 frente a 0,998268; pérdida absoluta 0,895713 y relativa 0,897268. | Cubierto. |
| Invarianza de FAST a escala | 0,925401 / 1,000000 / 0,340000 en IMG_01; se refuta con cifras. | Cubierto. |
| Discrepancia PSNR/SSIM | IMG_01 σ=20 y IMG_02 σ=20; se explica qué mide cada métrica. | Cubierto. |
| Figuras con ejes, unidades y escalas | E1 con barras de color; E2 con escala logarítmica; E3 y E4 con ejes rotulados y escalas comunes. | Cubierto; los pies del MD incluyen parámetros y cifras. |
| Semilla, módulos, rutas y requirements | Semilla 20260101, funciones separadas, `Path` relativo y versiones fijadas. | Cubierto. |
| Ejecución limpia | Prueba en `/tmp/opencode/aec2_nb`; CSV idénticos salvo `tiempo_ms`; notebook de 16 celdas ejecutado. | Cubierto. |

## Problemas de la AEC1 que podían heredarse

| Problema AEC1 | ¿Se hereda en la U2? | Qué he hecho |
| --- | --- | --- |
| Figuras ausentes en el PDF por exportar desde Notion | No en el PDF de la U2: el PDF actual sí las incluye. En el MD van como enlaces relativos a `../outputs/figuras/`. | El MD enlaza las 22 figuras. Si se exporta a PDF, hay que comprobar que el conversor las incrusta. |
| La memoria cita ficheros que no están en el zip | Sí, en la versión PDF: citaba `_herramientas/tests` y los comandos de `_herramientas`. | Corregido en el MD: los tests y el verificador se describen como internos, no como archivos entregados; A.3 solo usa `python codigo/banco_pruebas.py`. |
| Componente conexa mayor no justificada | No aplica: la U2 no usa componentes conexas. | Nada que corregir. |
| IoU con eje 0–1 que aplana diferencias | No aplica: no hay IoU. Las curvas de repetibilidad van de 0 a 1 porque la métrica está acotada. | Nada que corregir. |
| Falta la rejilla de máscaras por γ | No aplica: no hay segmentación HSV. | Nada que corregir. |
| Ninguna imagen lavada de histograma comprimido | No es un requisito de la U2. Las tres imágenes cubren textura, fondo saturado y ruido real. | Se declara como límite del lote, no como fallo de la rejilla. |
| Métricas mal normalizadas | No: PSNR y SSIM usan `data_range=255`; hay tests con negro, blanco y una imagen conocida. | Cubierto. |
| Configuración de barrido ausente | No: las cuatro rejillas están completas y los barridos auxiliares están en `outputs/`. | Cubierto. |
| `requirements` sin versiones | No: `codigo/requirements.txt` lleva versiones fijadas. | Cubierto. |
| Código monolítico o no reproducible | No: el banco es modular y se ejecuta en limpio; el notebook está ejecutado. | Cubierto. |

## Riesgos que quedan

1. **MD frente a PDF.** La rúbrica y el enunciado piden PDF; el MD es la fuente, no el formato de entrega. Si se entrega solo el MD, se pierde el criterio de comunicación. Hay que generar el PDF desde el MD o desde el HTML y revisar que las figuras aparezcan.
2. **Conversión del MD.** Si se pega en Notion o en un conversor que no resuelva rutas relativas, las figuras pueden quedar como enlaces rotos. Hay que comprobar el PDF final página a página.
3. **PDF actual.** No lo he regenerado después de mejorar los pies de figura del MD. El PDF existente conserva la redacción en primera persona y las figuras, pero no los últimos pies. Si se usa el PDF, conviene regenerarlo desde el HTML actualizado.
4. **AEC1 como referencia.** Se cita en el texto como referencia de tono y créditos; no se copian sus datos ni sus conclusiones.

## Decisión

Para la entrega dejaría `memoria/informe.md` como fuente editable y generaría el PDF al final, con las figuras comprobadas. No volvería a tocar los CSV ni los parámetros: la parte técnica ya está cerrada.
