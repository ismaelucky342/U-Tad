/*
Ejercicio 5_C - PROBLEMA CONCEPTUAL: ARQUITECTURAS STREAMING

ENUNCIADO:
Tienes un dataset histórico de 5 años de datos de ventas en HDFS.
Además, llegan eventos de ventas nuevas continuamente (100/seg).

Necesitas calcular: "Promedio de ventas diarias por categoría"

¿Cómo lo harías con Arquitectura LAMBDA?
¿Cómo lo harías con Arquitectura KAPPA?

---

ARQUITECTURA LAMBDA

Componentes:
1. BATCH LAYER: Procesa todos los datos históricos
2. SPEED LAYER: Procesa eventos en tiempo real
3. SERVING LAYER: Combina resultados

Implementación:

┌─────────────────────────────────┐
│ HDFS (5 años historicos)         │
└────────────────┬────────────────┘
                 │
           ┌─────▼──────┐
           │ BATCH LAYER│ (Spark Batch)
           │ Cron: 1/día│
           └─────┬──────┘
                 │
    ┌────────────▼────────────┐
    │ Promedio by categoria   │
    │ (5 años de datos)       │
    └────────────┬────────────┘
                 │
    ┌────────────▼────────────────────┐
    │      SERVING LAYER              │
    │  (Tablet de resultados)         │
    └────────────▲────────────────────┘
                 │
         ┌───────┴────────┐
         │                │
    ┌────▼────┐     ┌──────▼───┐
    │ SPEED   │     │  BATCH   │
    │ LAYER   │     │ RESULTS  │  
    └────┬────┘     └──────────┘
         │
    Kafka Stream
    (eventos nuevos 100/seg)
         │
    ┌────▼──────────────┐
    │Spark Streaming    │
    │Promedio últimas   │
    │24 horas           │
    └─────────────────┘

VENTAJAS:
✓ Precisión histórica (Batch Layer usa todos los datos)
✓ Baja latencia para datos nuevos (Speed Layer)
✓ Si algo falla, siempre hay un resultado anterior

DESVENTAJAS:
✗ Dos códigos distintos (batch + streaming)
✗ Más infraestructura
✗ Mantenimiento complejo

---

ARQUITECTURA KAPPA

Componentes:
1. LOG DISTRIBUIDO: Guarda TODOS los eventos (históricos + nuevos)
2. PROCESAMIENTO: Un único pipeline de streaming
3. ESTADO: Solo se procesa una vez de la forma correcta

Implementación:

┌──────────────────────────────────────┐
│ Kafka (5 años + eventos en tiempo real)│
│ (Re-procesable desde el inicio)       │
└──────────────┬───────────────────────┘
               │
       ┌───────▼────────┐
       │ SPARK STREAMING│(un único pipeline)
       │ Procesa TODOS  │
       │ los eventos    │
       └───────┬────────┘
               │
        ┌──────▼──────────┐
        │ Promedio by cat │
        │ (actualizado)   │
        └─────────────────┘

CÓMO RREPROCESAR TODO (si cambias la lógica):
1. Cambias el código de Spark Streaming
2. Buscas desde el offset 0 de Kafka
3. Reprocesas TODOS los eventos
4. Obtienes resultados nuevos

VENTAJAS:
✓ Solo un código (no hay batch+streaming)
✓ Lógica unificada
✓ Más simple de mantener
✓ Si cambias algoritmo, simplemente reprocesas

DESVENTAJAS:
✗ Kafka debe guardar años de datos (storage)
✗ Reprocesar todo es costoso
✗ Latencia inicial si hay mucho histórico

---

COMPARATIVA

| Aspecto | LAMBDA | KAPPA |
|---------|--------|-------|
| Complejidad | Alta | Media |
| Código | Duplicado (batch+stream) | Unificado |
| Latencia | Baja | Baja |
| Storage | Normal | Alto (guarda todo) |
| Reprocessing | Difícil | Fácil |
| Mantenimiento | Complejo | Simple |
| Tolerancia a fallos | Media | Alta |

---

PREGUNTAS:

1. ¿En qué caso preferirías LAMBDA?
   R: Cuando querés mantener batch y streaming separados,
      o cuando Kafka storage es prohibitivamente caro.

2. ¿Cuándo preferirías KAPPA?
   R: Cuando quieres uno código, y storage en Kafka es viable.
      Prácticamente siempre (hoy en día Kafka es barato).

3. Para ventas, ¿cuál elegirías?
   R: KAPPA. Un pipeline unificado es más simple.
      Si necesitas reajustar el promedio, simplemente reprocesas.

*/

println("""
╔════════════════════════════════════════════════════════════════╗
║  EJERCICIO 5_C: LAMBDA vs KAPPA - ARQUITECTURAS               ║
╚════════════════════════════════════════════════════════════════╝

LAMBDA = Batch + Streaming (dos vías)
KAPPA = Solo Streaming (una vía)

TENDENCIA ACTUAL:
KAPPA está ganando porque Kafka y storage distribuido son baratos.

CASOS ESPECÍFICOS:
- Twitter trending: KAPPA (streaming puro)
- Análisis histórico: LAMBDA tradicional
- Ventas en tiempo real: KAPPA
- Recomendaciones personalizadas: LAMBDA (necesita ML batch)
""")
