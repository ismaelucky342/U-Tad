 # Parte Teórica - Bases de Datos de Vectores (Unidad 5) — Resumen corto

## Definiciones clave

- **Vector / embedding**: representación numérica (lista de floats) de un objeto (texto, imagen, audio) en un espacio continuo.
- **Dimensionalidad**: número de componentes (p. ej. 128D, 768D). Alta dimensionalidad = más representación, pero más coste.
- **Espacio métrico / métricas**: distancia Euclídea (L2), similitud coseno, producto interno; elegir según cómo se entrenó el embedding.
- **k‑NN**: recuperar los k vecinos más cercanos según la métrica.

## Idea central (resumen rápido)

Las bases de datos de vectores almacenan embeddings para permitir búsquedas por similitud (semántica). Se usan junto a índices vectoriales y, frecuentemente, con un índice léxico para cubrir casos exactos.

## Pipeline RAG / búsqueda semántica (chuleta)

1. **Chunking**: troceo (200–400 palabras, solape 15–20%), guardar `doc_id`, `chunk_id`, `título`, `lang`.
2. **Indexación**: índice vectorial (HNSW/IVF/ANN) + índice léxico (BM25) para híbrido.
3. **Recuperación**: prefiltrar por metadatos → recuperar top-N de ambos índices.
4. **Fusión y reranking**: normalizar scores, ponderar (ej. 0.4/0.6), aplicar cross-encoder/MMR sobre top-20.
5. **Generación**: pasar top-k (3–8) al modelo generativo.

## Búsqueda híbrida (chuleta)

- BM25: exactitud (códigos, fechas). Vectorial: sinónimos y contexto. Combinar para mejor recall/precision; normalizar scores antes de fusionar.

## Recomendación y deduplicación (chuleta)

- **Recomendación k‑NN**: recuperar vecinos en espacio embedding + reglas de negocio (precio, stock).
- **Cold‑start**: usar embeddings de contenido (texto/imagen) hasta tener señales de usuario.
- **Deduplicación**: umbral sobre distancia coseno/L2 → candidatos; inspección adicional o clustering para consolidar.

## Métricas rápidas y validación

- Recall@k, MRR, Precision@k, NDCG, cobertura. Validar con dataset etiquetado y pruebas A/B.

## Fallos típicos y consejos rápidos

- Normalizar embeddings (L2) cuando uses similitud coseno.
- Mantener coherencia entre cómo se generan embeddings (mismo modelo/preprocesado) y cómo se consultan.
- Guardar metadatos para filtrar antes de lanzar búsquedas vectoriales costosas.

## Ejemplos rápidos (chuleta)

1) Chunking simple (pseudo):

```
# dividir texto en chunks ~300 palabras con solape 20%
def chunk_text(text, size=300, overlap=60):
	chunks = []
	i = 0
	while i < len(text):
		chunks.append(text[i:i+size])
		i += size - overlap
	return chunks
```

2) Indexación y consulta (conceptual):

```
# generar embedding -> store vector in index (HNSW)
emb = model.encode(chunk)
index.add(id=chunk_id, vector=emb, metadata={doc_id,chunk_id})

# consulta híbrida
bm25_results = bm25.search(q, k=50)
vec_results  = hnsw.search(model.encode(q), k=50)
# fusionar: normalizar scores y ponderar (0.4 BM25 + 0.6 vector)
final = fuse(bm25_results, vec_results, weights=(0.4,0.6))
```

3) Ejemplo rápido FAISS / Python (esqueleto):

```
import faiss
idx = faiss.IndexHNSWFlat(d, 32)
idx.add(np.array(vectors).astype('float32'))
D, I = idx.search(query_vector, k)
```

4) Reorder/rerank (cross-encoder) — idea:

```
# aplicar cross-encoder solo sobre top-20 candidatos
ranked = cross_encoder.rank([(query, chunk_text) for chunk_text in top20])
```

Estos ejemplos son intencionalmente mínimos — sirven como chuleta para recordar pasos y comandos concretos que suelen pedirse en examen.
