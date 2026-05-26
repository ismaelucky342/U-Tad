# AEC3 – Análisis de Redes Sociales + Integración LLM

## Introducción

En esta actividad me propongo extender la práctica anterior (AEC2 de Unidad 4) con dos nuevos componentes principales que permitan ir más allá del análisis de sentimiento tradicional. 

El primer componente es un análisis de redes sociales usando NetworkX, que construye grafos de interacciones a partir de menciones en tweets, calcula métricas de centralidad para identificar nodos influyentes, y detecta comunidades usando el algoritmo de Louvain.

El segundo componente integra modelos de lenguaje de gran tamaño (LLMs). La idea es que los insights extraídos del grafo se conviertan en prompts contextualizados que el LLM puede analizar e interpretar de forma cualitativa, proporcionando insights que van más allá de las métricas numéricas.

Mantengo el enfoque de centralizar toda la lógica en la clase `DataExtractor`, ahora extendida con nuevos métodos, pero esta vez he decidido modularizar el código en archivos separados para mantener la legibilidad y facilitar el mantenimiento.

---

## Estructura del Proyecto

Decidí separar el código en módulos para mejorar la mantenibilidad:

```
AEC3/
├── data_extractor.py           # Clase base que orquesta todo
├── network_analysis.py         # Métodos de NetworkX (grafo, centralidad, comunidades)
├── llm_integration.py          # Métodos de LLM (prompts, generación, fallback)
├── utils.py                    # Funciones auxiliares (exportación, validación)
├── AEC3_Network_LLM_Analysis.ipynb  # Notebook con ejemplos
├── requirements.txt            # Dependencias
├── .env.example               # Plantilla de configuración
├── .gitignore                 # Prevenir subir credenciales
└── README.md                  # Este archivo
```

### Decisión de Modularización

En AEC2 tenía toda la lógica en un único archivo `data_extractor.py`, lo cual funcionaba bien para ese alcance. Sin embargo, con los nuevos métodos de NetworkX e integración de LLM, el archivo crecería a más de 800 líneas, haciendo el código difícil de navegar.

He extraído en módulos separados pero mantengo `DataExtractor` como clase orquestadora que importa y expone todos los métodos. De esta forma:
- **data_extractor.py**: Interfaz pública (toda la lógica accesible desde la clase)
- **network_analysis.py**: Métodos especializados en análisis de redes
- **llm_integration.py**: Métodos especializados en LLM
- **utils.py**: Funciones reutilizables

---

## Instalación

### 1. Clonar o descargar el proyecto

```bash
cd Unit_6/AEC3
```

### 2. Crear y activar entorno virtual

Con venv:
```bash
python3.11 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

Con conda:
```bash
conda create -n aec3 python=3.11
conda activate aec3
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

Para GPU (NVIDIA):
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### 4. Descargar modelos de spacy

```bash
python -m spacy download en_core_web_sm
```

### 5. Configurar credenciales

```bash
cp .env.example .env
# Editar .env con tus credenciales
```

En `.env`:
```
RAPIDAPI_KEY=tu_clave_aqui
GOOGLE_API_KEY=tu_clave_google_ai_aqui
```

---

## Uso

### Opción 1: Ejecutar el Notebook (Recomendado)

```bash
jupyter notebook AEC3_Network_LLM_Analysis.ipynb
```

Este notebook ejecuta paso a paso el pipeline completo:
1. Carga de datos desde CSV local
2. Construcción del grafo de interacciones
3. Análisis de métricas de centralidad
4. Generación de prompts contextualizados
5. Ejecución del modelo LLM
6. Exportación de resultados

### Opción 2: Uso programático

```python
from data_extractor import DataExtractor

# 1. Cargar datos
ext = DataExtractor(source="Bitcoin_tweets.csv")
ext.load_data()

# 2. Construir grafo
G = ext.build_interaction_graph(mention_extraction=True)

# 3. Analizar red
analysis = ext.analyze_network(G, top_k=3)

# 4. Generar prompt
prompt = ext.generate_prompt_from_network(G, analysis)

# 5. Ejecutar LLM
response = ext.chat_local_llm(prompt=prompt, use_gpu=True)
print(response)

# 6. Exportar resultados
ext.export_network_analysis(output_dir="output", G=G, analysis=analysis)
```

---

## API de la Clase DataExtractor

### Métodos Nuevos (Unidad 6)

Implementé 4 métodos principales para el análisis de redes e integración LLM:

#### build_interaction_graph(mention_extraction=True) → nx.DiGraph

Construye un grafo dirigido de interacciones a partir de los tweets.

```python
G = ext.build_interaction_graph()
```

Los nodos son usuarios y hashtags. Las aristas representan interacciones:
- Menciones (@usuario) entre usuarios
- Uso de hashtags por parte de usuarios

El peso de cada arista representa la frecuencia de la interacción.

**Decisión de diseño**: Usé DiGraph (dirigido) en lugar de Graph (no dirigido) porque las menciones tienen dirección natural. De esta forma puedo calcular influencia de forma asimétrica.

---

#### analyze_network(G=None, top_k=3) → dict

Calcula métricas de centralidad y detecta comunidades usando Louvain.

```python
analysis = ext.analyze_network(G, top_k=5)
```

Retorna un diccionario con:
- Estadísticas globales (número de nodos, aristas, densidad)
- Top k nodos por degree centrality
- Top k nodos por betweenness centrality (intermediación)
- Top k nodos por closeness centrality
- Comunidades detectadas y sus tamaños

**Métricas calculadas**:
- **Degree**: Número de conexiones directas
- **Betweenness**: Qué tan importante es el nodo como "puente" entre otros
- **Closeness**: Distancia promedio a otros nodos en la red
- **Communities**: Grupos densamente conectados dentro de la red

---

#### generate_prompt_from_network(G=None, analysis=None) → str

Genera un prompt contextualizado a partir del análisis del grafo para ser enviado al LLM.

```python
prompt = ext.generate_prompt_from_network(G, analysis)
```

El prompt incluye:
- Estadísticas de la red (nodos, aristas, densidad)
- Top 3 nodos más influyentes
- Hashtags más frecuentes del corpus
- Información sobre comunidades detectadas
- Una pregunta específica pidiendo análisis interpretativo

El objetivo es que el LLM no solo vea números, sino que entienda el contexto de la red social.

---

#### chat_local_llm(prompt=None, model_name="google/gemma-2b-it", use_gpu=True) → str

Ejecuta un modelo LLM local para generar análisis interpretativo.

```python
response = ext.chat_local_llm(
    prompt=prompt,
    model_name="google/gemma-2b-it",
    use_gpu=True,
    temperature=0.7
)
```

Parámetros:
- `prompt`: Texto a procesar. Si es None, se genera automáticamente
- `model_name`: Modelo de Hugging Face ("google/gemma-2b-it", "mistralai/Mistral-7B-v0.1", etc.)
- `use_gpu`: Usar CUDA si está disponible
- `temperature`: Creatividad del modelo (0.0=determinístico, 1.0=creativo)
- `max_tokens`: Longitud máxima de la respuesta

**Modelos soportados**:
- google/gemma-2b-it (2B parámetros, requiere ~4 GB VRAM)
- google/gemma-7b-it (7B parámetros, requiere ~14 GB VRAM)
- mistralai/Mistral-7B-v0.1
- facebook/opt-6.7b

**Fallback automático**: Si no hay GPU disponible o hay error al cargar el modelo local, intenta usar Google Generative AI API de forma automática.

---

#### export_network_analysis(output_dir="output", G=None, analysis=None) → None

Exporta todos los resultados del análisis a archivos.

```python
ext.export_network_analysis(output_dir="results")
```

Genera los siguientes archivos:
- `network_stats.json`: Métricas de centralidad en formato estructurado
- `communities.json`: Estructura de las comunidades detectadas
- `network_prompt.txt`: Prompt enviado al LLM (para auditoría)
- `network_graph.gexf`: Grafo en formato GEXF (importable en Gephi para visualización)
- `llm_response.txt`: Respuesta completa del modelo
- Todos los outputs de export_results() de AEC2

---

### Métodos Heredados (Unidad 4)

La clase sigue exponiendo todos los métodos de AEC2:
- load_data() / load_data_api()
- clean_text()
- extract_hashtags()
- analytics_hashtags_extended()
- model_topics() con LDA
- analyze_sentiment()
- parse_and_summarize()
- export_results()

---

## Ejemplo Completo

Aquí muestro un flujo completo de análisis:

```python
from data_extractor import DataExtractor

# Cargar datos
ext = DataExtractor(source="Bitcoin_tweets.csv")
ext.load_data()
print(f"Cargados {len(ext.data)} tweets")

# Análisis de redes
G = ext.build_interaction_graph()
print(f"Grafo: {G.number_of_nodes()} nodos, {G.number_of_edges()} aristas")

# Métricas
analysis = ext.analyze_network(G, top_k=3)
influencers = [node for node, _ in analysis['top_degree_centrality']]
print(f"Top influencers: {influencers}")

# Generar context para LLM
prompt = ext.generate_prompt_from_network(G, analysis)

# Obtener análisis interpretativo
response = ext.chat_local_llm(prompt, use_gpu=True)
print("\nAnálisis del modelo LLM:")
print(response)

# Guardar todo
ext.export_network_analysis(output_dir="resultados")
```

Output esperado:
```
Cargados 10000 tweets
Grafo: 2847 nodos, 8923 aristas
Top influencers: ['@bitcoin_pro', '@crypto_daily', '@mining_pool']

Análisis del modelo LLM:
Based on the network analysis, the Bitcoin community exhibits several
distinct patterns. The high centrality of specific nodes suggests
concentrated influence...

Resultados exportados a: resultados/
```

---

## Decisiones Técnicas

### Por qué NetworkX

Elegí NetworkX porque:
- Es la librería estándar en Python para gráfos
- Bien documentada y mantenida activamente
- Eficiente para grafos de ~10k nodos
- Ofrece múltiples algoritmos de análisis listos para usar

Alternativas que consideré:
- GraphX (Apache Spark): Overkill para el tamaño de datos
- igraph: Menos Pythonic, requiere dependencias externas
- Custom implementation: Demasiado tiempo, reinventar la rueda

### Por qué Louvain para comunidades

Comparación de algoritmos:

- **Girvan-Newman**: Muy preciso pero O(n³), prohibitivo para >1000 nodos
- **Label Propagation**: Muy rápido pero resultados menos estables
- **Louvain**: O(n log n), escalable, resultados interpretables, ampliamente usado
- **Spectral Clustering**: Requiere cálculos de eigenvalores, más lento

Louvain es el balance perfecto entre velocidad y calidad.

### Modelos LLM Local vs API

He implementado soporte para ambos:

**Modelo Local**:
- Privacidad total (datos no abandonan la máquina)
- Sin costos recurrentes
- Requiere GPU para velocidad
- Control total sobre parámetros

**API (Google/OpenAI)**:
- Modelos más potentes
- No requiere GPU local
- Costo por uso
- Menos privacidad

Mi solución intenta local primero, fallback automático a API si falla.

### Prompt Engineering

Pasé tiempo optimizando cómo generar prompts. El LLM responde mejor cuando:
1. El contexto es específico (no genérico)
2. Incluye datos numéricos de la red
3. Plantea preguntas claras
4. Solicita análisis interpretativo, no solo descriptivo

Por eso `generate_prompt_from_network()` construye prompts contextualizados.

---

## Requerimientos de Hardware

| Componente | CPU | GPU | RAM Mínima | Notas |
|---|---|---|---|---|
| Cargar 10k tweets | 1-2 min | NA | 1 GB | Depende de tamaño del archivo |
| Construir grafo | 10-30 s | NA | 500 MB | NetworkX es eficiente |
| LLM local (2B) | 30 min | 3 min | 8 GB | Sin GPU es muy lento |
| LLM local (7B) | Infeasible | 10 min | 16 GB | Requiere GPU sí o sí |
| API (Google) | 10 s | NA | 500 MB | Red requerida, clave necesaria |

Mi recomendación: Si tienes GPU, úsala. Si no, la API gratuita de Google es suficiente.

---

## Troubleshooting

### Error: "No module named 'torch'"

```bash
pip install torch --upgrade
```

Para GPU (NVIDIA CUDA 12.1):
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

### Error: "CUDA out of memory"

Soluciones en orden de preferencia:

1. Usar modelo más pequeño:
```python
ext.chat_local_llm(model_name="google/gemma-2b-it")
```

2. Usar CPU (más lento pero posible):
```python
ext.chat_local_llm(use_gpu=False)
```

3. Usar API externa (sin GPU requerida):
```python
response = ext._chat_google_ai(prompt)
```

### Error: "transformers ModuleNotFoundError"

```bash
pip install transformers>=4.35.0
```

### El grafo tiene muy pocos nodos (solo 10)

Probablemente los tweets no contienen menciones. Verifica:

```python
import re
mention_pattern = re.compile(r'@\w+')
for text in ext.data['text'][:10]:
    mentions = mention_pattern.findall(text)
    print(f"{text[:50]}: {mentions}")
```

Si no hay menciones, prueba ajustar el tipo de datos o verificar que el dataset sea adecuado.

### Error: "RAPIDAPI_KEY not found in environment"

Verifica que `.env` esté en la carpeta actual:
```bash
ls -la | grep .env
# Debe mostrar .env
```

Verifica que Python puede leerlo:
```python
from dotenv import load_dotenv
import os
load_dotenv()
print(os.getenv('RAPIDAPI_KEY'))
# Debe mostrar tu clave, no None
```

## Optimizaciones Futuras

1. Visualización interactiva: Dashboard con Streamlit
2. Análisis temporal: Evolución del grafo en el tiempo
3. Detección de bots: Patrones de comportamiento
4. Fine-tuning: Entrenar LLM con datos específicos
5. Paralelización: Procesar múltiples consultas en paralelo

---

## Estructura Modular del Código

He separé el código en módulos para mejorar la mantenibilidad:

- **data_extractor.py**: Clase orquestadora que expone toda la API pública
- **network_analysis.py**: Métodos especializados en análisis de redes (NetworkX)
- **llm_integration.py**: Métodos especializados en integración LLM (Transformers)
- **utils.py**: Funciones auxiliares de exportación y validación

La clase `DataExtractor` importa desde estos módulos, manteniendo una interfaz simple para el usuario final mientras que internamente delega las operaciones especializadas.

---

## 📚 Referencias

### Papers y Documentación
- **NetworkX**: https://networkx.org/documentation/
- **Louvain Algorithm**: Blondel et al. (2008) - Fast unfolding of communities in large networks
- **Transformers**: https://huggingface.co/docs/transformers/
- **Gemma**: https://ai.google.dev/gemma/

### Recursos Externos
- **Hugging Face Model Hub**: https://huggingface.co/models
- **RapidAPI Twitter API**: https://rapidapi.com/alexanderxbx/api/twitter-api45
- **Google Generative AI Studio**: https://aistudio.google.com

### Entregas Relacionadas
- **AEC2 (Unidad 4)**: Análisis de sentimiento y tendencias
- **AEC1 (Unidad 3)**: Extracción básica de tweets

---

## 📝 Notas Importantes

1. **Gestión de Credenciales**:
   - NUNCA commits `.env` con credenciales reales
   - Usar `git-secrets` o `pre-commit` para prevenir fugas

2. **Reproducibilidad**:
   - Guardar versiones exactas de modelos (`model.safetensors`)
   - Documentar hyper-parámetros (temperature, top_p, etc.)
   - Usar random seed fijo para resultados consistentes

3. **Ética**:
   - Respetar privacidad en datasets de redes sociales
   - Documentar sesgos en modelos LLM
   - No usar para amplifikación de spam/desinformación

---

## 🙏 Agradecimientos

- Universidad U-Tad por el contexto académico
- Comunidad de Hugging Face por modelos accesibles
- NetworkX team por librería robusta

---

**Última actualización**: Mayo 2026  
**Versión**: 1.0  
**Autor**: Análisis Automático
