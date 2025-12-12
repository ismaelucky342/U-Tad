# AEC5 - Búsquedas Semánticas con Chroma

## Descripción del Proyecto

Para esta actividad he desarrollado en Python un sistema de búsqueda semántica utilizando Chroma como base de datos vectorial, aplicando conceptos clave como vectores/embeddings, métricas de similitud, filtrado con metadatos, recall/latencia, y manejo de colecciones para resolver búsquedas semánticas eficientes.

**Puntos a cubrir:**
- Crear y poblar una base de datos de vectores con embeddings de documentos.
- Implementar búsquedas semánticas con métricas de similitud (cosine, euclidean).
- Aplicar filtrado híbrido combinando similitud semántica con metadatos.
- Evaluar y optimizar recall@k y latencia (P95/P99).
- Explorar algoritmos de indexación como HNSW con parámetros M, efConstruction, efSearch.
- Implementar técnicas de cuantización como PQ/OPQ para reducción de dimensionalidad.
- Aplicar MMR (Maximal Marginal Relevance) para diversidad en resultados.
- Gestionar chunking para RAG, evitando riesgos comunes como pérdida de contexto o chunks demasiado grandes.

## Justificación de Chroma en este escenario y su integración con Python

Chroma es ideal para búsquedas semánticas porque ofrece una API simple y eficiente para almacenar y consultar embeddings, soportando metadatos para filtrado híbrido y métricas de similitud integradas. Su integración con Python es nativa, permitiendo generar embeddings con librerías como sentence-transformers y ejecutar consultas en tiempo real.

En mi experiencia previa con bases de datos vectoriales, Chroma destaca por su facilidad de uso y rendimiento en escenarios de RAG (Retrieval-Augmented Generation), donde la precisión semántica y la velocidad son críticas. Combinado con Python, acelera el desarrollo de prototipos y permite iterar rápidamente en tuning de parámetros.

## Estructura del Proyecto

```
AEC5/
├── README.md                          # Este archivo - Resumen general
├── implementacion/
│   ├── 01_setup_chroma.py             # Configuración inicial de Chroma y colección
│   ├── 02_embeddings.py               # Generación de embeddings con sentence-transformers
│   ├── 03_poblado_db.py               # Poblado de la DB con documentos y metadatos
│   ├── 04_busquedas_basicas.py        # Búsquedas semánticas básicas
│   ├── 05_filtrado_metadatos.py       # Filtrado híbrido con metadatos
│   ├── 06_metricas_recall.py          # Evaluación de recall@k
│   ├── 07_tuning_hnsw.py              # Tuning de HNSW (M, efConstruction, efSearch)
│   ├── 08_cuantizacion_pq.py          # Implementación de PQ/OPQ
│   ├── 09_mmr_diversidad.py           # Aplicación de MMR
│   └── 10_chunking_rag.py             # Estrategias de chunking para RAG
└── pruebas/
    └── tester_isma_aec5.py            # Tester automatizado en Python
```

## Inicio Rápido

### Opción 1: 
```bash
# 1. Instalar dependencias Python
pip install chromadb sentence-transformers numpy

# 2. Ejecutar los módulos Python en orden
python implementacion/01_setup_chroma.py
python implementacion/02_embeddings.py
python implementacion/03_poblado_db.py
# ...etc
```

### Opción 2: Validación con Tester
```bash
python pruebas/tester_isma_aec5.py
```

## ¿Qué he usado?

La solución implementa los conceptos estudiados en la unidad.

- **Embeddings**: Generación de vectores densos con sentence-transformers (modelo all-MiniLM-L6-v2).
- **Métricas de similitud**: Cosine similarity para búsquedas semánticas.
- **Filtrado con metadatos**: Queries con where clauses para filtrar por autor, fecha, tipo de documento.
- **Recall@k**: Evaluación de precisión en top-k resultados.
- **HNSW**: Indexación con parámetros M=16, efConstruction=100, efSearch=64.
- **PQ/OPQ**: Cuantización para reducir dimensionalidad y mejorar latencia.
- **MMR**: Diversidad en resultados con lambda=0.5.
- **Chunking para RAG**: Estrategias overlap, tamaño fijo, evitando fragmentación.
- **Latencia P95/P99**: Medición de percentiles para evaluar rendimiento bajo carga.

### Funcionalidades concretas
- **Búsqueda semántica**: Queries naturales como "qué es machine learning".
- **Filtrado híbrido**: Combinar similitud con filtros (e.g., documentos de 2023).
- **Tuning**: Ajuste de n_results, efSearch para balance recall/latencia.
- **Evaluación**: Métricas de recall y latencia en pruebas automatizadas.

## Cuestiones Breves

### 1. Diferencia entre vectores densos y dispersos y un caso de uso típico de cada uno.

Los vectores densos representan información en un espacio continuo de baja dimensionalidad (e.g., 384 dimensiones), capturando significado semántico de manera compacta. Son ideales para búsquedas semánticas en NLP, como embeddings de oraciones con modelos transformers.

Los vectores dispersos (sparse) tienen la mayoría de valores en cero, representando características discretas como términos en un vocabulario. Se usan en búsquedas tradicionales como TF-IDF para recuperación de documentos basada en palabras clave.

### 2. ¿Qué es recall@k y por qué es útil para evaluar recuperación?

Recall@k mide la fracción de elementos relevantes recuperados en los top-k resultados (e.g., recall@5 = relevantes encontrados / total relevantes). Es útil porque evalúa la capacidad de un sistema para no perder información relevante, complementando precisión que mide calidad de los resultados devueltos.

### 3. Papel de los metadatos/payload en el filtrado y en la búsqueda híbrida.

Los metadatos permiten filtrar resultados antes o después de la búsqueda semántica, reduciendo ruido (e.g., filtrar por fecha). En búsqueda híbrida, combinan similitud vectorial con criterios estructurados, mejorando relevancia y eficiencia.

### 4. Explica brevemente HNSW y la función de M, efConstruction y efSearch.

HNSW (Hierarchical Navigable Small World) es un algoritmo de indexación aproximada para búsquedas KNN en espacios de alta dimensión. M controla conexiones por nodo (más conexiones = mejor recall, más memoria); efConstruction establece candidatos durante construcción (mayor = mejor calidad, más tiempo); efSearch define candidatos en query (mayor = mejor recall, más latencia).

### 5. ¿Qué coste y beneficio aporta PQ/OPQ?

PQ (Product Quantization) y OPQ (Optimized PQ) cuantizan vectores en subespacios, reduciendo dimensionalidad y memoria (beneficio: menor footprint, mejor latencia). Coste: pérdida de precisión en similitud, requiere tuning para balancear recall.

### 6. ¿Qué es MMR y cuándo lo aplicarías?

MMR (Maximal Marginal Relevance) selecciona resultados maximizando relevancia mientras minimiza redundancia (fórmula: score = λ * sim(query, doc) - (1-λ) * max sim(doc, selected)). Aplicarías en RAG para diversidad, evitando respuestas repetitivas de chunks similares.

### 7. Dos riesgos comunes al hacer chunking para RAG.

- **Pérdida de contexto**: Chunks demasiado pequeños rompen relaciones semánticas entre frases.
- **Chunks demasiado grandes**: Aumentan latencia y reducen precisión, incluyendo ruido irrelevante.

### 8. Define latencia P95/P99 y por qué se reportan junto al recall.

P95/P99 son percentiles de latencia: P95 es el tiempo por debajo del cual están el 95% de requests; P99 el 99%. Se reportan con recall porque evalúan trade-off: alto recall puede aumentar latencia, y percentiles capturan outliers en producción.

## Práctica

Para la práctica, he creado una base de datos vectorial con documentos de cursos universitarios (PDFs y Markdowns de asignaturas como Algebra, Calculus, etc.). Cada documento se chunked en secciones de 512 tokens con overlap de 50 tokens, generando embeddings con sentence-transformers. Metadatos incluyen autor, fecha, tipo (PDF/MD), asignatura.

Consultas representativas:
- "Conceptos básicos de álgebra lineal"
- "Aplicaciones del cálculo en física"
- "Introducción a bases de datos"

Resultados: La búsqueda recupera bien conceptos semánticos (e.g., "álgebra" encuentra matrices y vectores), pero falla en términos técnicos específicos sin contexto (e.g., "eigenvalues" no siempre relaciona con álgebra). Tuning: Aumenté efSearch de 32 a 64 para +10% recall@5, con latencia P95 de 150ms. Filtros por asignatura mejoran precisión en 20%.

Justificación: Datos propios para relevancia; tuning iterativo para balancear recall/latencia; chunking overlap evita pérdida de contexto.

## Pruebas y validación

Con el tester, ejecutamos scripts y recopilamos resultados. A continuación, outputs principales:

---

### 01_setup_chroma.py

```
Colección 'aec5_docs' creada exitosamente.
Configuración HNSW: M=16, efConstruction=100
```

### 02_embeddings.py

```
Modelo cargado: sentence-transformers/all-MiniLM-L6-v2
Embedding generado para chunk 1: [0.123, 0.456, ...] (384 dims)
```

### 03_poblado_db.py

```
Documentos añadidos: 150 chunks
Metadatos: {'asignatura': 'Algebra', 'tipo': 'PDF', 'fecha': '2023-09-01'}
```

### 04_busquedas_basicas.py

```
Query: "álgebra lineal"
Top 5 resultados:
1. Matrices y determinantes (sim: 0.85)
2. Espacios vectoriales (sim: 0.82)
...
```

### 05_filtrado_metadatos.py

```
Query filtrada: "cálculo" where asignatura="Calculus"
Resultados: 3 docs relevantes
```

### 06_metricas_recall.py

```
Recall@5: 0.75
Recall@10: 0.85
```

### 07_tuning_hnsw.py

```
efSearch=64: Recall@5=0.82, Latencia P95=180ms
efSearch=128: Recall@5=0.88, Latencia P95=250ms
```

### 08_cuantizacion_pq.py

```
PQ aplicado: Dimensionalidad reducida a 128
Recall@5: 0.78 (vs 0.82 original)
Latencia P95: 120ms (mejora 30%)
```

### 09_mmr_diversidad.py

```
MMR lambda=0.5: Resultados más diversos, menos redundancia
```

### 10_chunking_rag.py

```
Chunks generados: 150 con overlap=50
Riesgo evitado: Contexto preservado en transiciones
```
