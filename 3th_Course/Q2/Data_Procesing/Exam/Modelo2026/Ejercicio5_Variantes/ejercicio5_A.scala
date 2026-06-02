/*
Ejercicio 5_A - PROBLEMA CONCEPTUAL: VENTANAS EN STREAMING

CASO: Sistema de monitorización de velocidades en Fórmula 1

Un radar en un punto del circuito detecta velocidades de los pilotos.
Cada evento tiene: timestamp, DriverID, Speed

Datos (en m/s, timestamps en minutos:segundos.milisegundos):

| EventID | Time     | DriverID | Speed |
|---------|----------|----------|-------|
| 0       | 9:00.235 | 7        | 180   |
| 1       | 9:00.237 | 3        | 185   |
| 2       | 9:00.249 | 4        | 190   |
| 3       | 9:00.450 | 5        | 192   |
| 4       | 9:00.795 | 8        | 182   |
| 5       | 9:00.815 | 1        | 198   |
| 6       | 9:01.005 | 6        | 195   |
| 7       | 9:01.204 | 2        | 184   |
| 8       | 9:01.429 | 9        | 194   |
| 9       | 9:01.626 | 0        | 199   |

SE PIDE: Calcular el rango (Max - Min) de velocidades para CADA tipo de ventana.

---

PREGUNTA 1: Ventana Temporal (Tumbling) - cada 1 segundo

Los eventos se agrupan por segundos exactos, sin solapamiento.

Ventana [9:00.000 - 9:01.000):
  Contiene eventos: 0,1,2,3,4,5
  Velocidades: {180, 185, 190, 192, 182, 198}
  Max: 198
  Min: 180
  Range: 198 - 180 = 18

Ventana [9:01.000 - 9:02.000):
  Contiene eventos: 6,7,8,9
  Velocidades: {195, 184, 194, 199}
  Max: 199
  Min: 184
  Range: 199 - 184 = 15

RESPUESTA: 2 ventanas con ranges [18, 15]

---

PREGUNTA 2: Ventana por Conteo (Count-based) - cada 5 eventos

Agrupa exactamente 5 eventos, luego comienza nueva ventana.

Ventana 1 (eventos 0-4):
  Velocidades: {180, 185, 190, 192, 182}
  Max: 192
  Min: 180
  Range: 192 - 180 = 12

Ventana 2 (eventos 5-9):
  Velocidades: {198, 195, 184, 194, 199}
  Max: 199
  Min: 184
  Range: 199 - 184 = 15

RESPUESTA: 2 ventanas con ranges [12, 15]

---

PREGUNTA 3: Ventana Deslizante (Sliding) - tamaño 1000ms, avanza 200ms

La ventana se mueve cada 200ms pero incluye eventos en los últimos 1000ms.

¿Cuántas ventanas se generan?

Inicio en 9:00.000:
- W1: [9:00.000 - 9:01.000] → eventos 0,1,2,3,4,5 → Range = 18
- W2: [9:00.200 - 9:01.200] → eventos 0,1,2,3,4,5,6 → Range = 18
- W3: [9:00.400 - 9:01.400] → eventos 3,4,5,6,7 → Range = 16
- W4: [9:00.600 - 9:01.600] → eventos 4,5,6,7,8 → Range = 16
- W5: [9:00.800 - 9:01.800] → eventos 5,6,7,8,9 → Range = 15
- W6: [9:01.000 - 9:02.000] → eventos 6,7,8,9 → Range = 15

RESPUESTA: 6 ventanas con ranges [18, 18, 16, 16, 15, 15]

---

PREGUNTA 4: Ventana de Sesión - gap de inactividad 200ms

Se crea una nueva ventana cada vez que hay un hueco > 200ms entre eventos.

Análisis de diferencias entre timestamps consecutivos:
- 0→1: 2ms (< 200ms) → misma sesión
- 1→2: 12ms (< 200ms) → misma sesión
- 2→3: 201ms (> 200ms) → NUEVA SESIÓN ✓
- 3→4: 345ms (> 200ms) → NUEVA SESIÓN ✓
- 4→5: 20ms (< 200ms) → misma sesión
- 5→6: 190ms (< 200ms) → misma sesión
- 6→7: 199ms (< 200ms) → misma sesión
- 7→8: 225ms (> 200ms) → NUEVA SESIÓN ✓
- 8→9: 197ms (< 200ms) → misma sesión

Sesión 1 (eventos 0,1,2):
  Velocidades: {180, 185, 190}
  Range: 190 - 180 = 10

Sesión 2 (evento 3):
  Velocidades: {192}
  Range: 0

Sesión 3 (eventos 4,5,6,7):
  Velocidades: {182, 198, 195, 184}
  Range: 198 - 182 = 16

Sesión 4 (eventos 8,9):
  Velocidades: {194, 199}
  Range: 199 - 194 = 5

RESPUESTA: 4 sesiones con ranges [10, 0, 16, 5]

---

ANÁLISIS Y CONCLUSIONES:

Mistos datos, DIFERENTES resultados según ventana:

| Tipo Ventana | Num Ventanas | Ranges | Observación |
|--------------|--------------|--------|-------------|
| Tumbling | 2 | [18, 15] | Ventanas siempre del mismo tamaño |
| Count | 2 | [12, 15] | Agrupa por número de eventos |
| Sliding | 6 | [18,18,16,16,15,15] | Más ventanas, hay solapamiento |
| Session | 4 | [10, 0, 16, 5] | Depende de actividad real |

¿Cuándo usar cada una?

- TUMBLING: Reportes cada hora/día (exactitud temporal)
- COUNT: Procesar lotes de clientes (exactitud de volumen)
- SLIDING: Detección de anomalías (visibilidad de patrones)
- SESSION: Análisis de comportamiento usuario (sesiones reales)

*/

println("""
╔════════════════════════════════════════════════════════════════╗
║  EJERCICIO 5_A: CÁLCULOS DE VENTANAS EN SPARK STREAMING       ║
╚════════════════════════════════════════════════════════════════╝

TIPOS DE VENTANAS:
1. TUMBLING (Tumbada): No se solapan, avanzan en saltos fijos de tiempo
2. SLIDING (Deslizante): Se solapan, hay retrasos de procesamiento
3. SESSION: Dinámicas, basadas en inactividad entre eventos
4. COUNT-BASED: Basadas en número de eventos, no en tiempo

EJEMPLO RESUMEN:
Misma secuencia: 10 eventos de velocidad
├─ Tumbling [1s] → 2 ventanas distintas
├─ Sliding [1s, paso 0.2s] → 6 ventanas con solapamiento
├─ Session [gap 0.2s] → 4 sesiones de actividad
└─ Count [5 eventos] → 2 ventanas uniformes

REGLA PRÁCTICA:
- Reportes periódicos (diarios/horarios) → TUMBLING
- Análisis en tiempo real de eventos → SLIDING
- Detección de sesiones de usuario → SESSION
- Procesamiento en lotes exactos → COUNT

IMPORTANTE: La ventana que ELIJAS afecta dramáticamente los resultados.
""")
