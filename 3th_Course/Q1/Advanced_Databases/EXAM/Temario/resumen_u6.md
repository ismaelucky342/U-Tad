 # Parte Teórica - Bases de Datos Distribuidas / Cassandra (Unidad 6) — Resumen corto

## Definiciones clave

- **BBDD orientadas a columnas**: almacenan por columnas (optimizado para lecturas sobre pocas columnas, compresión eficiente).
- **Timestamp**: marca temporal asociada a operaciones; útil para resolución de conflictos y versiones.
- **Cassandra**: NoSQL column-family, descentralizada, tolerante a fallos y escalable horizontalmente.

## Idea central (resumen rápido)

Arquitectura descentralizada optimizada para escrituras intensivas y alta disponibilidad: los datos se particionan por clave, se replican y la consistencia es configurables por operación.

## Arquitectura mínima (chuleta)

- **Nodo**: instancia de Cassandra (puede actuar de coordinador para peticiones cliente).
- **Seed node**: punto de descubrimiento para nuevos nodos.
- **Partición**: unidad lógica derivada de la clave primaria; base de la distribución.
- **Token ring**: anillo lógico donde cada nodo posee un rango de tokens.
- **Particionador**: Murmur3 (equilibrado), Random, ByteOrdered (consultas por rango → cuidado con hotspots).

## Replicación y consistencia (chuleta)

- **Factor de replicación (RF)**: número de réplicas por partición.
- **Niveles de consistencia**: ONE, QUORUM, ALL (elegir según latencia vs consistencia deseada).
- **Mecanismos de tolerancia**: hinted handoff, read-repair, anti-entropy (repair) y nodos por DC/rack.

## Flujo simplificado de operación

1. Cliente → cualquier nodo (coordinador).
2. Coordinador calcula token/partición y localiza nodos responsables.
3. Ejecuta lectura/escritura en nodos responsables según RF y política de consistencia.

## Puntos prácticos que suelen preguntar

- **Escalado**: al añadir nodos hay que redistribuir tokens; planificar réplica por racks/DataCenters para tolerancia.
- **Elegir particionador**: Murmur3 = buena distribución; ByteOrdered = consultas por rangos (puede crear hotspots).
- **Casos de uso**: series temporales, telemetría, logs, métricas, cargas write-heavy, alta disponibilidad.

## Fallos típicos y consejos rápidos

- Monitorizar GC, compactions y latencias de disco; particiones calientes degradan el rendimiento.
- Elegir RF y nivel de consistencia acorde al SLA (ej.: RF=3 + QUORUM para balance entre disponibilidad y consistencia).

## Ejemplos rápidos (CQL / operaciones)

1) Crear Keyspace con estrategia de replicación simple:

```cql
CREATE KEYSPACE IF NOT EXISTS ks_demo
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '3'};
```

2) Crear tabla (modelo por consulta):

```cql
CREATE TABLE IF NOT EXISTS ks_demo.events (
	user_id text,
	event_time timestamp,
	event_type text,
	data text,
	PRIMARY KEY (user_id, event_time)
);
```

3) Insert y lectura con consistencia (cliente/cqlsh puede fijar CONSISTENCY):

```cql
INSERT INTO ks_demo.events (user_id, event_time, event_type, data)
VALUES ('u123', toTimestamp(now()), 'click', '{...}');

CONSISTENCY QUORUM;      -- en cqlsh o desde driver
SELECT * FROM ks_demo.events WHERE user_id='u123' LIMIT 10;
```

4) Comandos de administración útiles (nodo):

```
# nodetool status    -> ver estado del clúster
# nodetool repair    -> anti-entropy para arreglar réplicas
```

5) Nota práctica: para consultas por rango temporal, diseñar la PK/clustering keys que permitan reads eficientes (ej. partition by user_id, cluster by time).

Estos fragmentos funcionan como referencia rápida para lo que suelen pedir en ejercicios: crear keyspace/tabla, escribir/leer y entender replicación/consistencia.
