# AEC3 Bases de Datos Avanzadas - REDIS

## Descripción del Proyecto

Para esta actividad he desarrollado en Python un sistema de gestión para una flota de transportes (autobuses, furgonetas, vans) similar a empresas como Hertz o Enterprise, usando Redis como base de datos principal y `redis-py` para la implementación de la lógica.

## Justificación de Redis

El uso de base de datos extremadamente rápida y flexible, perfecta para un sistema de gestión de flotas donde la inmediatez es fundamental. Redis trabaja en memoria, así que las operaciones son prácticamente instantáneas, lo que es ideal para consultas de disponibilidad, reservas o notificaciones en tiempo real.

Como hemos seguido en el temario redis ofrece estructuras de datos muy variadas (Strings, Hashes, Lists, Sets, Sorted Sets) que encajan perfectamente con las necesidades de modelar vehículos, reservas, sesiones, rankings y colas de mantenimiento. Gracias a los TTL, puedo gestionar datos temporales (como sesiones o reservas) sin preocuparme por limpiar manualmente, ya que expiran solos.

Redis también es muy fácil de desplegar y mantener, y su política de memoria (por ejemplo, allkeys-lru) me permite asegurar que los datos más importantes siempre estén disponibles, eliminando los menos usados cuando sea necesario. En resumen, Redis me da velocidad, flexibilidad y control total sobre los datos temporales y persistentes del sistema, todo en una sola herramienta.

## Estructura del Proyecto

```
AEC3/
├── README.md                          # Este archivo - Resumen general
├── implementacion/
│   ├── 01_vehiculos.py                # Gestión de vehículos (Strings, Hashes, Sets)
│   ├── 02_reservas.py                 # Sistema de reservas (Hashes con TTL)
│   ├── 03_sesiones.py                 # Gestión de sesiones (Strings con SETEX)
│   ├── 04_metricas.py                 # Contadores y estadísticas (INCR, Hashes)
│   ├── 05_rankings.py                 # Rankings dinámicos (Sorted Sets)
│   ├── 06_mantenimiento.py            # Colas de mantenimiento (Lists)
│   ├── 07_notificaciones.py           # Sistema Pub/Sub en tiempo real
│   ├── 08_transacciones.py            # MULTI/EXEC, WATCH, Pipelining
│   └── 09_cache_policies.py           # TTL, EXPIRE, Políticas de memoria
└── pruebas/
    └── tester_isma_aec3.py            # Tester automatizado en Python
```

## Inicio Rápido

### Opción 1: Demo Completa (Recomendado)
```bash
# 1. Iniciar Redis
redis-server

# 2. Instalar dependencias Python
pip install redis

# 3. Ejecutar los módulos Python en orden
python implementacion/01_vehiculos.py
python implementacion/02_reservas.py
python implementacion/03_sesiones.py
# ...etc
```

### Opción 2: Validación con Tester
```bash
python pruebas/tester_isma_aec3.py
```

## ¿Que he usado?

### Estructuras de Datos Redis
- **Strings**: Contadores, sesiones, flags, caché simple
- **Hashes**: Vehículos, reservas, métricas agrupadas
- **Lists**: Colas FIFO, historial, auditoría
- **Sets**: Índices, búsquedas, intersecciones
- **Sorted Sets**: Rankings, leaderboards, alertas por tiempo

### Funcionalidades concretas
- **Pub/Sub**: Notificaciones en tiempo real
- **Transacciones**: MULTI/EXEC para atomicidad
- **Watch**: Optimistic locking para concurrencia
- **TTL/Expiración**: Auto-limpieza de datos temporales
- **Pipelining**: Optimización de latencia de red
- **Políticas de Memoria**: allkeys-lru para gestión automática

---


## Escenarios Implementados

### Vehículos
- Registro con múltiples atributos (HASH)
- Búsqueda por tipo, ciudad, disponibilidad (SET)
- Caché de vehículos frecuentes (STRING con TTL)
- Contadores de disponibilidad (INCR/DECR)

### Reservas
- Creación con expiración automática (HASH + EXPIRE)
- Pre-reservas temporales (15 min TTL)
- Bloqueos de disponibilidad
- Historial persistente

### Sesiones
- Sesiones con auto-expiración (SETEX)
- Multi-dispositivo (SET de sesiones)
- Seguridad por timeout
- Auditoría de accesos (LIST)

### Métricas
- Contadores en tiempo real (INCR)
- Ingresos con decimales (INCRBYFLOAT)
- Métricas agrupadas por ciudad/tipo (HASH)
- Dashboard consolidado

### Rankings
- Vehículos más populares (ZSET)
- Clientes VIP por gasto (ZSET)
- Top por ingresos (ZSET)
- Múltiples rankings del mismo dato

### Mantenimiento
- Cola FIFO de mantenimiento (LIST)
- Priorización por urgencia (ZSET)
- Historial por vehículo (LIST + LTRIM)
- Tracking de mecánicos

### Notificaciones
- Notificaciones push (PUB/SUB)
- Canales temáticos (por rol, ciudad, usuario)
- Patterns con wildcard (PSUBSCRIBE)
- Chat en tiempo real

### Transacciones
- Reservas atómicas (MULTI/EXEC)
- Prevención de doble reserva (WATCH)
- Optimización con pipelining
- Consistencia de datos

### Caché
- Política LRU para memoria limitada
- TTL estratégicos por tipo
- Limpieza automática
- Warm-up de datos importantes
### Caché
- Política LRU para memoria limitada
- TTL estratégicos por tipo
- Limpieza automática
- Warm-up de datos importantes

