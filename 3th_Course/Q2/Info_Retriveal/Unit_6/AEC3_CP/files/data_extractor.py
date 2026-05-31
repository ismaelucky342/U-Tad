#====================================================================================================#
#                                                                                                    #
#                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        #
#      AEC3 - BAIN                                       ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       #
#                                                        ██║   ██║█████╗██║   ███████║██║  ██║       #
#      created:        08/04/2026  -  01:00:51           ██║   ██║╚════╝██║   ██╔══██║██║  ██║       #
#      last change:    31/05/2026  -  00:00:00           ╚██████╔╝      ██║   ██║  ██║██████╔╝       #
#                                                         ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        #
#                                                                                                    #
#      Ismael Hernandez Clemente                         ismael.hernandez@live.u-tad.com             #
#                                                                                                    #
#      Github:                                           https://github.com/ismaelucky342            #
#                                                                                                    #
#====================================================================================================#

import os
import re
import unicodedata
import pandas as pd
import requests
from pathlib import Path


class DataExtractor:
    """
    Clase central del pipeline de análisis de tweets.

    AEC1: carga de datos, limpieza, análisis de hashtags.
    AEC2: modelado de tópicos (LDA), análisis de sentimiento, resumen extractivo.
    AEC3: análisis de redes con NetworkX + integración de LLM local via Ollama (gemma3).
    """

    # Patrones compilados una sola vez para eficiencia
    _RE_URL     = re.compile(r'https?://\S+|www\.\S+', re.IGNORECASE)
    _RE_MENTION = re.compile(r'@(\w+)')
    _RE_HASHTAG = re.compile(r'#(\w+)')
    _RE_SPECIAL = re.compile(r'[^\w\s#]', re.UNICODE)
    _RE_SPACES  = re.compile(r'\s+')

    def __init__(self, source: str = None, chunksize: int = 100_000):
        """
        Inicializa el extractor.

        Parámetros:
            source   : Ruta al archivo local CSV o JSON. Puede ser None si se
                       va a usar load_data_api() para obtener tweets en tiempo real.
            chunksize: Tamaño de chunk para leer CSVs grandes sin saturar la RAM.
        """
        self.source    = source
        self.data      = None
        self.chunksize = chunksize

    # =========================================================================
    # BLOQUE 1 – EXTRACCIÓN Y CARGA DE DATOS  (AEC1)
    # =========================================================================

    def _parse_api_response(self, response_json: dict) -> list:
        """
        Normaliza la respuesta JSON de RapidAPI.

        La API de Twitter vía RapidAPI puede devolver la lista de tweets bajo
        distintas claves según el endpoint y versión ('tweets', 'data',
        'timeline', 'results', 'statuses'). Este método busca la clave correcta
        de forma robusta y normaliza cada tweet al formato mínimo:
        {user_name, date, text}.
        """
        tweets_list = None
        for key in ['tweets', 'data', 'timeline', 'results', 'statuses']:
            if key in response_json and isinstance(response_json[key], list):
                tweets_list = response_json[key]
                break

        if tweets_list is None:
            raise ValueError(f"No se encontró lista de tweets. Claves disponibles: {list(response_json.keys())}")

        rows = []
        for t in tweets_list:
            if not isinstance(t, dict):
                continue
            text = t.get('text') or t.get('full_text') or t.get('body') or ''
            user = (t.get('user_name') or t.get('author_id') or
                    t.get('user', {}).get('name') or 'unknown')
            date = t.get('date') or t.get('created_at') or t.get('timestamp') or ''
            if text.strip():
                rows.append({'user_name': str(user).strip(),
                             'date':      str(date).strip(),
                             'text':      str(text).strip()})
        if not rows:
            raise ValueError("La respuesta de la API no contiene tweets válidos.")
        return rows

    def load_data_api(self, query: str, max_results: int = 100,
                      output_file: str = "tweets.csv") -> pd.DataFrame:
        """
        Extrae tweets en tiempo real desde la API de Twitter vía RapidAPI.

        La clave RAPIDAPI_KEY se lee desde la variable de entorno del mismo nombre
        para no exponerla en el código. El resultado se guarda en CSV local para
        poder trabajar con él sin agotar la cuota de la API.

        Parámetros:
            query      : Hashtag o término de búsqueda (ej. '#bitcoin').
            max_results: Número máximo de tweets a extraer (el tier gratuito
                         suele devolver 100-200 como máximo).
            output_file: Ruta del CSV donde se guardan los tweets extraídos.
        """
        try:
            resp = requests.get(
                "https://twitter-api45.p.rapidapi.com/search.php",
                headers={"X-RapidAPI-Key":  os.environ.get("RAPIDAPI_KEY", ""),
                         "X-RapidAPI-Host": "twitter-api45.p.rapidapi.com"},
                params={"query": query, "count": max_results},
                timeout=15
            )
            resp.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Fallo en la petición a la API: {e}")

        rows       = self._parse_api_response(resp.json())
        self.data  = pd.DataFrame(rows)
        self.data.to_csv(output_file, index=False, encoding="utf-8")
        self.source = output_file
        print(f"✅ {len(self.data)} tweets extraídos y guardados en '{output_file}'")
        return self.data

    def load_data(self) -> pd.DataFrame:
        """
        Carga datos desde el archivo local indicado en self.source (CSV o JSON).

        Para CSVs grandes se usa chunksize: se lee en bloques y se concatenan,
        evitando cargar todo el archivo en memoria de una vez. También normaliza
        los nombres de columna por si vienen con espacios o CRLF.
        """
        ext = Path(self.source).suffix.lower()

        if ext == '.json':
            self.data = pd.read_json(self.source, encoding='utf-8')
        elif ext == '.csv':
            chunks    = pd.read_csv(self.source, encoding='utf-8',
                                    chunksize=self.chunksize, low_memory=False)
            self.data = pd.concat(chunks, ignore_index=True)
        else:
            raise ValueError(f"Formato no soportado: '{ext}'. Usa CSV o JSON.")

        self.data.columns = [c.strip().replace('\r', '') for c in self.data.columns]
        print(f"✅ {len(self.data):,} filas cargadas – columnas: {list(self.data.columns)}")
        return self.data

    # =========================================================================
    # BLOQUE 2 – LIMPIEZA Y EXTRACCIÓN  (AEC1)
    # =========================================================================

    def clean_text(self, text: str) -> str:
        """
        Normaliza un tweet: minúsculas, sin URLs, sin menciones, sin emojis,
        sin caracteres especiales. CONSERVA los hashtags (#bitcoin) porque son
        fundamentales para los análisis posteriores.
        """
        if not isinstance(text, str):
            text = str(text) if pd.notna(text) else ''
        text = text.strip().lower()
        text = self._RE_URL.sub(' ', text)
        text = self._RE_MENTION.sub(' ', text)
        text = ''.join(ch for ch in text
                       if unicodedata.category(ch) not in ('So', 'Sk', 'Cs'))
        text = self._RE_SPECIAL.sub(' ', text)
        return self._RE_SPACES.sub(' ', text).strip()

    def extract_hashtags(self, text: str) -> list:
        """
        Extrae hashtags únicos de un tweet (en minúsculas, sin duplicados,
        manteniendo el orden de aparición).
        """
        if not isinstance(text, str):
            return []
        seen, result = set(), []
        for tag in self._RE_HASHTAG.findall(text):
            t = tag.lower()
            if t not in seen:
                seen.add(t)
                result.append(t)
        return result

    def _extract_mentions(self, text: str) -> list:
        """
        Extrae menciones (@usuario) únicas de un tweet.
        Método privado usado por build_interaction_graph.
        """
        if not isinstance(text, str):
            return []
        seen, result = set(), []
        for mention in self._RE_MENTION.findall(text):
            m = mention.lower()
            if m not in seen:
                seen.add(m)
                result.append(m)
        return result

    # =========================================================================
    # BLOQUE 3 – ANÁLISIS DE HASHTAGS  (AEC1)
    # =========================================================================

    def analytics_hashtags_extended(self) -> dict:
        """
        Analiza hashtags desde tres perspectivas:
          - 'overall' : frecuencia global de cada hashtag.
          - 'by_user' : qué usuarios usan cada hashtag y con qué frecuencia
                        (útil para detectar bots que repiten los mismos hashtags).
          - 'by_date' : evolución temporal de hashtags día a día.

        Devuelve un dict con tres DataFrames.
        """
        if self.data is None:
            raise RuntimeError("Sin datos. Llama a load_data() o load_data_api() primero.")

        df = self.data.copy()
        df['clean_text'] = df['text'].apply(self.clean_text)
        df['hashtags']   = df['clean_text'].apply(self.extract_hashtags)
        df['date']       = pd.to_datetime(df['date'], utc=True, errors='coerce').dt.date

        df_exp = df.explode('hashtags').dropna(subset=['hashtags'])
        df_exp = df_exp[df_exp['hashtags'].str.strip() != ''].rename(columns={'hashtags': 'hashtag'})

        overall = (df_exp.groupby('hashtag', as_index=False).size()
                         .rename(columns={'size': 'frequency'})
                         .sort_values('frequency', ascending=False)
                         .reset_index(drop=True))
        by_user = (df_exp.groupby(['user_name', 'hashtag'], as_index=False).size()
                         .rename(columns={'size': 'frequency'})
                         .sort_values('frequency', ascending=False)
                         .reset_index(drop=True))
        by_date = (df_exp.groupby(['date', 'hashtag'], as_index=False).size()
                         .rename(columns={'size': 'frequency'})
                         .sort_values(['date', 'frequency'], ascending=[True, False])
                         .reset_index(drop=True))

        print(f"📊 {len(overall)} hashtags únicos encontrados.")
        return {'overall': overall, 'by_user': by_user, 'by_date': by_date}

    def generate_hashtag_wordcloud(self, overall_df: pd.DataFrame = None,
                                   max_words: int = 100, figsize: tuple = (10, 6)) -> None:
        """
        Genera y muestra una nube de palabras (wordcloud) a partir de las
        frecuencias de hashtags. Los hashtags más frecuentes aparecen más grandes.
        """
        import matplotlib.pyplot as plt
        from wordcloud import WordCloud

        if overall_df is None:
            overall_df = self.analytics_hashtags_extended()['overall']

        freq_dict = dict(zip(overall_df['hashtag'], overall_df['frequency']))
        wc = WordCloud(width=figsize[0] * 100, height=figsize[1] * 100,
                       max_words=max_words, background_color='white',
                       colormap='viridis').generate_from_frequencies(freq_dict)

        plt.figure(figsize=figsize)
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.tight_layout()
        plt.savefig('wordcloud_hashtags.png', dpi=150, bbox_inches='tight')
        plt.show()

    # =========================================================================
    # BLOQUE 4 – MODELADO DE TÓPICOS  (AEC2)
    # =========================================================================

    def model_topics(self, num_topics: int = 5, passes: int = 10,
                     min_word_len: int = 3) -> list:
        """
        Aplica LDA (Latent Dirichlet Allocation) con gensim para descubrir los
        temas ocultos del corpus de tweets.

        Filtrado aplicado antes de entrenar:
          - Stopwords en inglés.
          - Palabras muy cortas (< min_word_len caracteres).
          - Números puros.
          - Hashtags (se analizan por separado con analytics_hashtags_extended).

        Devuelve una lista de tópicos; cada tópico es una lista de 10 palabras.

        NOTA: gensim requiere Python 3.11-3.13. Si usas Python 3.14+ el import
        fallará y el método lanza ImportError con instrucciones claras.
        """
        try:
            import gensim
            from gensim import corpora
        except ImportError:
            raise ImportError(
                "gensim no está instalado o no es compatible con esta versión de Python. "
                "Usa Python 3.11–3.13 y ejecuta: pip install gensim"
            )

        import nltk
        from nltk.corpus import stopwords
        nltk.download('stopwords', quiet=True)
        stop_words = set(stopwords.words('english'))

        if 'clean_text' not in self.data.columns:
            self.data['clean_text'] = self.data['text'].apply(self.clean_text)

        texts = []
        for text in self.data['clean_text'].dropna():
            words = [w.lower() for w in text.split()
                     if (len(w) >= min_word_len
                         and not w.startswith('#')
                         and not w.isdigit()
                         and w not in stop_words
                         and not all(c.isdigit() or c in '-.' for c in w))]
            if words:
                texts.append(words)

        if not texts:
            raise ValueError("No quedan palabras después del filtrado. Corpus demasiado pequeño.")

        dictionary = corpora.Dictionary(texts)
        corpus     = [dictionary.doc2bow(text) for text in texts]
        lda_model  = gensim.models.LdaModel(corpus, num_topics=num_topics,
                                            id2word=dictionary, passes=passes,
                                            random_state=42, workers=1)

        topics = [[w for w, _ in t[1]]
                  for t in lda_model.show_topics(num_topics=num_topics,
                                                 num_words=10, formatted=False)]
        print(f"🧠 LDA completado: {num_topics} tópicos ({len(texts)} documentos)")
        return topics

    # =========================================================================
    # BLOQUE 5 – ANÁLISIS DE SENTIMIENTO  (AEC2)
    # =========================================================================

    def analyze_sentiment(self, method: str = 'textblob') -> pd.DataFrame:
        """
        Calcula la polaridad y subjetividad de cada tweet.

        Métricas:
          - sentiment_polarity    : [-1, +1]. -1 = muy negativo, +1 = muy positivo.
          - sentiment_subjectivity: [0, 1].   0  = objetivo/hechos, 1 = opinión.

        Métodos disponibles:
          - 'textblob' : rápido, basado en diccionarios. Suficiente para la mayoría de casos.
          - 'spacy'    : más preciso pero requiere spaCy + spacytextblob instalados.
        """
        if 'clean_text' not in self.data.columns:
            self.data['clean_text'] = self.data['text'].apply(self.clean_text)

        if method == 'textblob':
            from textblob import TextBlob
            self.data['sentiment_polarity'] = (
                self.data['clean_text'].apply(lambda x: TextBlob(x).sentiment.polarity))
            self.data['sentiment_subjectivity'] = (
                self.data['clean_text'].apply(lambda x: TextBlob(x).sentiment.subjectivity))

        elif method == 'spacy':
            import spacy
            from spacytextblob.spacytextblob import SpacyTextBlob
            nlp = spacy.load('en_core_web_sm')
            nlp.add_pipe('spacytextblob')
            self.data['sentiment_polarity'] = (
                self.data['clean_text'].apply(lambda x: nlp(x)._.polarity))
            self.data['sentiment_subjectivity'] = (
                self.data['clean_text'].apply(lambda x: nlp(x)._.subjectivity))
        else:
            raise ValueError(f"Método '{method}' no soportado. Usa 'textblob' o 'spacy'.")

        return self.data

    # =========================================================================
    # BLOQUE 6 – RESUMEN EXTRACTIVO  (AEC2)
    # =========================================================================

    def parse_and_summarize(self, summary_ratio: float = 0.05,
                            max_length: int = 500) -> str:
        """
        Genera un resumen extractivo del corpus completo.

        No genera texto nuevo (abstractivo), sino que selecciona las oraciones
        más relevantes del corpus original (extractivo). El algoritmo:
          1. Tokeniza el corpus completo en oraciones.
          2. Calcula la frecuencia de cada palabra significativa.
          3. Puntúa cada oración por la suma de frecuencias de sus palabras.
          4. Selecciona las top (summary_ratio * total) oraciones.
          5. Las reordena por posición original para mantener coherencia.

        Parámetros:
            summary_ratio: Fracción de oraciones a incluir (0.05 = 5%).
            max_length   : Límite de palabras en el resumen final.
        """
        import nltk
        from nltk.tokenize import sent_tokenize, word_tokenize
        from nltk.corpus import stopwords
        import string

        nltk.download('punkt',     quiet=True)
        nltk.download('punkt_tab', quiet=True)
        nltk.download('stopwords', quiet=True)

        if 'clean_text' not in self.data.columns:
            self.data['clean_text'] = self.data['text'].apply(self.clean_text)

        text      = ' '.join(self.data['clean_text'].dropna().tolist())
        sentences = sent_tokenize(text)
        if not sentences:
            return "[Corpus vacío – no se generó resumen]"

        stop_words = set(stopwords.words('english'))
        word_freq  = {}
        for sent in sentences:
            for word in word_tokenize(sent.lower()):
                if (len(word) >= 3 and not word.startswith('#')
                        and not word.isdigit()
                        and word not in stop_words
                        and word not in string.punctuation):
                    word_freq[word] = word_freq.get(word, 0) + 1

        if not word_freq:
            return "[Corpus vacío – no se generó resumen]"

        sent_scores = {sent: sum(word_freq.get(w, 0)
                                 for w in word_tokenize(sent.lower())
                                 if w not in string.punctuation)
                       for sent in sentences}

        ranked   = sorted([s for s in sent_scores if sent_scores[s] > 0],
                          key=lambda s: sent_scores[s], reverse=True)
        selected = sorted(ranked[:max(1, int(len(sentences) * summary_ratio))],
                          key=sentences.index)

        result_words, final = 0, []
        for sent in selected:
            sent_len = len(sent.split())
            if result_words + sent_len <= max_length:
                final.append(sent)
                result_words += sent_len
            elif result_words < max_length:
                final.append(sent)
                break

        return ' '.join(final) if final else "[Resumen vacío]"

    # =========================================================================
    # BLOQUE 7 – ANÁLISIS DE REDES CON NETWORKX  (AEC3) ← NUEVO
    # =========================================================================

    def build_interaction_graph(self) -> 'nx.DiGraph':
        """
        Construye un grafo dirigido de interacciones a partir de los tweets.

        Lógica del grafo:
          - Nodo    : cada usuario (@usuario) que aparece en el dataset.
          - Arista  : si el usuario A menciona a B en un tweet, se añade la
                      arista A → B con peso = número de menciones.

        Columnas requeridas en self.data: 'user_name' y 'text'.

        Justificación: modelar la red de menciones permite identificar quiénes
        son los actores más influyentes (centralidad), detectar comunidades de
        discusión y entender la estructura de difusión de información.

        Devuelve un nx.DiGraph con atributos:
          - Nodo 'tweet_count' : número de tweets que ha publicado ese usuario.
          - Arista 'weight'    : número de veces que A ha mencionado a B.
        """
        import networkx as nx

        if self.data is None:
            raise RuntimeError("Sin datos. Llama a load_data() o load_data_api() primero.")

        G = nx.DiGraph()

        # Contar tweets por usuario para añadir como atributo del nodo
        tweet_counts = self.data['user_name'].value_counts().to_dict()

        for _, row in self.data.iterrows():
            source = str(row.get('user_name', '')).strip().lower()
            text   = str(row.get('text', ''))

            if not source or source == 'nan':
                continue

            # Añadir nodo fuente con atributo tweet_count
            if source not in G:
                G.add_node(source, tweet_count=tweet_counts.get(source, 0))

            # Extraer menciones del texto original (no del clean, porque clean elimina @)
            mentions = self._extract_mentions(text)

            for target in mentions:
                if target == source:
                    continue  # Ignorar auto-menciones

                if target not in G:
                    G.add_node(target, tweet_count=tweet_counts.get(target, 0))

                if G.has_edge(source, target):
                    G[source][target]['weight'] += 1
                else:
                    G.add_edge(source, target, weight=1)

        print(f"🕸️  Grafo construido: {G.number_of_nodes()} nodos, "
              f"{G.number_of_edges()} aristas")
        return G

    def analyze_network(self, G: 'nx.DiGraph') -> dict:
        """
        Calcula métricas de red y detecta comunidades en el grafo.

        Métricas calculadas:
          - Grado de entrada (in-degree)    : cuántos usuarios mencionan a cada nodo.
          - Grado de salida (out-degree)    : cuántos usuarios menciona cada nodo.
          - Centralidad de grado (in-degree centrality): versión normalizada del in-degree.
          - Betweenness centrality          : importancia como puente entre grupos.
          - PageRank                        : influencia global en la red (mismo algoritmo que Google).
          - Detección de comunidades        : algoritmo de Louvain sobre el grafo no dirigido.

        Justificación:
          - Centralidad: identifica los 'influencers' reales de la red.
          - Betweenness: detecta nodos que actúan como puente entre comunidades.
          - PageRank: mide la influencia teniendo en cuenta la calidad (no solo cantidad)
            de los que te mencionan.
          - Louvain: agrupa usuarios con patrones de interacción similares,
            revelando comunidades temáticas o sociales.

        Devuelve un dict con métricas y genera una visualización del grafo.
        """
        import networkx as nx
        import matplotlib.pyplot as plt
        import matplotlib.cm as cm
        import numpy as np

        # ── Métricas básicas ──────────────────────────────────────────────────
        n_nodes    = G.number_of_nodes()
        n_edges    = G.number_of_edges()
        density    = nx.density(G)
        # Componentes conexas del grafo no dirigido
        n_components = nx.number_weakly_connected_components(G)

        in_degree_centrality  = nx.in_degree_centrality(G)
        out_degree_centrality = nx.out_degree_centrality(G)
        betweenness           = nx.betweenness_centrality(G, weight='weight', normalized=True)
        pagerank              = nx.pagerank(G, weight='weight', max_iter=200)

        # Top 3 por cada métrica
        top3_in_degree   = sorted(in_degree_centrality.items(),  key=lambda x: x[1], reverse=True)[:3]
        top3_betweenness = sorted(betweenness.items(),           key=lambda x: x[1], reverse=True)[:3]
        top3_pagerank    = sorted(pagerank.items(),              key=lambda x: x[1], reverse=True)[:3]

        # ── Detección de comunidades (Louvain) ────────────────────────────────
        # Louvain opera sobre grafos no dirigidos; convertimos con peso acumulado
        G_undirected = G.to_undirected(reciprocal=False)
        communities  = {}
        try:
            from community import best_partition   # python-louvain
            partition    = best_partition(G_undirected, weight='weight')
            n_communities = len(set(partition.values()))
            communities  = partition
            print(f"🔍 Louvain detectó {n_communities} comunidades")
        except ImportError:
            # Fallback: greedy modularity (disponible en NetworkX nativo)
            from networkx.algorithms.community import greedy_modularity_communities
            comms = list(greedy_modularity_communities(G_undirected, weight='weight'))
            partition     = {}
            n_communities = len(comms)
            for idx, comm in enumerate(comms):
                for node in comm:
                    partition[node] = idx
            communities = partition
            print(f"🔍 Greedy modularity detectó {n_communities} comunidades (fallback de Louvain)")

        # ── Impresión de estadísticas ──────────────────────────────────────────
        print("\n" + "=" * 55)
        print("         MÉTRICAS DE RED – RESUMEN")
        print("=" * 55)
        print(f"  Nodos              : {n_nodes:,}")
        print(f"  Aristas            : {n_edges:,}")
        print(f"  Densidad           : {density:.4f}")
        print(f"  Componentes débiles: {n_components}")
        print(f"  Comunidades        : {n_communities}")
        print("\n  Top 3 – In-degree centrality (más mencionados):")
        for node, val in top3_in_degree:
            print(f"    @{node:<20} {val:.4f}")
        print("\n  Top 3 – Betweenness centrality (puentes de red):")
        for node, val in top3_betweenness:
            print(f"    @{node:<20} {val:.4f}")
        print("\n  Top 3 – PageRank (mayor influencia global):")
        for node, val in top3_pagerank:
            print(f"    @{node:<20} {val:.4f}")
        print("=" * 55 + "\n")

        # ── Visualización ─────────────────────────────────────────────────────
        # Limitamos a los N nodos más activos para mantener el grafo legible
        MAX_NODES = 80
        if n_nodes > MAX_NODES:
            top_nodes = sorted(pagerank, key=pagerank.get, reverse=True)[:MAX_NODES]
            subG      = G.subgraph(top_nodes).copy()
            subpart   = {n: communities.get(n, 0) for n in top_nodes}
            print(f"ℹ️  Visualizando los {MAX_NODES} nodos con mayor PageRank")
        else:
            subG    = G
            subpart = communities

        fig, axes = plt.subplots(1, 2, figsize=(18, 8))

        # Panel izquierdo: grafo coloreado por comunidades
        ax1 = axes[0]
        try:
            pos = nx.spring_layout(subG, seed=42, k=0.5)
        except Exception:
            pos = nx.random_layout(subG, seed=42)

        n_comms  = max(subpart.values()) + 1 if subpart else 1
        cmap     = cm.get_cmap('tab20', n_comms)
        colors   = [cmap(subpart.get(node, 0) % n_comms) for node in subG.nodes()]
        sizes    = [300 + pagerank.get(node, 0) * 15000 for node in subG.nodes()]
        weights  = [subG[u][v]['weight'] for u, v in subG.edges()]
        max_w    = max(weights) if weights else 1

        nx.draw_networkx_nodes(subG, pos, ax=ax1, node_color=colors,
                               node_size=sizes, alpha=0.85)
        nx.draw_networkx_edges(subG, pos, ax=ax1,
                               width=[0.5 + 2.5 * (w / max_w) for w in weights],
                               alpha=0.4, arrows=True,
                               arrowstyle='->', arrowsize=10,
                               edge_color='gray')
        # Etiquetas solo para top 10 nodos (para no saturar)
        top10_labels = {n: f"@{n}" for n in
                        sorted(pagerank, key=pagerank.get, reverse=True)[:10]
                        if n in subG.nodes()}
        nx.draw_networkx_labels(subG, pos, labels=top10_labels,
                                ax=ax1, font_size=7, font_weight='bold')
        ax1.set_title("Red de menciones – Comunidades (Louvain)", fontsize=12)
        ax1.axis('off')

        # Panel derecho: distribución del grado de entrada (in-degree)
        ax2   = axes[1]
        degs  = [d for _, d in G.in_degree()]
        ax2.hist(degs, bins=min(50, max(degs) + 1) if degs else 10,
                 color='steelblue', edgecolor='white', alpha=0.85)
        ax2.set_xlabel("In-degree (veces mencionado)", fontsize=11)
        ax2.set_ylabel("Número de nodos",              fontsize=11)
        ax2.set_title("Distribución de in-degree",     fontsize=12)
        ax2.set_yscale('log')

        plt.suptitle("Análisis de red de interacciones en Twitter",
                     fontsize=14, fontweight='bold', y=1.01)
        plt.tight_layout()
        plt.savefig('network_analysis.png', dpi=150, bbox_inches='tight')
        plt.show()
        print("📈 Visualización guardada en 'network_analysis.png'")

        return {
            'n_nodes':              n_nodes,
            'n_edges':              n_edges,
            'density':              density,
            'n_components':         n_components,
            'n_communities':        n_communities,
            'communities':          communities,
            'in_degree_centrality': in_degree_centrality,
            'betweenness':          betweenness,
            'pagerank':             pagerank,
            'top3_in_degree':       top3_in_degree,
            'top3_betweenness':     top3_betweenness,
            'top3_pagerank':        top3_pagerank,
        }

    # =========================================================================
    # BLOQUE 8 – GENERACIÓN DE PROMPT + LLM LOCAL (AEC3) ← NUEVO
    # =========================================================================

    def generate_prompt_from_network(self, G: 'nx.DiGraph',
                                     metrics: dict = None) -> str:
        """
        Genera un prompt interpretativo para el LLM a partir de los insights
        del análisis de redes.

        El prompt incluye:
          - Top 3 nodos por in-degree centrality (los más mencionados).
          - Top 3 nodos por PageRank (mayor influencia global).
          - Número de comunidades detectadas.
          - Hashtag más frecuente del dataset (si hay datos de hashtags).
          - Pregunta abierta para que el LLM explique el comportamiento de la red.

        Justificación: condensar los hallazgos cuantitativos de la red en lenguaje
        natural permite que el LLM aporte un análisis interpretativo y contextual
        que va más allá de los números, conectando los patrones de la red con
        dinámicas sociales conocidas (difusión de información, influencia, etc.).

        Parámetros:
            G      : Grafo dirigido generado por build_interaction_graph().
            metrics: Dict devuelto por analyze_network(). Si es None, se calculan
                     las métricas básicas aquí.

        Devuelve el string del prompt listo para pasarse al LLM.
        """
        import networkx as nx

        # Si no se pasaron métricas precalculadas, calculamos las básicas
        if metrics is None:
            in_deg   = nx.in_degree_centrality(G)
            pagerank = nx.pagerank(G, weight='weight', max_iter=200)
            top3_in  = sorted(in_deg.items(),   key=lambda x: x[1], reverse=True)[:3]
            top3_pr  = sorted(pagerank.items(),  key=lambda x: x[1], reverse=True)[:3]
            n_nodes  = G.number_of_nodes()
            n_edges  = G.number_of_edges()
            density  = nx.density(G)
            # Comunidades básicas con fallback
            try:
                from community import best_partition
                partition     = best_partition(G.to_undirected(), weight='weight')
                n_communities = len(set(partition.values()))
            except Exception:
                n_communities = "N/D"
        else:
            top3_in       = metrics.get('top3_in_degree', [])
            top3_pr       = metrics.get('top3_pagerank',  [])
            n_nodes       = metrics.get('n_nodes',        G.number_of_nodes())
            n_edges       = metrics.get('n_edges',        G.number_of_edges())
            density       = metrics.get('density',        nx.density(G))
            n_communities = metrics.get('n_communities',  "N/D")

        # Hashtag más frecuente (si los datos están disponibles)
        top_hashtag = "N/D"
        if self.data is not None:
            try:
                if 'clean_text' not in self.data.columns:
                    self.data['clean_text'] = self.data['text'].apply(self.clean_text)
                all_tags = []
                for text in self.data['clean_text'].dropna():
                    all_tags.extend(self.extract_hashtags(text))
                if all_tags:
                    from collections import Counter
                    top_hashtag = Counter(all_tags).most_common(1)[0][0]
            except Exception:
                pass

        # Construir el prompt
        top3_in_str = ", ".join([f"@{n} ({v:.4f})" for n, v in top3_in]) or "N/D"
        top3_pr_str = ", ".join([f"@{n} ({v:.4f})" for n, v in top3_pr]) or "N/D"

        prompt = f"""Eres un experto en análisis de redes sociales y comportamiento en Twitter/X.
A continuación te proporciono los resultados de un análisis de red de menciones sobre tweets de Bitcoin.

=== DATOS DE LA RED ===
- Total de nodos (usuarios): {n_nodes}
- Total de aristas (menciones): {n_edges}
- Densidad de la red: {density:.4f}
- Comunidades detectadas (Louvain): {n_communities}

=== NODOS MÁS INFLUYENTES ===
Top 3 por in-degree centrality (usuarios más mencionados):
{top3_in_str}

Top 3 por PageRank (usuarios con mayor influencia ponderada):
{top3_pr_str}

=== TENDENCIAS DE CONTENIDO ===
Hashtag más frecuente en el dataset: #{top_hashtag}

=== PREGUNTA ===
Con base en estos datos:
1. ¿Qué patrones de comportamiento social observas en esta red de menciones?
2. ¿Por qué crees que estos usuarios tienen tanta centralidad? ¿Qué rol suelen jugar en comunidades de criptomonedas?
3. ¿Qué nos dice la densidad de la red sobre la cohesión de esta comunidad de Bitcoin en Twitter?
4. ¿Cómo podrían las {n_communities} comunidades detectadas reflejar distintas posturas o subgrupos dentro de la comunidad cripto?

Por favor, da un análisis interpretativo detallado basado en estos insights."""

        print(f"📝 Prompt generado ({len(prompt.split())} palabras)")
        return prompt

    def chat_local_llm(self, prompt: str = None,
                       model: str = "gemma3",
                       ollama_url: str = "http://localhost:11434",
                       stream: bool = True) -> str:
        """
        Levanta un chat interactivo con un LLM local ejecutándose en Ollama.

        Modo de uso:
          A) Con prompt automático (generado por generate_prompt_from_network):
             Se envía el prompt como primer mensaje y se muestra la respuesta.
             Luego se abre el modo chat interactivo para continuar la conversación.

          B) Sin prompt (prompt=None):
             Entra directamente en modo chat interactivo.

        Flujo conversacional:
          - El historial completo se mantiene en memoria y se pasa en cada
            petición a Ollama, simulando una conversación con contexto.
          - Cada turno del modelo incluye todos los mensajes anteriores, lo que
            permite hacer preguntas de seguimiento ("¿puedes explicar más el
            punto 2?") y obtener respuestas coherentes.
          - Para salir escribe 'salir', 'exit' o 'quit'.

        Parámetros:
            prompt     : Prompt inicial (generalmente el de la red). None = chat libre.
            model      : Nombre del modelo en Ollama (por defecto 'gemma3').
            ollama_url : URL base de la instancia de Ollama (por defecto localhost).
            stream     : Si True, muestra la respuesta token a token (streaming).

        Requisitos:
            - Ollama instalado y en ejecución: https://ollama.com
            - Modelo descargado: ollama pull gemma3
            - Puerto 11434 accesible (default de Ollama).

        Devuelve la última respuesta del modelo como string.
        """
        import json as _json

        api_chat_url = f"{ollama_url.rstrip('/')}/api/chat"

        def _call_ollama(messages: list) -> str:
            """Envía los mensajes a Ollama y devuelve la respuesta completa."""
            payload = {
                "model":    model,
                "messages": messages,
                "stream":   stream
            }
            try:
                resp = requests.post(api_chat_url, json=payload,
                                     timeout=300, stream=stream)
                resp.raise_for_status()
            except requests.exceptions.ConnectionError:
                raise RuntimeError(
                    f"No se puede conectar a Ollama en {ollama_url}.\n"
                    "Asegúrate de que Ollama está en ejecución: ollama serve\n"
                    f"Y de que el modelo está descargado: ollama pull {model}"
                )
            except requests.exceptions.RequestException as e:
                raise RuntimeError(f"Error en la petición a Ollama: {e}")

            full_response = ""
            if stream:
                print(f"\n🤖 {model}: ", end="", flush=True)
                for line in resp.iter_lines():
                    if line:
                        try:
                            chunk = _json.loads(line.decode('utf-8'))
                            token = chunk.get('message', {}).get('content', '')
                            print(token, end="", flush=True)
                            full_response += token
                            if chunk.get('done', False):
                                break
                        except _json.JSONDecodeError:
                            continue
                print()  # Salto de línea al terminar
            else:
                data          = resp.json()
                full_response = data.get('message', {}).get('content', '')
                print(f"\n🤖 {model}: {full_response}")

            return full_response

        # ── Verificar que Ollama está activo ──────────────────────────────────
        try:
            ping = requests.get(f"{ollama_url.rstrip('/')}/api/tags", timeout=5)
            available_models = [m['name'] for m in ping.json().get('models', [])]
            model_available  = any(model in m for m in available_models)
            if not model_available:
                print(f"⚠️  Modelo '{model}' no encontrado en Ollama.")
                print(f"   Modelos disponibles: {available_models or 'ninguno'}")
                print(f"   Ejecuta: ollama pull {model}")
        except requests.exceptions.ConnectionError:
            raise RuntimeError(
                f"Ollama no está en ejecución. Inicia con: ollama serve\n"
                f"Luego descarga el modelo: ollama pull {model}"
            )

        # ── Historial de conversación ─────────────────────────────────────────
        conversation = []
        last_response = ""

        # Si hay prompt inicial, procesarlo primero
        if prompt:
            print("\n" + "=" * 60)
            print("🚀 Enviando análisis de red al LLM...")
            print("=" * 60)
            conversation.append({"role": "user", "content": prompt})
            last_response = _call_ollama(conversation)
            conversation.append({"role": "assistant", "content": last_response})

        # ── Modo chat interactivo ─────────────────────────────────────────────
        print("\n" + "=" * 60)
        print(f"💬 Chat interactivo con {model} (escribe 'salir' para terminar)")
        print("=" * 60)

        while True:
            try:
                user_input = input("\n👤 Tú: ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\n\n👋 Chat terminado.")
                break

            if user_input.lower() in ('salir', 'exit', 'quit', 'q', ''):
                print("👋 Chat terminado.")
                break

            conversation.append({"role": "user", "content": user_input})
            last_response = _call_ollama(conversation)
            conversation.append({"role": "assistant", "content": last_response})

        return last_response

    # =========================================================================
    # BLOQUE 9 – EXPORTACIÓN DE RESULTADOS  (AEC2 + AEC3)
    # =========================================================================

    def export_results(self, output_dir: str = "output",
                       topics: list = None) -> None:
        """
        Exporta todos los resultados del pipeline a archivos en output_dir:
          - tweets_clean.csv         : Tweets limpios + columnas de análisis.
          - hashtags_overall.csv     : Frecuencia global de hashtags.
          - hashtags_by_user.csv     : Frecuencia por usuario.
          - hashtags_by_date.csv     : Frecuencia por fecha.
          - sentiment_results.csv    : Polaridad y subjetividad (si se calcularon).
          - topics_lda.txt           : Tópicos LDA (si se calcularon).
          - summary.txt              : Resumen extractivo del corpus.
        """
        if self.data is None:
            raise RuntimeError("Sin datos cargados.")

        out = Path(output_dir)
        out.mkdir(parents=True, exist_ok=True)

        if 'clean_text' not in self.data.columns:
            self.data['clean_text'] = self.data['text'].apply(self.clean_text)

        self.data.to_csv(out / 'tweets_clean.csv', index=False, encoding='utf-8')
        print(f"💾 tweets_clean.csv ({len(self.data):,} filas)")

        analytics = self.analytics_hashtags_extended()
        for key, fname in [('overall',  'hashtags_overall.csv'),
                           ('by_user',  'hashtags_by_user.csv'),
                           ('by_date',  'hashtags_by_date.csv')]:
            analytics[key].to_csv(out / fname, index=False, encoding='utf-8')
            print(f"💾 {fname} ({len(analytics[key]):,} filas)")

        if 'sentiment_polarity' in self.data.columns:
            cols = [c for c in ['user_name', 'date', 'text', 'clean_text',
                                'sentiment_polarity', 'sentiment_subjectivity']
                    if c in self.data.columns]
            self.data[cols].to_csv(out / 'sentiment_results.csv',
                                   index=False, encoding='utf-8')
            print(f"💾 sentiment_results.csv ({len(self.data):,} filas)")

        if topics:
            lines = ["LDA Topics\n" + "=" * 40 + "\n"]
            for i, topic in enumerate(topics, 1):
                lines.append(f"Topic {i}: {', '.join(topic)}\n")
            (out / 'topics_lda.txt').write_text(''.join(lines), encoding='utf-8')
            print("💾 topics_lda.txt")

        summary = self.parse_and_summarize(summary_ratio=0.01)
        (out / 'summary.txt').write_text(summary, encoding='utf-8')
        print(f"💾 summary.txt ({len(summary.split())} palabras)")
        print(f"\n✅ Todos los resultados exportados a '{out.resolve()}'")
