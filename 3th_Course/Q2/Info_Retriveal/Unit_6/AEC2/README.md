# AEC2 – Unidad 6: Análisis de Redes e Integración de LLMs

## Introducción

Esta entrega es la extensión final del proyecto de análisis de tweets sobre Bitcoin. Sobre el pipeline de las unidades anteriores (extracción de datos, limpieza, análisis de hashtags, LDA, análisis de sentimiento y resumen extractivo) se añaden dos nuevos módulos:

1. **Análisis de redes sociales con NetworkX** — construimos un grafo de interacciones a partir de las menciones en los tweets, calculamos métricas de centralidad y detectamos comunidades.
2. **Integración con LLM** — los insights del análisis de red se convierten en un prompt estructurado que se pasa a un modelo de lenguaje preentrenado (Gemma-2-2B-it en local, o la API de Gemini como fallback) para obtener una interpretación cualitativa de la red.

El enfoque sigue siendo el de una clase única y centralizada (`DataExtractor`) que encapsula todo el pipeline de principio a fin.

---

## Estructura del Proyecto

```
AEC2/
├── data_extractor.py            # Clase principal con todos los métodos del pipeline
├── AEC2_DataExtractor_U6.ipynb  # Notebook con ejemplos y demostraciones de U6
├── dashboard.py                 # Dashboard interactivo con Streamlit
├── requirements.txt             # Dependencias del proyecto
├── .env.example                 # Plantilla para RAPIDAPI_KEY y GEMINI_API_KEY
└── README.md                    # Este archivo
```

---

## Nuevos Métodos – Unidad 6

### `build_interaction_graph() → nx.DiGraph`

Construye un **dígrafo ponderado** de interacciones a partir de las menciones (@usuario) extraídas del texto de los tweets.

- Cada **nodo** representa un usuario (`user_name`).
- Cada **arista dirigida** A → B indica que el usuario A mencionó a B en al menos un tweet.
- El **peso** de la arista cuenta cuántas veces se produjo esa mención.

La elección de un dígrafo frente a un grafo no dirigido es deliberada: en Twitter la relación "mencionar" no es simétrica. Que @alice mencione a @bob no implica que @bob mencione a @alice, y esa asimetría es información relevante para identificar quién difunde y quién recibe.

```python
ext = DataExtractor(source='Bitcoin_tweets_dataset_2.csv')
ext.load_data()
G = ext.build_interaction_graph()
# [Graph] Nodes: 12,458  |  Edges: 8,234
```

---

### `analyze_network(G: nx.DiGraph) → dict`

Calcula cuatro métricas de centralidad sobre el grafo y detecta comunidades mediante el **algoritmo de Louvain**.

| Métrica | Interpretación |
|---|---|
| **In-degree centrality** | Usuarios más mencionados — popularidad por recepción |
| **Out-degree centrality** | Usuarios que más mencionan a otros — amplificadores o posibles bots |
| **Betweenness centrality** | Nodos puente entre sub-redes — intermediarios informativos clave |
| **PageRank** | Influencia propagada: pondera no solo cuántas menciones recibes sino de quién |

**Detección de comunidades:** usa `python-louvain` (algoritmo de Louvain), con fallback automático a `greedy_modularity_communities` de NetworkX si la librería no está instalada. El algoritmo de Louvain optimiza la modularidad del grafo agrupando nodos que interactúan más entre sí de lo esperado en una red aleatoria equivalente.

**Visualizaciones generadas** (`network_analysis.png`):
- Grafo de los 100 nodos con mayor PageRank, coloreado por comunidad.
- Distribución de in-degree (en redes sociales reales suele seguir una ley de potencia).

```python
metrics = ext.analyze_network(G)
# metrics['top_nodes']['pagerank']   → [(usuario, valor), ...]
# metrics['n_communities']           → int
# metrics['communities']             → {usuario: community_id, ...}
```

---

### `generate_prompt_from_network(G: nx.DiGraph) → str`

Extrae los insights más relevantes del grafo y los integra en un **prompt estructurado** listo para enviarse al LLM. Incluye:

- Estadísticas globales de la red (nodos, aristas, comunidades).
- Top-3 usuarios por PageRank (los más influyentes).
- Top-3 usuarios por betweenness (los intermediarios clave).
- Hashtag más frecuente del dataset.

El prompt pide al modelo:
1. Interpretar qué revela la estructura de la red sobre la comunidad Bitcoin en Twitter.
2. Especular sobre el perfil de los usuarios centrales (periodistas, influencers, bots).
3. Analizar qué sugiere el hashtag dominante sobre el sentimiento de la comunidad.
4. Proponer acciones de marketing o investigación basadas en la topología de la red.

```python
prompt = ext.generate_prompt_from_network(G)
```

La separación entre generación del prompt y ejecución del LLM es intencional: permite revisar y ajustar el prompt antes de enviarlo, y también reutilizarlo con distintos modelos.

---

### `chat_local_llm(prompt, model_name, max_new_tokens, temperature) → None`

Carga un **modelo LLM preentrenado desde HuggingFace** y abre una sesión de chat multi-turno interactiva en consola.

El modelo por defecto es `google/gemma-2-2b-it`. El enunciado menciona "gemma-4-E2B-it", que no existe como modelo público en HuggingFace; `gemma-2-2b-it` es el equivalente accesible (2B parámetros, instruction-tuned, misma familia).

**Flujo de ejecución:**
1. Si se pasa `prompt`, se genera una respuesta automática inicial que se incorpora al historial.
2. Se abre un bucle interactivo donde el usuario puede continuar la conversación.
3. Escribe `exit` para terminar la sesión.

**Gestión del contexto:** el historial se mantiene como lista de dicts `{role, content}`. En cada turno, todo el historial se re-tokeniza y se envía al modelo, lo que le permite "recordar" lo dicho anteriormente. Es la aproximación estándar para chat con modelos decoder-only.

**Formato de chat Gemma:** usa las etiquetas `<start_of_turn>user` / `<start_of_turn>model` específicas del formato de instrucción de Gemma. Otros modelos (LLaMA, Mistral) usan `[INST]...[/INST]`.

**Requisitos de hardware:**

| Entorno | Mínimo recomendado |
|---|---|
| GPU local (NVIDIA) | ≥ 6 GB VRAM |
| CPU sin GPU | ≥ 8 GB RAM (funciona pero lento) |
| Google Colab T4 | Suficiente, sin coste |

```python
ext.chat_local_llm(
    prompt=prompt,
    model_name='google/gemma-2-2b-it',
    max_new_tokens=512,
    temperature=0.7,
)
```

Modelos alternativos más ligeros si hay restricciones de memoria:
- `TinyLlama/TinyLlama-1.1B-Chat-v1.0` (~2.2 GB RAM)
- `microsoft/phi-2` (~5.5 GB RAM)

---

### `api_llm_fallback(prompt, model, api_key_env) → str`

Alternativa a `chat_local_llm()` para entornos sin GPU. Llama a la **API de Gemini** de Google AI Studio, que es gratuita hasta 15 peticiones/minuto.

La clave se lee de la variable de entorno `GEMINI_API_KEY` para no exponerla en el código ni subirla al repositorio.

```python
import os
os.environ['GEMINI_API_KEY'] = 'tu_clave_aqui'

response = ext.api_llm_fallback(
    prompt=prompt,
    model='gemini-1.5-flash',
)
```

Obtén tu clave gratuita en: https://aistudio.google.com/app/apikey

---

## Pipeline Completo U6

```
load_data()
    ↓
build_interaction_graph()          # DiGraph ponderado de menciones
    ↓
analyze_network(G)                 # métricas + comunidades + visualización
    ↓
generate_prompt_from_network(G)    # insights del grafo → prompt estructurado
    ↓
chat_local_llm(prompt)             # LLM local (Gemma-2-2B-it)
    o
api_llm_fallback(prompt)           # API Gemini (sin GPU)
```

---

## Decisiones de Diseño

**¿Por qué PageRank y no solo in-degree?**
In-degree cuenta menciones brutas, pero PageRank pondera por la importancia de quien te menciona. Ser mencionado por @CoinTelegraph tiene más peso que ser mencionado 100 veces por cuentas recién creadas. Es exactamente el razonamiento que aplica Google: no solo cuántos enlaces recibes, sino de quién.

**¿Por qué el algoritmo de Louvain para comunidades?**
Es el algoritmo de detección de comunidades más usado en redes sociales reales a gran escala. Optimiza la modularidad de forma eficiente y produce resultados interpretables. La modularidad mide qué tan bien separadas están las comunidades respecto a lo que se esperaría en una red aleatoria equivalente.

**¿Por qué Gemma-2-2B-it como modelo local?**
Es el modelo instruction-tuned de Google más accesible sin licencia especial. Sus 2B parámetros caben en la T4 gratuita de Google Colab. El sufijo `-it` (instruction-tuned) es crítico: los modelos base sin ajuste de instrucciones no siguen prompts de forma coherente.

**¿Por qué re-tokenizar todo el historial en cada turno?**
Los modelos decoder-only no tienen memoria entre llamadas. Re-tokenizar el historial completo en cada turno es la solución estándar para conversaciones multi-turno. El coste en latencia es asumible para sesiones cortas. Para sesiones largas habría que implementar sliding window o memoria externa (RAG).

**¿Por qué separar `generate_prompt_from_network` de `chat_local_llm`?**
La separación permite revisar y ajustar el prompt antes de enviarlo al modelo, y reutilizarlo con distintos backends (modelo local o API) sin duplicar lógica. También facilita el testing: se puede verificar la calidad del prompt de forma independiente.

---

## Instalación y Ejecución

### Dependencias

```bash
pip install pandas requests matplotlib wordcloud textblob gensim spacy nltk
pip install networkx python-louvain
pip install transformers torch accelerate
```

Para el dashboard:
```bash
pip install streamlit
```

### Variables de entorno

Crea un archivo `.env` (no lo subas al repositorio):
```
RAPIDAPI_KEY=tu_clave_rapidapi
GEMINI_API_KEY=tu_clave_gemini
```

### Ejecutar el notebook

```bash
jupyter notebook AEC2_DataExtractor_U6.ipynb
```

O abre el notebook directamente en Google Colab.

### Ejecutar el dashboard

```bash
streamlit run dashboard.py
```

---

## Fuentes de Datos

- **API en tiempo real**: [twitter-api45 en RapidAPI](https://rapidapi.com/alexanderxbx/api/twitter-api45)
- **Dataset estático**: [Bitcoin Tweets – Kaggle](https://www.kaggle.com/datasets/kaushiksuresh147/bitcoin-tweets)

---

## Referencias

- [NetworkX Documentation](https://networkx.org/documentation/stable/)
- [python-louvain (community detection)](https://python-louvain.readthedocs.io/)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers)
- [Google Gemma 2 Model Card](https://huggingface.co/google/gemma-2-2b-it)
- [Google AI Studio (Gemini API)](https://aistudio.google.com/)
- [Blondel et al. – Fast unfolding of communities in large networks (Louvain)](https://arxiv.org/abs/0803.0476)
- [Page et al. – The PageRank Citation Ranking (Stanford)](http://ilpubs.stanford.edu:8090/422/)
