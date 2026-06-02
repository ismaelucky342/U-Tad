
# ===============================================================================
# EJERCICIO 5 (2 puntos) - STREAMING: VENTANAS Y SEMÁNTICA
# ===============================================================================
# 
# PARTE A: CÁLCULO DE VENTANAS (1 punto)
# Se reciben eventos de clicks en un sitio web cada 50-200ms.
# Los datos son: timestamp, usuario_id, página
# 
# Dados estos eventos (timestamp en segundos.milisegundos):
# Event 0: 10:00.050, user1, /home
# Event 1: 10:00.120, user2, /productos
# Event 2: 10:00.180, user1, /carrito
# Event 3: 10:00.450, user3, /pago
# Event 4: 10:00.890, user2, /checkout
# Event 5: 10:01.100, user1, /confirmacion
# Event 6: 10:01.350, user2, /factura
# Event 7: 10:01.900, user3, /gracias
# 
# Calcula cuántos clicks hay en cada ventana:
# a) Ventana Temporal (Tumbling): 1 segundo
# b) Ventana Deslizante (Sliding): 500ms cada 200ms
# c) Ventana de Sesión: con gap inactividad 300ms
# 
# PARTE B: SEMÁNTICA DE ENTREGA (1 punto)
# Para cada escenario, elige la semántica más apropiada y justifica:
# 
# B1) Sistema de contadores inteligentes (electricidad):
#     - At-most-once / At-least-once / Exactly-once
#     - ¿Por qué?
# 
# B2) Sistema de alertas de seguridad (detección de intrusos):
#     - At-most-once / At-least-once / Exactly-once
#     - ¿Por qué?
# 
# B3) Sistema de pagos en E-commerce:
#     - At-most-once / At-least-once / Exactly-once
#     - ¿Por qué?
# 

# apartado A:
# a) Ventana Temporal (Tumbling) de 1 segundo:
# Ventana 1 (10:00.000 - 10:00.999): Event 0, Event 1, Event 2, Event 3, Event 4 (5 clicks)
# Ventana 2 (10:01.000 - 10:01.999): Event 5, Event 6, Event 7 (3 clicks)

# b) Ventana Deslizante (Sliding) de 500ms cada 200ms:
# Ventana 1 (10:00.000 - 10:00.500): Event 0, Event 1, Event 2, Event 3 (4 clicks)
# Ventana 2 (10:00.200 - 10:00.700): Event 1, Event 2, Event 3, Event 4 (4 clicks)
# Ventana 3 (10:00.400 - 10:00.900): Event 3, Event 4 (2 clicks)
# Ventana 4 (10:00.600 - 10:01.100): Event 4, Event 5 (2 clicks)
# Ventana 5 (10:00.800 - 10:01.300): Event 5 (1 click)
# Ventana 6 (10:01.000 - 10:01.500): Event 5, Event 6 (2 clicks)
# Ventana 7 (10:01.200 - 10:01.700): Event 6 (1 click)

# c) Ventana de Sesión con gap de inactividad de 300ms:
# Sesión 1: Event 0, Event 1, Event 2, Event 3, Event 4 (5 clicks) - gap entre Event 4 y Event 5 es de 210ms, por lo que se cierra la sesión
# Sesión 2: Event 5, Event 6 (2 clicks) - gap entre Event 6 y Event 7 es de 550ms, por lo que se cierra la sesión
# Sesión 3: Event 7 (1 click)

# apartado B:
# B1) Sistema de contadores inteligentes (electricidad):
# Semántica recomendada: At-least-once
# Justificación: En este caso, es crucial que no se pierdan eventos de consumo, 
# incluso si eso significa que algunos eventos puedan ser procesados más de una vez. La pérdida de datos
# podría resultar en facturación incorrecta, por lo que es preferible tener duplicados que perder información.

# B2) Sistema de alertas de seguridad (detección de intrusos):
# Semántica recomendada: At-most-once
# Justificación: En un sistema de alertas de seguridad, es más importante evitar falsos positivos que perder
#  alguna alerta. Si se procesan eventos más de una vez, podría generar alertas innecesarias, lo que podría
# causar pánico o desensibilización. Por lo tanto, es preferible perder alguna alerta que generar demasiadas alertas falsas.     

# B3) Sistema de pagos en E-commerce:
# Semántica recomendada: Exactly-once
# Justificación: En un sistema de pagos, es fundamental que cada transacción se procese
# exactamente una vez para evitar cargos duplicados o pérdidas de pagos. La semántica de exactly-once 
# garantiza que cada evento de pago se procese una sola vez, lo que es esencial para la integridad financiera
# y la confianza del cliente.