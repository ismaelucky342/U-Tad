# AEC3 – Unidad 6: Análisis de Redes Sociales y Modelos de Lenguaje

## Introducción

En esta última entrega, amplio el pipeline de las unidades anteriores (extracción de datos desde API, limpieza, análisis de hashtags, LDA, sentimiento, resumen) con dos ejes nuevos que cierren el proyecto:

1. **Análisis de redes sociales con NetworkX** — Construyo un grafo de interacciones a partir de las menciones (@usuario) en los tweets. Luego calculo métricas de centralidad (in-degree, out-degree, betweenness, PageRank) y detecto comunidades con el algoritmo de Louvain.

2. **Integración con LLM** — Los insights extraídos del análisis de red (top usuarios, hashtag dominante, número de comunidades) se integran en un prompt estructurado que se pasa a un modelo preentrenado en local (TinyLlama/Gemma por defecto, con fallback a API Gemini si no hay GPU).

El proyecto mantiene el mismo enfoque que la U4: una clase centralizada `DataExtractor` que encapsula todo el pipeline. He refactorizado el código en módulos separados (`core/loader.py`, `core/cleaner.py`, `core/network.py`, `core/llm.py`, etc.) para que sea más escalable y mantenible, pero la interfaz pública sigue siendo la misma.

---

## Estructura del Proyecto

```
Unit_6/AEC3/
├── core/                          # Módulos especializados
│   ├── __init__.py                # Exporta DataExtractor
│   ├── extractor.py               # DataExtractor (orquestación)
│   ├── loader.py                  # DataLoader (ingesta)
│   ├── cleaner.py                 # TextCleaner (normalización)
│   ├── analyzer.py                # NLPAnalyzer (sentiment, topics)
│   ├── network.py                 # NetworkAnalyzer (grafos)
│   └── llm.py                     # LLMHandler (LLM local + API)
├── utils/                         # Utilidades compartidas
│   ├── __init__.py
│   └── constants.py               # Regex y constantes globales
├── datasets/                      # Datos de entrada (CSV, JSON)
│   └── .gitkeep
├── outputs/                       # Resultados: grafos, logs, imágenes
│   └── .gitkeep
├── data_extractor.py              # Wrapper compatibilidad (reexporta core)
├── main.py                        # CLI con ArgumentParser
├── dashboard.py                   # Streamlit UI
├── AEC3_DataExtractor_U6.ipynb    # Notebook con ejemplos
├── requirements.txt               # pip install -r requirements.txt
├── .env.example                   # Template de variables de entorno
└── README.md                      # Este archivo
```

---

## Métodos Nuevos – Unit 6

### `build_interaction_graph()` 

Construyo un **grafo dirigido ponderado** a partir de las menciones (@usuario) en los tweets. Cada nodo es un usuario, cada arista dirigida A → B significa que A mencionó a B, y el peso cuenta cuántas veces se produjo esa mención.

Elegí un dígrafo en lugar de un grafo no dirigido porque en Twitter la mención no es simétrica. Que @alice mencione a @bob dice algo diferente a que @bob mencione a @alice, y esa asimetría es crucial para identificar quién amplifica y quién recibe.

```python
ext = DataExtractor(source='Bitcoin_tweets_dataset_2.csv')
ext.load_data()
G = ext.build_interaction_graph()
# [Graph] Nodes: 12,458  |  Edges: 8,234
```

---

### `analyze_network()`

Calculo cuatro métricas de centralidad y detecto comunidades con Louvain:

| Métrica | Qué mide |
|---|---|
| **In-degree** | Quién es más mencionado (popularidad por recepción) |
| **Out-degree** | Quién menciona a más gente (amplificadores o bots) |
| **Betweenness** | Quién es puente entre sub-redes (intermediarios informativos) |
| **PageRank** | Influencia propagada (no solo cuánto recibo, sino de quién) |

PageRank es interesante porque ser mencionado por @CoinTelegraph pesa más que 100 menciones de cuentas recién creadas. Es exactamente el razonamiento que aplica Google para ranquear sitios web.

El algoritmo de Louvain optimiza la modularidad del grafo, agrupando usuarios que interactúan más entre sí de lo esperado en una red aleatoria equivalente. Genera comunidades interpretables y funciona bien en redes reales grandes.

Genero dos visualizaciones (`network_graph.png`):
- El grafo de los 100 nodos con mayor PageRank, coloreado por comunidad
- Distribución de in-degree (suele ser una ley de potencia en redes sociales)

```python
metrics = ext.analyze_network(G)
# metrics['top_nodes']['pagerank']   → top 3 usuarios más influyentes
# metrics['n_communities']           → número de comunidades detectadas
```

---

### `generate_prompt_from_network()`

Extraigo los insights más relevantes del grafo en un prompt estructurado para el LLM. El prompt incluye:

- Estadísticas globales (nodos, aristas, comunidades, densidad)
- Top-3 usuarios por PageRank
- Top-3 usuarios por betweenness
- Hashtag más frecuente del dataset

Luego pido al modelo que:
1. Interprete qué revela la estructura de la red sobre la comunidad Bitcoin
2. Especule sobre el perfil de los usuarios centrales (¿periodistas, influencers, bots?)
3. Analice qué sugiere el hashtag dominante sobre el sentimiento
4. Proponga acciones de marketing/investigación basadas en la topología

Separo deliberadamente la generación del prompt de la ejecución del LLM. Esto permite revisar el prompt antes de enviarlo, y reutilizarlo con distintos modelos.

```python
prompt = ext.generate_prompt_from_network(G)
print(prompt)  # Revisar antes de pasar al LLM
```

---

### `chat_local_llm()`

Cargo un modelo LLM preentrenado desde HuggingFace y abro una sesión de chat interactivo multi-turno.

Por defecto uso **TinyLlama-1.1B** porque:
- ✅ Corre en CPU con ~4GB de RAM o GPU modesta
- ✅ Instruction-tuned (sigue prompts coherentemente)
- ✅ Gratuito, sin licencias especiales

El flujo es:
1. Si paso un `prompt`, genera una respuesta inicial automática
2. Se abre un bucle interactivo donde puedo continuar la conversación
3. Escrito `exit` para terminar

El historial se mantiene como lista de dicts `{role, content}`. En cada turno re-tokenizo todo el historial y lo envío al modelo, lo que le permite "recordar" lo anterior. Es la aproximación estándar para decoder-only LLMs.

```python
ext.chat_local_llm(
    prompt=prompt,
    model_name='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    max_new_tokens=512,
    temperature=0.7
)
```

**Alternativas si tengo más VRAM:**
- `google/gemma-2-2b-it` (2B, mejor calidad que TinyLlama)
- `meta-llama/Llama-2-7b-chat-hf` (7B, mucho mejor pero necesita ~16GB)

**Requisitos de hardware:**
- Con GPU ≥6GB VRAM: corre rápido
- Solo CPU: funciona pero tarda ~10s por token
- Google Colab T4: suficiente para TinyLlama

---

### `api_llm_fallback()`

Alternativa a `chat_local_llm()` para entornos sin GPU. Uso la API de Gemini de Google AI Studio (gratuita hasta 15 req/min).

La clave se lee de `GEMINI_API_KEY` env var para no exponerla en código.

```python
response = ext.api_llm_fallback(prompt=prompt)
```

Obtén clave gratuita en: https://aistudio.google.com/app/apikey

---

## Pipeline Completo

```
load_data()
    ↓
build_interaction_graph()          # DiGraph ponderado de menciones
    ↓
analyze_network(G)                 # métricas + comunidades + visualización
    ↓
generate_prompt_from_network(G)    # insights del grafo → prompt estructurado
    ↓
chat_local_llm(prompt)             # LLM local (TinyLlama o Gemma-2-2B)
    o
api_llm_fallback(prompt)           # API Gemini (sin GPU)
```

---

## Decisiones de Diseño

### ¿Por qué modular y no monolítico?

En versiones anteriores (Unit 4) la clase `DataExtractor` tenía 827 líneas. Mantener todo en un archivo dificulta:
- Localizar bugs (¿está el error en cargar datos o en tokenizar?)
- Probar cada parte aisladamente
- Reutilizar módulos en otros proyectos
- Cambiar una función sin romper otras

Decidí dividir en **6 módulos especializados**:

| Módulo | Responsabilidad | Clases |
|---|---|---|
| `loader.py` | Ingesta de datos (API, CSV, JSON) | `DataLoader` |
| `cleaner.py` | Normalización, extracción de hashtags | `TextCleaner` |
| `analyzer.py` | Sentiment, topics, summarization | `NLPAnalyzer` |
| `network.py` | Grafos dirigidos, métricas, comunidades | `NetworkAnalyzer` |
| `llm.py` | Chat local e API LLM | `LLMHandler` |
| `extractor.py` | Orquestación de todo lo anterior | `DataExtractor` |

Cada módulo:
- Tiene una responsabilidad única (Single Responsibility Principle)
- Puede testarse independientemente
- Se actualiza sin afectar a otros

La clase `DataExtractor` en `core/extractor.py` sigue siendo el punto de entrada, pero ahora **delega**, no **duplica** lógica.

---

### ¿Por qué dígrafo ponderado, no grafo?

- Los grafos no dirigidos pierden información: que A mencione a B es distinto a que B mencione a A.
- El peso es importante: que A mencione a B 3 veces es distinto a mencionarlo 1 vez.
- Permite calcular in-degree (popularidad) separado de out-degree (amplificación).

---

### ¿Por qué Louvain en lugar de otros algoritmos?

Alternativas:
- **Greedy modularity** (NetworkX): rápido, pero es un greedy heurístico frágil.
- **Spectral clustering**: más robusto, pero requiere matriz laplaciana (más RAM en redes grandes).
- **Label propagation**: estocástico, resultados varían en cada ejecución.
- **Louvain**: más rápido que spectral, más reproducible que label propagation, muy usado en práctica.

Implemento un fallback: si `python-louvain` no está instalado, uso `greedy_modularity_communities` de NetworkX.

---

### ¿Por qué TinyLlama × Gemma?

Para Unit 6 necesito un LLM que:
- Funcione offline (sin internet)
- Corra en hardware modesto (laptops, Colab básico)
- Sea gratuito

| Modelo | Size | VRAM | Velocidad | Calidad |
|---|---|---|---|---|
| TinyLlama 1.1B | ~2.2 GB | ~4 GB | ⚡⚡ | ⭐⭐ |
| Gemma-2 2B | ~3.5 GB | ~6 GB | ⚡ | ⭐⭐⭐ |
| Llama-2 7B | ~13 GB | ~16 GB | 🐢 | ⭐⭐⭐⭐ |
| Gemini API | N/A | API | ⚡⚡⚡ | ⭐⭐⭐⭐⭐ |

Elegí un fallback dual:
1. **Primero:** modelo local (TinyLlama es suficiente, Gemma-2 si tienes GPU)
2. **Si no hay GPU:** Gemini API (gratuita hasta 15 req/min)

---

### ¿Por qué se guarda el log del LLM?

Ejecutar un LLM es lento. Si revierto o quiero comparar respuestas, no quiero volver a ejecutarlo. El archivo `output.log` guarda:
- Prompt enviado
- Fecha/hora
- Modelo usado
- Tokens procesados
- Respuesta completa

Útil para auditoría y reproducibilidad.

---

## Instalación y Ejecución

### 1. Clonar y navegar al proyecto

```bash
cd /path/to/Unit_6/AEC3
```

### 2. Crear entorno virtual (recomendado)

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

**Nota:** `torch` es pesado (~2 GB). Si tienes GPU NVIDIA, instala `torch` con CUDA:
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### 4. Configurar variables de entorno

Copia `.env.example` a `.env` y completa:

```bash
cp .env.example .env
```

Edita `.env`:
```
RAPIDAPI_KEY=tu_clave_rapidapi_here
GEMINI_API_KEY=tu_clave_gemini_aqui
HF_TOKEN=tu_token_huggingface_aqui
```

**Dónde obtener las claves:**
- **RAPIDAPI_KEY:** https://rapidapi.com/hub → Sign Up → Usar clave existente de RapidAPI
- **GEMINI_API_KEY:** https://aistudio.google.com/app/apikey
- **HF_TOKEN:** https://huggingface.co/settings/tokens (es gratuito)

---

### 5. Ejecutar el pipeline

**Opción A: Interfaz de línea de comandos (`main.py`)**

```bash
# Cargar tweets de CSV, NO usar LLM, guardar en outputs/
python main.py --source Bitcoin_tweets_dataset_2.csv --no-llm

# Cargar tweets de API RapidAPI, usar LLM local (TinyLlama), guardar en outputs/
python main.py --api --output outputs/ --model TinyLlama/TinyLlama-1.1B-Chat-v1.0

# Ver opciones
python main.py --help
```

**Opción B: Script Python interactivo**

```python
from data_extractor import DataExtractor

# Crear instancia
ext = DataExtractor(source='Bitcoin_tweets_dataset_2.csv')

# Ejecutar pipeline completo
ext.execute_pipeline(
    use_llm=True,
    model_name='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    output_dir='outputs/'
)

# O paso a paso:
ext.load_data()
G = ext.build_interaction_graph()
metrics = ext.analyze_network(G)
prompt = ext.generate_prompt_from_network(G)
ext.chat_local_llm(prompt=prompt)
```

**Opción C: Jupyter Notebook (`AEC3_DataExtractor_U6.ipynb`)**

Abre el notebook en VS Code o Jupyter:
```bash
jupyter notebook
```

Navega a `Unit_6/AEC3/AEC3_DataExtractor_U6.ipynb` y ejecuta las celdas en orden.

**Opción D: Dashboard interactivo (`dashboard.py`)**

```bash
streamlit run dashboard.py
```

Se abre en http://localhost:8501 con:
- Editor de archivos CSV
- Análisis de hashtags
- Detección de bots
- Visualización de grafo

---

## Validación de Requisitos

| Requisito | Cumplido | Ubicación |
|---|---|---|
| Estructura centralizada (una clase DataExtractor) | ✅ | `/core/extractor.py` |
| Sin duplicación de código | ✅ | `data_extractor.py` reexporta, `dashboard.py` importa |
| Análisis de red con NetworkX | ✅ | `/core/network.py` + `build_interaction_graph()` + `analyze_network()` |
| Integración de LLM local | ✅ | `/core/llm.py` + `chat_local_llm()` |
| Fallback a API (no GPU required) | ✅ | `/core/llm.py` + `api_llm_fallback()` |
| Prompt interpretativo desde grafo | ✅ | `generate_prompt_from_network()` |
| Métodos nuevos en Unit 6 | ✅ | 5 métodos especificados (arriba) |

---

## Solución de Problemas

**Error:** `No module named 'torch'`
```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

**Error:** `No module named 'louvain'`
```bash
pip install python-louvain
```

**Error:** `CUDA out of memory` (si tienes GPU)
- Reduce `max_new_tokens` en `chat_local_llm()`
- O baja a modelo más pequeño (TinyLlama vs Gemma)
- O usa API fallback (sin GPU necesario)

**¿Cómo acelerar?**
- GPU NVIDIA: instala `torch` con CUDA
- Reduce `default_num_topics` en `/utils/constants.py` (por defecto 5)
- Salta el análisis de sentimiento si no lo necesitas

---

## Dependencias Principales

| Librería | Uso | Versión |
|---|---|---|
| `pandas` | Procesamiento de DataFrames | ≥1.3.0 |
| `numpy` | Álgebra lineal | ≥1.21.0 |
| `networkx` | Construcción y análisis de grafos | ≥2.6 |
| `python-louvain` | Detección de comunidades | ≥0.15 |
| `torch` | Backend de transformers | ≥2.0.0 |
| `transformers` | LLMs preentrenados | ≥4.30.0 |
| `textblob` | Sentiment analysis simple | ≥0.17.1 |
| `spacy` | NLP (tokenización, etiquetado) | ≥3.5.0 |
| `nltk` | Stemming, stopwords | ≥3.8 |
| `gensim` | Topic modeling (LDA) | ≥4.2.0 |
| `wordcloud` | Visualización de palabras frecuentes | ≥1.9.0 |
| `matplotlib` | Gráficos | ≥3.7.0 |
| `requests` | HTTP (API) | ≥2.31.0 |
| `python-dotenv` | Leer `.env` | ≥1.0.0 |
| `streamlit` | Dashboard interactivo | ≥1.28.0 *(opcional)* |

---

## Referencias

- [NetworkX Documentation](https://networkx.org/)
- [Python-Louvain](https://github.com/taynaud/python-louvain)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/)
- [Google Gemini API](https://aistudio.google.com/)
- [Gensim LDA](https://radimrehurek.com/gensim/)
- [TextBlob Sentiment](https://textblob.readthedocs.io/)
- [Streamlit Docs](https://docs.streamlit.io/)

---
