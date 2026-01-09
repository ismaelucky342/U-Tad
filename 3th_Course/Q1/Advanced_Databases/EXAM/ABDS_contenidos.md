# Ampliación de Bases de Datos (ABDS) — Resumen + modelos de examen

Este documento resume los contenidos de la asignatura y deja una guía clara de **cómo será el examen final** (según el mensaje del profesor). Al final del directorio `EXAM/` encontrarás además **exámenes modelo resueltos** para practicar.

## Estructura del examen (según el profesor)

En el examen final habrá:

- **Preguntas teóricas y prácticas**.
- **Teoría**:
	- **4 o 5 cuestiones breves** (tipo test / muy cortas, similares a las de las unidades).
	- El resto serán **preguntas cortas abiertas** sobre los contenidos, para desarrollar conocimiento (no “datos sueltos”, sino explicar conceptos).
	- Ejemplos de este estilo:
		- “¿Puedes describir brevemente las propiedades ACID?”
		- “Explica las diferencias entre los 2 tipos de escalado. Habla de rendimiento y coste económico.”
- **Práctica** (consulta/operaciones):
	- Alguna pregunta de **MongoDB**, **Redis** y **Neo4j** (consultas u operaciones).

Referencia recomendada por el profesor: **presentaciones de cada unidad** + este resumen.

## Índice rápido

- [Unidad 1 — BBDD NoSQL](#unidad-1--bbdd-nosql)
- [Unidad 2 — MongoDB (documentos)](#unidad-2--bbdd-orientadas-a-documentos-mongodb)
- [Unidad 3 — Redis (clave-valor)](#unidad-3--bbdd-orientadas-a-clave-valor-redis)
- [Unidad 4 — Neo4j (grafos)](#unidad-4--bbdd-orientadas-a-grafos-neo4j)
- [Unidad 5 — Chroma (vectores)](#unidad-5--bbdd-de-vectores-chroma)
- [Unidad 6 — Cassandra (distribuidas)](#unidad-6--bbdd-distribuidas-cassandra)

---

## Unidad 1 — BBDD NoSQL

- Tipos de datos (estructurados, semi-estructurados, no estructurados).
- Problemas y soluciones de las BBDD relacionales.
- Propiedades **ACID**.
- **Impedance Mismatch** / **(O)RM** (Object–Relational Mapping).
- Escalado **vertical** vs **horizontal** (rendimiento, disponibilidad, coste).
- Motivación del surgimiento de NoSQL.
- Clasificación de las BBDD NoSQL (documentos, clave-valor, grafos, columnas, etc.).

## Unidad 2 — BBDD orientadas a documentos. MongoDB

- Características básicas de las BBDD orientadas a documentos.
- Rendimiento y problemas de diseño (conocimiento básico).
	- Embedding vs referencing (cuándo conviene cada uno).
	- Índices (noción general).
- Manejo de operaciones CRUD:
	- Consultas (`find`, filtros, proyecciones, ordenación, limit/paginación).
	- Agregaciones (pipeline con `$match`, `$group`, `$project`, `$sort`, `$lookup`...).

## Unidad 3 — BBDD orientadas a clave-valor. Redis

- Características básicas:
	- Persistencia.
	- Clústeres.
	- Replicación.
- Casos de uso:
	- Como base de datos.
	- Como caché.
	- Como sistema de mensajería.
- Tipos de datos.
- Operaciones sobre tipos de datos:
	- Cadenas (strings).
	- Listas (lists).
	- Tablas hash (hashes).
	- Sets.
	- Sorted sets.
	- Bits / bitmaps.
	- Iteradores (`SCAN`, `HSCAN`, `SSCAN`, `ZSCAN`).
- **Pipelining**.
- Transacciones.
- Publicación y suscripción (pub/sub).
- Eviction Policies.

## Unidad 4 — BBDD orientadas a grafos. Neo4j

- Características básicas:
	- Nodos.
	- Relaciones.
	- Propiedades.
	- Etiquetas.
- Cypher:
	- Crear y actualizar nodos/relaciones.
	- Patrones (MATCH, WHERE, RETURN).
	- Consultas típicas (traversals, recomendaciones simples, contajes).
- Nociones sobre índices y restricciones.

## Unidad 5 — BBDD de vectores. Chroma

- Vectores y embeddings.
- Estructura y modelo de datos.
- Aplicaciones:
	- RAG.
	- Recomendación.
	- Deduplicación.
	- MMR.
- Búsquedas y familias de índices (visión general).
- Sintaxis básica de Chroma.

## Unidad 6 — BBDD distribuidas. Cassandra

- Características de Cassandra.
- Elementos:
	- Nodo, partición, rack, data center, clúster.
	- Nodo semilla y coordinador.
	- Token ring.
	- Nodos virtuales.
- Replicación.
- Niveles de consistencia.
- Write path flow y estructuras involucradas.
- Read path flow y estructuras involucradas.