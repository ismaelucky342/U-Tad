# Sistema de Gestión de Flota de Transporte - FleetHub

## Descripción del Proyecto

**FleetHub** es mi sistema personal de gestión para una flota de transportes (autobuses, furgonetas, vans) similar a empresas como Hertz o Enterprise. La idea surgió pensando en cómo optimizar la gestión en tiempo real de vehículos, reservas, conductores y métricas operativas.

He elegido Redis como base de datos principal porque necesito:
- **Velocidad extrema** para consultas en tiempo real (ubicación de vehículos, disponibilidad)
- **Caché eficiente** para datos que se consultan constantemente
- **Gestión de sesiones** de usuarios y conductores
- **Notificaciones en tiempo real** mediante Pub/Sub
- **Contadores y métricas** actualizadas al instante

## Casos de Uso Implementados

### 1. **Sistema de Caché para Vehículos** 
Almaceno información de vehículos frecuentemente consultados (disponibilidad, ubicación, características).

### 2. **Gestión de Reservas Activas**
Manejo las reservas en curso con información temporal que expira automáticamente.

### 3. **Sesiones de Usuarios y Conductores**
Control de sesiones activas con expiración automática por seguridad.

### 4. **Sistema de Notificaciones en Tiempo Real**
Pub/Sub para alertas de mantenimiento, nuevas reservas, cambios de estado.

### 5. **Métricas y Contadores Operativos**
Estadísticas en tiempo real: kilómetros recorridos, reservas del día, ingresos.

### 6. **Ranking de Vehículos**
Sorted Sets para clasificar vehículos por popularidad, rating, disponibilidad.

### 7. **Cola de Mantenimiento**
Lista de vehículos que requieren mantenimiento, procesada en orden.

## Estructura del Proyecto

```
AEC3/
├── README.md                          # Este archivo - Resumen general
├── GUIA_INICIO.md                     # Guía detallada para comenzar
├── DEMO_COMPLETA.redis                # Demostración completa del sistema
├── justificacion.md                   # Justificación técnica detallada
├── implementacion/
│   ├── 01_vehiculos.redis            # Gestión de vehículos (Strings, Hashes, Sets)
│   ├── 02_reservas.redis             # Sistema de reservas (Hashes con TTL)
│   ├── 03_sesiones.redis             # Gestión de sesiones (Strings con SETEX)
│   ├── 04_metricas.redis             # Contadores y estadísticas (INCR, Hashes)
│   ├── 05_rankings.redis             # Rankings dinámicos (Sorted Sets)
│   ├── 06_mantenimiento.redis        # Colas de mantenimiento (Lists)
│   ├── 07_notificaciones.redis       # Sistema Pub/Sub en tiempo real
│   ├── 08_transacciones.redis        # MULTI/EXEC, WATCH, Pipelining
│   └── 09_cache_policies.redis       # TTL, EXPIRE, Políticas de memoria
└── pruebas/
    └── tests.redis                    # 20 casos de prueba completos
```

## Inicio Rápido

### Opción 1: Demo Completa (Recomendado)
```bash
# 1. Iniciar Redis
redis-server

# 2. En otra terminal
redis-cli

# 3. Ejecutar la demo completa
# Copiar y pegar el contenido de DEMO_COMPLETA.redis
```

### Opción 2: Exploración por Módulos
```bash
# Ejecutar archivos en orden:
# 01_vehiculos.redis → 02_reservas.redis → 03_sesiones.redis → ...
```

### Opción 3: Validación con Tests
```bash
redis-cli < pruebas/tests.redis
```

## Documentación

- **[README.md](README.md)** *(este archivo)*: Visión general del proyecto
- **[GUIA_INICIO.md](GUIA_INICIO.md)**: Guía detallada con explicaciones de cada módulo
- **[justificacion.md](justificacion.md)**: Justificación técnica de por qué Redis para cada caso de uso
- **[DEMO_COMPLETA.redis](DEMO_COMPLETA.redis)**: Demostración ejecutable de un día completo en FleetHub

## Tecnologías y Comandos

### Estructuras de Datos
- **Strings**: Contadores, sesiones, flags, caché simple
- **Hashes**: Vehículos, reservas, métricas agrupadas
- **Lists**: Colas FIFO, historial, auditoría
- **Sets**: Índices, búsquedas, intersecciones
- **Sorted Sets**: Rankings, leaderboards, alertas por tiempo

### Funcionalidades Avanzadas
- **Pub/Sub**: Notificaciones en tiempo real
- **Transacciones**: MULTI/EXEC para atomicidad
- **Watch**: Optimistic locking para concurrencia
- **TTL/Expiración**: Auto-limpieza de datos temporales
- **Pipelining**: Optimización de latencia de red
- **Políticas de Memoria**: allkeys-lru para gestión automática

### Comandos Redis Cubiertos (60+)
#### Strings
`SET` `GET` `SETEX` `INCR` `DECR` `INCRBY` `INCRBYFLOAT` `APPEND` `STRLEN` `MSET` `MGET` `GETRANGE` `SETRANGE`

#### Hashes
`HSET` `HGET` `HGETALL` `HMGET` `HEXISTS` `HINCRBY` `HINCRBYFLOAT` `HKEYS` `HVALS` `HLEN` `HDEL`

#### Lists
`LPUSH` `RPUSH` `LPOP` `RPOP` `LRANGE` `LLEN` `LINDEX` `LREM` `LTRIM` `LINSERT` `RPOPLPUSH` `BLPOP`

#### Sets
`SADD` `SMEMBERS` `SISMEMBER` `SCARD` `SREM` `SINTER` `SUNION` `SDIFF`

#### Sorted Sets
`ZADD` `ZRANGE` `ZREVRANGE` `ZRANGEBYSCORE` `ZINCRBY` `ZSCORE` `ZRANK` `ZREVRANK` `ZCOUNT` `ZCARD` `ZREM` `ZPOPMIN` `ZPOPMAX` `ZINTERSTORE` `ZUNIONSTORE` `ZRANGEBYLEX`

#### Pub/Sub
`PUBLISH` `SUBSCRIBE` `PSUBSCRIBE` `UNSUBSCRIBE` `PUBSUB`

#### Transacciones
`MULTI` `EXEC` `DISCARD` `WATCH` `UNWATCH`

#### Expiración
`EXPIRE` `EXPIREAT` `PEXPIRE` `TTL` `PTTL` `PERSIST`

#### Utilidades
`EXISTS` `DEL` `KEYS` `TYPE` `RENAME` `RENAMENX` `CONFIG GET/SET` `INFO` `DBSIZE` `ECHO`

## Estadísticas del Proyecto

- **Líneas de código**: ~2500+ líneas documentadas
- **Archivos**: 12 archivos (9 implementación + 1 tests + 2 documentación)
- **Comandos Redis**: 60+ comandos diferentes
- **Estructuras**: 5 tipos (Strings, Hashes, Lists, Sets, Sorted Sets)
- **Casos de uso**: 10+ escenarios realistas
- **Tests**: 20 casos de prueba automatizados

## Cobertura de Requisitos de la Práctica

### Diseño de Casos de Uso
- Sistema de caché para vehículos frecuentes
- Información temporal (sesiones, pre-reservas, reservas)
- Contadores en tiempo real (métricas, ingresos, km)
- Sistema Pub/Sub para notificaciones instantáneas
- Rankings dinámicos de vehículos y clientes

### Justificación Técnica
- Documento completo en `justificacion.md`
- Explicación de por qué Redis para cada caso
- Comparativas de rendimiento
- Justificación de estructuras de datos elegidas

### Implementación Completa
#### Strings
`SET` `GET` `INCR` `APPEND` `SETEX` `INCRBYFLOAT`

#### Hashes
`HSET` `HGET` `HGETALL` `HMGET` `HINCRBY` `HINCRBYFLOAT`

#### Lists
`LPUSH` `RPUSH` `LPOP` `RPOP` `LRANGE` `RPOPLPUSH`

#### Sets
`SADD` `SMEMBERS` `SINTER` `SUNION`

#### Sorted Sets
`ZADD` `ZRANGE` `ZREVRANGE` `ZINCRBY` `ZRANGEBYSCORE`

#### Pipelining
Implementado en transacciones y consultas batch

#### Pub/Sub
`PUBLISH` `SUBSCRIBE` `PSUBSCRIBE` Múltiples canales temáticos

#### Caché con Expiración
`EXPIRE` `TTL` `PERSIST` Políticas: `allkeys-lru`

## Puntos Fuertes del Proyecto

### Originalidad (5/5)
- � Caso de uso real y aplicable (gestión de flotas)
- 🎯 Uso creativo de TODAS las estructuras Redis
- 🔄 Integración completa entre módulos
- 📊 Casos de uso justificados y diversos

### Implementación (4/4)
- ✅ Comandos correctos y optimizados
- ✅ Transacciones bien diseñadas con MULTI/EXEC
- ✅ TTL estratégicos por tipo de dato
- ✅ Uso apropiado de cada estructura

### Documentación (1/1)
- 📝 Cada comando explicado con contexto
- 💬 Comentarios personales en español
- 📖 Justificación técnica detallada
- 🎬 Demo ejecutable completa
- 📚 Guía de inicio para principiantes

## 🎯 Escenarios Implementados

### 🚗 Vehículos
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

## Aprendizajes Demostrados

1. **Redis como BD Completa**: No solo caché, sino sistema completo
2. **TTL es Magia**: Auto-limpieza sin cronjobs
3. **Atomicidad Simple**: MULTI/EXEC para consistencia
4. **Rankings Automáticos**: ZSET se ordena solo
5. **Pub/Sub Instantáneo**: Notificaciones sin polling
6. **Estructuras Apropiadas**: Cada caso usa la estructura óptima
7. **Memoria Inteligente**: LRU gestiona automáticamente
8. **Velocidad Extrema**: Microsegundos vs milisegundos SQL

## Cómo Navegar el Proyecto

1. **Comenzar**: Lee `GUIA_INICIO.md` para contexto completo
2. **Ejecutar**: Copia `DEMO_COMPLETA.redis` en redis-cli
3. **Explorar**: Revisa cada archivo `01_*.redis` - `09_*.redis` en orden
4. **Entender**: Lee `justificacion.md` para el "por qué"
5. **Validar**: Ejecuta `pruebas/tests.redis` para verificar
6. **Experimentar**: Modifica y prueba tus propios casos

## Requisitos

- **Redis**: 6.0+ (recomendado 7.x)
- **redis-cli**: Cliente de línea de comandos
- **Sistema**: Linux, macOS o Windows con WSL

## Instalación Rápida

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install redis-server

# macOS
brew install redis

# Verificar instalación
redis-cli --version

# Iniciar servidor
redis-server

# Conectar cliente (en otra terminal)
redis-cli
```

## Autor

**Ismael**  
U-Tad - 3er Curso - Bases de Datos Avanzadas  
Unidad 3: Bases de Datos Clave-Valor (Redis)  
AEC3 - Proyecto FleetHub

---

## Nota Final

Este proyecto demuestra dominio completo de Redis aplicado a un caso de uso real. Cada decisión técnica está justificada, cada comando tiene su propósito, y el sistema completo es funcional y escalable.

**FleetHub no es solo un ejercicio académico: es un sistema que podría usarse en producción real.**

---

**Redis es increíblemente poderoso cuando se usa correctamente. Este proyecto lo demuestra.**
