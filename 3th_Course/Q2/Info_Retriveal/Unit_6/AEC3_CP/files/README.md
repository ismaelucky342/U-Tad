# AEC3 – Análisis de Redes e Integración de LLMs

## Introducción

Esta entrega es la continuación directa de la AEC2. Se mantiene la misma clase `DataExtractor` como núcleo del proyecto y se amplía con dos grandes bloques nuevos:

1. **Análisis de redes sociales con NetworkX**: construcción de un grafo de menciones, cálculo de métricas de centralidad y detección de comunidades con el algoritmo de Louvain.
2. **Integración de LLM local via Ollama**: los insights extraídos de la red se condensan en un prompt interpretativo que se pasa a `gemma3` corriendo en local. Se incluye un modo de chat interactivo con historial completo de conversación.

La decisión de usar Ollama en lugar de Hugging Face directamente tiene una justificación práctica clara: Ollama gestiona la descarga, cuantización y ejecución del modelo de forma transparente, sin necesidad de gestionar manualmente tokenizadores, device maps ni memoria GPU. El resultado es el mismo modelo pero con una interfaz mucho más limpia para integrar en un pipeline Python.

## Estructura del Proyecto

```
AEC3/
├── data_extractor.py        # Clase principal: todo el pipeline centralizado
├── AEC3_DataExtractor.ipynb # Notebook con ejemplos y visualizaciones
├── dashboard.py             # Dashboard Streamlit (6 tabs, incluye red y chat LLM)
├── requirements.txt         # Dependencias Python
├── .env.example             # Plantilla para RAPIDAPI_KEY
└── README.md                # Este archivo
```

## Nuevos Métodos (AEC3)

Todos los nuevos métodos están integrados en la misma clase `DataExtractor`. No se rompe nada de lo que ya existía.

### `_extract_mentions(text)` — privado

Extrae las menciones `@usuario` de un tweet. Método auxiliar usado por `build_interaction_graph`. Se mantiene separado de `clean_text` porque este último elimina las menciones intencionalmente (son ruido para LDA y sentimiento, pero son los datos clave para el grafo).

### `build_interaction_graph()` → `nx.DiGraph`

Construye el grafo de interacciones a partir de `self.data`. La lógica es:

- **Nodo**: cada usuario (`user_name`) que aparece en el dataset, con atributo `tweet_count`.
- **Arista dirigida A → B**: usuario A menciona a B en algún tweet, con `weight` = número de veces que ocurre esa mención.

Las auto-menciones se filtran. El resultado es un `DiGraph` de NetworkX listo para analizar.

```python
ext = DataExtractor()
ext.load_data_api(query="#bitcoin", max_results=200)
G = ext.build_interaction_graph()
# Output: 🕸️ Grafo construido: 847 nodos, 1203 aristas
```

### `analyze_network(G)` → `dict`

Calcula las métricas de red y detecta comunidades. Métricas calculadas:

| Métrica | Qué mide | Por qué es útil |
|---|---|---|
| In-degree centrality | Cuántos usuarios mencionan a cada nodo, normalizado | Identifica los 'influencers' más citados |
| Out-degree centrality | Cuántos usuarios menciona cada nodo | Detecta usuarios hiperconectados o bots |
| Betweenness centrality | Frecuencia con la que un nodo actúa como puente entre otros | Identifica intermediarios clave en la difusión |
| PageRank | Influencia global ponderada por la calidad de los que te mencionan | El mismo algoritmo que usaba Google; mide influencia real, no solo popularidad |
| Louvain (comunidades) | Agrupa nodos con patrones de interacción similares | Revela subgrupos temáticos o sociales dentro de la comunidad |

La detección de comunidades usa `python-louvain` si está instalado, con fallback automático a `greedy_modularity_communities` de NetworkX si no lo está.

El método genera automáticamente una visualización con dos paneles:
- Grafo de la red con nodos coloreados por comunidad y tamaño proporcional al PageRank.
- Histograma de distribución de in-degree en escala logarítmica.

```python
metrics = ext.analyze_network(G)
# Imprime tabla de estadísticas y guarda 'network_analysis.png'
```

### `generate_prompt_from_network(G, metrics)` → `str`

Traduce los resultados cuantitativos del análisis de red a un prompt en lenguaje natural para el LLM. Incluye:

- Estadísticas globales de la red (nodos, aristas, densidad, comunidades).
- Top 3 nodos por in-degree y PageRank con sus valores.
- Hashtag más frecuente del dataset.
- Cuatro preguntas específicas para guiar el análisis interpretativo del modelo.

La idea es que el LLM no solo repita los números, sino que los interprete en el contexto de las dinámicas sociales de Twitter y las comunidades de criptomonedas.

### `chat_local_llm(prompt, model, ollama_url, stream)` → `str`

Gestiona la interacción con el LLM local. Flujo:

1. Verifica que Ollama está en ejecución y que el modelo está disponible.
2. Si se pasa un `prompt`, lo envía como primer mensaje y muestra la respuesta.
3. Abre un bucle de chat interactivo donde el usuario puede hacer preguntas de seguimiento.
4. El historial completo se mantiene en memoria y se pasa en cada petición, permitiendo conversaciones con contexto real.
5. Para salir: escribe `salir`, `exit`, `quit` o pulsa Ctrl+C.

Con `stream=True` (por defecto) los tokens aparecen en tiempo real mientras el modelo genera la respuesta, lo que da una experiencia de chat más natural.

## El Pipeline Completo (AEC3)

```python
from data_extractor import DataExtractor

# 1. Cargar datos desde API
ext = DataExtractor()
ext.load_data_api(query="#bitcoin", max_results=200, output_file="tweets.csv")

# O desde CSV local
# ext = DataExtractor("Bitcoin_tweets.csv")
# ext.load_data()

# 2. Análisis de redes
G       = ext.build_interaction_graph()
metrics = ext.analyze_network(G)

# 3. Generar prompt desde los insights de la red
prompt = ext.generate_prompt_from_network(G, metrics)

# 4. Chat con el LLM local (gemma3 via Ollama)
ext.chat_local_llm(prompt=prompt, model="gemma3")

# 5. Exportar todos los resultados
ext.export_results(output_dir="output")
```

## Configuración de Ollama

Ollama es la capa de gestión del LLM local. A diferencia de usar Hugging Face directamente (que requiere gestionar manualmente tokenizadores, precisión del modelo, device maps y memoria GPU), Ollama encapsula todo eso y expone una API REST sencilla.

### Instalación

```bash
# Linux / macOS
curl -fsSL https://ollama.com/install.sh | sh

# Windows: descargar instalador desde https://ollama.com
```

### Descargar y ejecutar el modelo

```bash
# Iniciar el servidor Ollama (queda escuchando en puerto 11434)
ollama serve

# En otra terminal, descargar gemma3
ollama pull gemma3
```

### Requisitos de hardware

| Configuración | RAM mínima | Notas |
|---|---|---|
| gemma3 (4B, cuantizado Q4) | 6 GB | Funciona en CPU, lento |
| gemma3 (4B, cuantizado Q4) | 6 GB VRAM | GPU NVIDIA/AMD, rápido |
| gemma3 (12B) | 12 GB RAM / 10 GB VRAM | Mejor calidad, más lento |

Si no tienes GPU, el modelo funciona en CPU pero las respuestas tardan más (30-120 segundos por respuesta según el hardware).

### Verificar que todo funciona

```bash
# Test rápido
curl http://localhost:11434/api/chat -d '{
  "model": "gemma3",
  "messages": [{"role": "user", "content": "Hola, ¿estás funcionando?"}],
  "stream": false
}'
```

## Dependencias

```
# Instalar todo de una vez
pip install -r requirements.txt
```

Contenido del `requirements.txt`:

```
pandas>=2.0
requests>=2.31
textblob>=0.17
gensim>=4.3          # Requiere Python 3.11-3.13
nltk>=3.8
spacy>=3.7
spacytextblob>=0.1.7
wordcloud>=1.9
matplotlib>=3.7
seaborn>=0.12
networkx>=3.2
python-louvain>=0.16  # Detección de comunidades (opcional, hay fallback)
streamlit>=1.30
python-dotenv>=1.0
```

Modelo de spaCy:
```bash
python -m spacy download en_core_web_sm
```

## Variables de entorno

Crea un archivo `.env` en la raíz del proyecto (no lo subas al repositorio):

```
RAPIDAPI_KEY=tu_clave_aqui
```

## Dashboard Streamlit

El dashboard incluye ahora 6 tabs:

| Tab | Contenido |
|---|---|
| 📊 Top Hashtags | Barras horizontales de los N hashtags más frecuentes |
| ☁️ WordCloud | Nube de palabras de hashtags |
| 📈 Evolución | Evolución temporal de los top 5 hashtags |
| 🤖 Bots | Detección de posibles cuentas automatizadas |
| 🕸️ Red de Menciones | Grafo interactivo, métricas de centralidad, comunidades |
| 💬 Chat LLM | Generación de prompt desde la red + chat con gemma3 |

Para lanzarlo:

```bash
streamlit run dashboard.py
```

## Diferencias clave respecto a la AEC2

| Aspecto | AEC2 | AEC3 |
|---|---|---|
| LLM | No había | gemma3 via Ollama (local, sin API externa) |
| Redes | No había | NetworkX + Louvain + visualización |
| Prompt | No había | Generado automáticamente desde métricas de red |
| Chat | No había | Modo interactivo con historial completo de conversación |
| Dashboard | 4 tabs | 6 tabs (se añaden Red y Chat LLM) |

## Solución de Problemas

**"No se puede conectar a Ollama"**  
Verifica que el servidor está corriendo: `ollama serve`. Por defecto escucha en `http://localhost:11434`.

**"Modelo 'gemma3' no encontrado"**  
Descárgalo: `ollama pull gemma3`. La primera descarga tarda varios minutos.

**"python-louvain no instalado"**  
El código tiene fallback automático a `greedy_modularity_communities` de NetworkX. Instálalo para mejores resultados: `pip install python-louvain`.

**"ImportError: gensim"**  
gensim no es compatible con Python 3.14+. Usa Python 3.11-3.13 para LDA. Los demás módulos funcionan en cualquier versión.

**El grafo tiene muy pocas aristas**  
La API gratuita de Twitter (RapidAPI tier free) devuelve 100-200 tweets. Con tan pocos datos, pocos usuarios se mencionan entre sí. Usa el dataset de Kaggle ("Bitcoin Tweets") para un grafo más rico.

## Fuentes de datos

- **API en tiempo real**: [twitter-api45 en RapidAPI](https://rapidapi.com/alexanderxbx/api/twitter-api45)
- **Dataset estático**: [Bitcoin Tweets – Kaggle](https://www.kaggle.com/datasets/kaushiksuresh147/bitcoin-tweets)

---

## Referencias

### AEC1 y AEC2 (heredadas)
- **[42 AI](https://42-ai.github.io/)** — referencia metodológica para el pipeline.
- **[RapidAPI](https://rapidapi.com/)** — extracción de tweets en tiempo real.
- **[Pandas](https://pandas.pydata.org/docs/)**, **[NLTK](https://www.nltk.org/)**, **[TextBlob](https://textblob.readthedocs.io/)**, **[Gensim](https://radimrehurek.com/gensim/)**, **[spaCy](https://spacy.io/)**, **[WordCloud](https://amueller.github.io/word_cloud/)**, **[Matplotlib](https://matplotlib.org/)**, **[Streamlit](https://streamlit.io/)**.

### AEC3 (nuevas)
- **[NetworkX](https://networkx.org/documentation/stable/)** — construcción y análisis del grafo de interacciones.
- **[python-louvain](https://python-louvain.readthedocs.io/)** — detección de comunidades con el algoritmo de Louvain.
- **[Ollama](https://ollama.com)** — gestión y ejecución de LLMs en local con API REST.
- **[Gemma 3 (Google)](https://ai.google.dev/gemma)** — modelo de lenguaje usado para el análisis interpretativo.
- **[NetworkX – Community detection](https://networkx.org/documentation/stable/reference/algorithms/community.html)** — documentación de los algoritmos de comunidad de NetworkX.
