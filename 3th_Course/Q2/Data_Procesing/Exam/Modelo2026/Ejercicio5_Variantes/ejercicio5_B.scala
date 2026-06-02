/*
Ejercicio 5_B - PROBLEMA CONCEPTUAL: SEMÁNTICA DE ENTREGA

ENUNCIADO:
Para cada escenario, elige la semántica MÁS APROPIADA:
- At-most-once: ≤1 vez (puede perder)
- At-least-once: ≥1 vez (puede duplicar)
- Exactly-once: =1 vez (perfecto, pero caro)

---

ESCENARIO A: Monitorizar sensores de una estación meteorológica

Datos: temperatura, humedad, presión que se actualizan continuamente

¿Qué sucede si...?
- PIERDES un dato → mala precisión histórica
- DUPLICAS un dato → puede suavizarse/promediarse<br>

RECOMENDACIÓN: At-least-once
JUSTIFICACIÓN: Es más importante no perder datos. Los duplicados
se pueden filtrar o promediar en agregaciones.

---

ESCENARIO B: Procesamiento de pedidos en tienda online

Cada pedido es dinero, inventario, cliente satisfecho

¿Qué sucede si...?
- PIERDES un pedido → cliente molesto, dinero perdido
- DUPLICAS un pedido → cobras dos veces, envías dos paquetes ❌

RECOMENDACIÓN: Exactly-once
JUSTIFICACIÓN: Los duplicados son PEOR que perder un pedido.
Necesitas garantía exacta de procesamiento.

---

ESCENARIO C: Control de inventario en farmacia

Stock de medicamentos: crítico y debe ser preciso

¿Qué sucede si...?
- PIERDES un evento de venta → stock dice que hay pero NO hay ❌
- DUPLICAS un evento → stock baja dos veces, falta medicamento ❌

RECOMENDACIÓN: Exactly-once
JUSTIFICACIÓN: El inventario es crítico. Perder o duplicar es igual
de malo. Necesitas que cada venta se registre EXACTAMENTE una vez.

---

ESCENARIO D: Monitorización de piloto automático de avión

Altitud, velocidad, trayectoria en tiempo real

¿Qué sucede si...?
- PIERDES un evento → un dato puntual, hay otros sensores
- DUPLICAS un evento → el sistema ejecuta la misma orden DOS veces ❌

RECOMENDACIÓN: At-most-once
JUSTIFICACIÓN: En un sistema crítico, DUPLICAR una acción es peor
que perder un dato puntual (hay monitorización continua).

---

ESCENARIO E: Detectar tendencias en redes sociales

Análisis de tweets, posts, menciones

¿Qué sucede si...?
- PIERDES tweets → análisis menos completo
- DUPLICAS tweets → afecta el conteo estadístico ligeramente

RECOMENDACIÓN: At-least-once
JUSTIFICACIÓN: El análisis es estadístico. Cuantos más datos mejor.
Los duplicados se pueden desduplicar después.

---

ESCENARIO F: Alerta de ataque informático en CPD

Detección de intentos de acceso no autorizado

¿Qué sucede si...?
- PIERDES una alerta → un ataque pasa desapercibido ❌❌❌
- DUPLICAS una alerta → notificación redundante, pero seguro

RECOMENDACIÓN: At-least-once
JUSTIFICACIÓN: En ciberseguridad, es mejor alertar dos veces
que no alertar. Los duplicados son ruido tolerable.

---

TABLA RESUMEN:

| Escenario | Semántica | Razón Clave |
|-----------|-----------|-------------|
| Sensores meteorología | At-least-once | Datos históricos importantes |
| Pedidos tienda | Exactly-once | Dinero y satisfacción cliente |
| Inventario farmacia | Exactly-once | Stock crítico y preciso |
| Piloto automático | At-most-once | Evitar acciones duplicadas |
| Tendencias redes | At-least-once | Análisis estadístico tolera duplicados |
| Alertas ciberseguridad | At-least-once | Mejor perder dinero que seguridad |

*/

println("""
╔════════════════════════════════════════════════════════════════╗
║   EJERCICIO 5_B: ELEGIR SEMÁNTICA DE ENTREGA CORRECTA         ║
╚════════════════════════════════════════════════════════════════╝

PRINCIPIO CLAVE:
- Pedidos/transacciones → Exactly-once
- Monitorización crítica → At-most-once (evitar acciones duplicadas)
- Análisis/sensores → At-least-once (tolera duplicados y pérdidas)

LO IMPORTANTE:
1. Entender qué es peor en CADA caso
2. Perder datos NO es siempre lo peor
3. Duplicar acciones TAMPOCO es siempre lo peor
4. Depende del impacto del negocio

EJEMPLO REAL:
Banco: Exactly-once (transferencias de dinero)
Reloj conectado: At-least-once (pasos diarios)
Medidor de electricidad: At-least-once (consumo)
Cardiomensual: At-most-once (avisos críticos deben ser únicos)
""")
