#====================================================================================================#
#                                                                                                    #
#                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        #
#      AEC2 - BAIN                                       ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       #
#                                                        ██║   ██║█████╗██║   ███████║██║  ██║       #
#      created:        08/04/2026  -  01:00:51           ██║   ██║╚════╝██║   ██╔══██║██║  ██║       #
#      last change:    25/04/2026  -  12:14:43           ╚██████╔╝      ██║   ██║  ██║██████╔╝       #
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
    """Extracción, limpieza y análisis de tweets."""

    _RE_URL = re.compile(r'https?://\S+|www\.\S+', re.IGNORECASE)
    _RE_MENTION = re.compile(r'@\w+')
    _RE_HASHTAG = re.compile(r'#(\w+)')
    _RE_SPECIAL = re.compile(r'[^\w\s#]', re.UNICODE)
    _RE_SPACES = re.compile(r'\s+')

    def __init__(self, source: str = None, chunksize: int = 100_000):
        self.source = source
        self.data = None
        self.chunksize = chunksize

    # Inicializador de la clase, aqui apunto el source al archivo local de datos (CSV o JSON) o None si voy
    # a usar load_data_api(). self.data es el DataFrame principal donde se cargan los tweets.
    # chunksize es el tamaño de bloque para leer CSVs gigantes


    def _parse_api_response(self, response_json: dict) -> list:
        """Parse API response handling multiple formats: tweets, data, timeline, results."""
        tweets_list = None
        for key in ['tweets', 'data', 'timeline', 'results', 'statuses']:
            if key in response_json and isinstance(response_json[key], list):
                tweets_list = response_json[key]
                break

        if tweets_list is None:
            raise ValueError(f"No tweets. Keys: {list(response_json.keys())}")

        rows = []
        for t in tweets_list:
            if not isinstance(t, dict):
                continue
            text = t.get('text') or t.get('full_text') or t.get('body') or ''
            user = t.get('user_name') or t.get('author_id') or t.get('user', {}).get('name') or 'unknown'
            date = t.get('date') or t.get('created_at') or t.get('timestamp') or ''
            if text.strip():
                rows.append({'user_name': str(user).strip(), 'date': str(date).strip(), 'text': str(text).strip()})

        return rows if rows else (_ for _ in ()).throw(ValueError("No valid tweets in response"))

    # con este metodo privado normalizo las respuestas de la API de Twitter. Distintos endpoints y versiones
    # de RapidAPI devuelven la lista de tweets bajo diferentes nombres de claves ('tweets', 'data',
    # 'timeline', etc.), así que intento encontrarla de forma robusta. Si la encuentro, normalizo
    # cada tweet a un formato común (user_name, date, text) para que el resto de métodos funcionen.
    def load_data_api(self, query: str, max_results: int = 100, output_file: str = "tweets.csv") -> pd.DataFrame:
        """Extract tweets from RapidAPI Twitter endpoint."""
        try:
            resp = requests.get(
                "https://twitter-api45.p.rapidapi.com/search.php",
                headers={"X-RapidAPI-Key": os.environ.get("RAPIDAPI_KEY", ""),
                         "X-RapidAPI-Host": "twitter-api45.p.rapidapi.com"},
                params={"query": query, "count": max_results}, timeout=15
            )
            resp.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"API request failed: {e}")

        rows = self._parse_api_response(resp.json())
        self.data = pd.DataFrame(rows)
        self.data.to_csv(output_file, index=False, encoding="utf-8")
        self.source = output_file
        print(f" {len(self.data)} tweets extracted and saved to '{output_file}'")
        return self.data

    # Extraigo tweets en tiempo real desde la API de RapidAPI usando credenciales de variable de entorno.
    # Leo la clave RAPIDAPI_KEY desde os.environ para evitar exponerla en el código. Luego hago una
    # petición GET al endpoint search.php con los parámetros query (hashtag/búsqueda) y count (número
    # de tweets). El parser robusto convierte la respuesta al formato estándar. Finalmente guardo en
    # CSV local para poder reutilizar los datos sin hacer más llamadas a la API (que tiene límites).
    def load_data(self) -> pd.DataFrame:
        """Load data from local CSV or JSON."""
        ext = Path(self.source).suffix.lower()

        if ext == '.json':
            self.data = pd.read_json(self.source, encoding='utf-8')
        elif ext == '.csv':
            chunks = pd.read_csv(self.source, encoding='utf-8', chunksize=self.chunksize, low_memory=False)
            self.data = pd.concat(chunks, ignore_index=True)
        else:
            raise ValueError(f"Unsupported format: {ext}")

        self.data.columns = [c.strip().replace('\r', '') for c in self.data.columns]
        print(f" Loaded {len(self.data):,} rows – {list(self.data.columns)}")
        return self.data

    # Cargo datos desde archivo local (CSV o JSON). Para archivos CSV grandes uso chunksize para no
    # saturar la RAM: leo el archivo en pedazos y los concateno. También limpio nombres de columnas
    # por si vienen con espacios o caracteres raros (CRLF). El método detecta automáticamente el
    # formato por la extensión del archivo y lo carga apropiadamente.

    def clean_text(self, text: str) -> str:
        """Normalize text: lowercase, remove URLs/mentions/emojis, keep hashtags."""
        if not isinstance(text, str):
            text = str(text) if pd.notna(text) else ''
        text = text.strip().lower()
        text = self._RE_URL.sub(' ', text)
        text = self._RE_MENTION.sub(' ', text)
        text = ''.join(ch for ch in text if unicodedata.category(ch) not in ('So', 'Sk', 'Cs'))
        text = self._RE_SPECIAL.sub(' ', text)
        return self._RE_SPACES.sub(' ', text).strip()

    # Normaliza y limpia cada tweet de manera sistemática. Paso a minúsculas, elimino URLs
    # (amenudo enlaces spammers), menciones (@usuario), emojis (usando categorías Unicode), y
    # caracteres especiales; pero CONSERVO hashtags (#bitcoin) porque son cruciales para el análisis.
    # Colapso espacios múltiples al final para tener texto limpio. 
    def extract_hashtags(self, text: str) -> list:
        """Extract unique hashtags from text."""
        if not isinstance(text, str):
            return []
        seen, result = set(), []
        for tag in self._RE_HASHTAG.findall(text):
            t = tag.lower()
            if t not in seen:
                seen.add(t)
                result.append(t)
        return result

    # Extraigo hashtags únicos de un tweet usando regex. Busco el patrón #(\w+) y devuelvo una lista
    # sin duplicados manteniendo el orden de aparición. Esto se usa tanto para análisis like frecuencia
    # de hashtags como para filtrado en LDA (eliminamos hashtags antes de modelar tópicos porque no
    # son palabras "reales" y añaden ruido).

    def analytics_hashtags_extended(self) -> dict:
        """Analyze hashtags: global frequency, by user, by date."""
        if self.data is None:
            raise RuntimeError("No data loaded. Call load_data() or load_data_api() first.")

        df = self.data.copy()
        df['clean_text'] = df['text'].apply(self.clean_text)
        df['hashtags'] = df['clean_text'].apply(self.extract_hashtags)
        df['date'] = pd.to_datetime(df['date'], utc=True, errors='coerce').dt.date

        df_exp = df.explode('hashtags').dropna(subset=['hashtags'])
        df_exp = df_exp[df_exp['hashtags'].str.strip() != ''].rename(columns={'hashtags': 'hashtag'})

        overall = df_exp.groupby('hashtag', as_index=False).size().rename(columns={'size': 'frequency'}).sort_values('frequency', ascending=False)
        by_user = df_exp.groupby(['user_name', 'hashtag'], as_index=False).size().rename(columns={'size': 'frequency'}).sort_values('frequency', ascending=False)
        by_date = df_exp.groupby(['date', 'hashtag'], as_index=False).size().rename(columns={'size': 'frequency'}).sort_values(['date', 'frequency'], ascending=[True, False])

        print(f" {len(overall)} unique hashtags found")
        return {'overall': overall, 'by_user': by_user, 'by_date': by_date}

    # Análisis profundo de hashtags en tres perspectivas: frecuencia global de cada
    # hashtag sin contexto ¿cuál es el más popular?,  qué usuarios usan cada hashtag
    # con qué frecuencia ayuda a detectar bots que spammean el mismo hashtag y 
    # evolución temporal  ¿está el hashtag en tendencia? Todos los análisis se hacen sobre
    # datos limpios y con hashtags normalizados (minúsculas, sin duplicados).
    def generate_hashtag_wordcloud(self, overall_df: pd.DataFrame = None, max_words: int = 100, figsize: tuple = (10, 6)):
        """Generate wordcloud from hashtag frequencies."""
        import matplotlib.pyplot as plt
        from wordcloud import WordCloud

        if overall_df is None:
            overall_df = self.analytics_hashtags_extended()['overall']

        freq_dict = dict(zip(overall_df['hashtag'], overall_df['frequency']))
        wc = WordCloud(width=figsize[0] * 100, height=figsize[1] * 100, max_words=max_words,
                       background_color='white', colormap='viridis').generate_from_frequencies(freq_dict)

        plt.figure(figsize=figsize)
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.tight_layout()
        plt.show()

    # Genera una nube de palabras (wordcloud) basada en la frecuencia de hashtags. WordCloud interpreta
    # tamaños relativos: hashtags más frecuentes aparecen más grandes. Es una visualización rápida y
    # efectiva para ver de un vistazo cuál es el vocabulario dominante del corpus sin necesidad de
    # tablas. Si no le paso un DataFrame de frecuencias, calculo uno sobre la marcha.

    def model_topics(self, num_topics: int = 5, passes: int = 10, min_word_len: int = 3) -> list:
        """LDA topic modeling with aggressive filtering (stopwords, numbers, short words, hashtags)."""
        try:
            import gensim
            from gensim import corpora
        except ImportError:
            raise ImportError("gensim required. Use Python 3.11-3.13 for compatibility.")

        import nltk
        from nltk.corpus import stopwords
        nltk.download('stopwords', quiet=True)
        stop_words = set(stopwords.words('english'))

        if 'clean_text' not in self.data.columns:
            self.data['clean_text'] = self.data['text'].apply(self.clean_text)

        texts = []
        for text in self.data['clean_text'].dropna():
            words = [w.lower() for w in text.split()
                     if len(w) >= min_word_len and not w.startswith('#') and not w.isdigit()
                     and w not in stop_words and not all(c.isdigit() or c in '-.' for c in w)]
            if words:
                texts.append(words)

        if not texts:
            raise ValueError("No words after filtering. Corpus too small.")

        dictionary = corpora.Dictionary(texts)
        corpus = [dictionary.doc2bow(text) for text in texts]
        lda_model = gensim.models.LdaModel(corpus, num_topics=num_topics, id2word=dictionary, 
                                           passes=passes, random_state=42, workers=1)

        topics = [[w for w, _ in t[1]] for t in lda_model.show_topics(num_topics=num_topics, num_words=10, formatted=False)]
        print(f" LDA: {num_topics} topics ({len(texts)} docs)")
        return topics

    # Modelado de tópicos con Latent Dirichlet Allocation (LDA). El algoritmo descubre temas
    # latentes en el corpus de forma no supervisada. CRÍTICO: filtrado agresivo antes de entrenar:
    # elimino stopwords ingleses (the, is, etc.), números, palabras muy cortas (<3 caracteres),
    # y hashtags - todo esto es ruido que degradaría la calidad de los tópicos. Uso gensim que es
    # la librería estándar. El modelo se entrena con N iteraciones ppara convergencia.
    # Devuelvo los tópicos como listas de palabras más relevantes de cada tema.
    def analyze_sentiment(self, method: str = 'textblob') -> pd.DataFrame:
        """Analyze sentiment (polarity & subjectivity) using TextBlob or spaCy."""
        if 'clean_text' not in self.data.columns:
            self.data['clean_text'] = self.data['text'].apply(self.clean_text)

        if method == 'textblob':
            from textblob import TextBlob
            self.data['sentiment_polarity'] = self.data['clean_text'].apply(lambda x: TextBlob(x).sentiment.polarity)
            self.data['sentiment_subjectivity'] = self.data['clean_text'].apply(lambda x: TextBlob(x).sentiment.subjectivity)
        elif method == 'spacy':
            import spacy
            from spacytextblob.spacytextblob import SpacyTextBlob
            nlp = spacy.load('en_core_web_sm')
            nlp.add_pipe('spacytextblob')
            self.data['sentiment_polarity'] = self.data['clean_text'].apply(lambda x: nlp(x)._.polarity)
            self.data['sentiment_subjectivity'] = self.data['clean_text'].apply(lambda x: nlp(x)._.subjectivity)
        else:
            raise ValueError(f"Method '{method}' not supported. Use 'textblob' or 'spacy'.")

        return self.data

    # Análisis de sentimiento tweet por tweet. Calculo dos métricas por cada uno: (1) Polaridad:
    # de -1 (muy negativo) a +1 (muy positivo). (2) Subjetividad: de 0 (objetivo/hechos) a 1
    # (subjetivo/opinión). TextBlob es rápido pero simple; spaCy con spacytextblob es más preciso
    # pero requiere modelos descargados. Los resultados se guardan como columnas nuevas en el DataFrame.
    def parse_and_summarize(self, summary_ratio: float = 0.05, max_length: int = 500) -> str:
        """Extractive summarization: select top sentences by word frequency."""
        import nltk
        from nltk.tokenize import sent_tokenize, word_tokenize
        from nltk.corpus import stopwords
        import string

        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)

        if 'clean_text' not in self.data.columns:
            self.data['clean_text'] = self.data['text'].apply(self.clean_text)

        text = ' '.join(self.data['clean_text'].dropna().tolist())
        sentences = sent_tokenize(text)
        if not sentences:
            return "[Empty summary]"

        stop_words = set(stopwords.words('english'))
        word_freq = {}
        for sent in sentences:
            for word in word_tokenize(sent.lower()):
                if (len(word) >= 3 and not word.startswith('#') and not word.isdigit() 
                    and word not in stop_words and word not in string.punctuation):
                    word_freq[word] = word_freq.get(word, 0) + 1

        if not word_freq:
            return "[Empty summary]"

        sent_scores = {sent: sum(word_freq.get(w, 0) for w in word_tokenize(sent.lower()) if w not in string.punctuation)
                       for sent in sentences}

        ranked = sorted([s for s in sent_scores if sent_scores[s] > 0], key=lambda s: sent_scores[s], reverse=True)
        selected = sorted(ranked[:max(1, int(len(sentences) * summary_ratio))], key=sentences.index)

        result_words, final = 0, []
        for sent in selected:
            sent_len = len(sent.split())
            if result_words + sent_len <= max_length:
                final.append(sent)
                result_words += sent_len
            elif result_words < max_length:
                final.append(sent)
                break

        return ' '.join(final) if final else "[Empty summary]"

    # Generación de resumen extractivo: selecciono las oraciones más relevantes del corpus basándome
    # en frecuencia de palabras clave. Primero tokenizo en oraciones, luego calculo frecuencia de cada
    # palabra (ignorando stopwords, puntuación, etc.). Después puntúo cada oración por suma de frecuencias
    # de sus palabras - oraciones con palabras más frecuentes son "más importantes". Selecciono el top
    # summary_ratio (ej. 5%) y las reordeno por posición original para mantener coherencia. Limito a
    # max_length palabras para no generar resúmenes enormes. 

    # =========================================================================
    # UNIDAD 6 – ANÁLISIS DE REDES E INTEGRACIÓN DE LLMs
    # =========================================================================

    def build_interaction_graph(self) -> "nx.DiGraph":
        """
        Construye un grafo dirigido de interacciones a partir de menciones en tweets.

        Cada nodo es un usuario (user_name).  Para cada tweet que contenga una o
        más menciones (@usuario), se añade una arista dirigida desde el autor del
        tweet hacia cada usuario mencionado.  Si la arista ya existe se incrementa
        su atributo 'weight' para reflejar la frecuencia de interacción.

        Requiere que self.data tenga las columnas 'user_name' y 'text'.

        Returns
        -------
        nx.DiGraph
            Grafo de interacciones listo para analizar con analyze_network().
        """
        import networkx as nx

        if self.data is None:
            raise RuntimeError("No data loaded. Call load_data() or load_data_api() first.")

        required = {'user_name', 'text'}
        if not required.issubset(self.data.columns):
            raise ValueError(f"Dataset must contain columns: {required}")

        G = nx.DiGraph()

        # Patrón para extraer menciones (@usuario) del texto crudo
        _RE_MENTION_EXTRACT = re.compile(r'@(\w+)')

        for _, row in self.data.iterrows():
            author = str(row['user_name']).strip().lower()
            text   = str(row['text']) if pd.notna(row['text']) else ''
            mentioned = {m.lower() for m in _RE_MENTION_EXTRACT.findall(text)}

            # Añado el nodo autor aunque no mencione a nadie (grafo con nodos aislados)
            if not G.has_node(author):
                G.add_node(author)

            for target in mentioned:
                if target == author:
                    continue                      # ignorar auto-menciones
                if not G.has_node(target):
                    G.add_node(target)
                if G.has_edge(author, target):
                    G[author][target]['weight'] += 1
                else:
                    G.add_edge(author, target, weight=1)

        print(f"[Graph] Nodes: {G.number_of_nodes():,}  |  Edges: {G.number_of_edges():,}")
        return G

    # El grafo es dirigido (DiGraph) porque la interacción A→B (A menciona a B) no implica B→A.
    # El peso de cada arista cuenta cuántas veces el autor mencionó a ese usuario, lo que permite
    # detectar relaciones especialmente fuertes (o cuentas bot que siempre mencionan al mismo target).
    # Construir este grafo es la base del análisis de redes: una vez tenemos la estructura podemos
    # calcular centralidad, detectar comunidades y entender quiénes son los actores más influyentes.

    def analyze_network(self, G: "nx.DiGraph") -> dict:
        """
        Calcula métricas de red y detecta comunidades (algoritmo de Louvain).

        Métricas calculadas
        -------------------
        - in_degree_centrality  : importancia por quién apunta a ti (quién recibe menciones)
        - out_degree_centrality : importancia por a quién apuntas
        - betweenness_centrality: nodos puente entre partes de la red
        - pagerank              : influencia global propagada por la red
        - Detección comunidades : algoritmo de Louvain sobre versión no-dirigida

        Parameters
        ----------
        G : nx.DiGraph
            Grafo devuelto por build_interaction_graph().

        Returns
        -------
        dict con claves:
            'in_degree', 'out_degree', 'betweenness', 'pagerank',
            'communities', 'top_nodes'
        """
        import networkx as nx
        import matplotlib.pyplot as plt
        import matplotlib.cm as cm
        import numpy as np

        if G.number_of_nodes() == 0:
            raise ValueError("Graph is empty – nothing to analyze.")

        # --- Métricas de centralidad ---------------------------------------------
        in_deg   = nx.in_degree_centrality(G)
        out_deg  = nx.out_degree_centrality(G)
        # betweenness sobre grafo no-dirigido para mayor relevancia en redes pequeñas
        G_und    = G.to_undirected()
        between  = nx.betweenness_centrality(G_und, normalized=True)
        pr       = nx.pagerank(G, alpha=0.85, max_iter=200)

        # --- Detección de comunidades (Louvain) ----------------------------------
        try:
            from community import best_partition          # python-louvain
            partition = best_partition(G_und)
            n_communities = len(set(partition.values()))
        except ImportError:
            # Fallback: greedy modularity (networkx nativo)
            communities_gen = nx.algorithms.community.greedy_modularity_communities(G_und)
            partition = {}
            for cid, members in enumerate(communities_gen):
                for node in members:
                    partition[node] = cid
            n_communities = len(set(partition.values()))

        # --- Top-3 nodos por cada métrica ----------------------------------------
        def _top3(metric_dict):
            return sorted(metric_dict.items(), key=lambda x: x[1], reverse=True)[:3]

        top_nodes = {
            'in_degree'   : _top3(in_deg),
            'out_degree'  : _top3(out_deg),
            'betweenness' : _top3(between),
            'pagerank'    : _top3(pr),
        }

        # --- Estadísticas generales -----------------------------------------------
        print("\n" + "=" * 55)
        print("  NETWORK ANALYSIS REPORT")
        print("=" * 55)
        print(f"  Nodes            : {G.number_of_nodes():>10,}")
        print(f"  Edges            : {G.number_of_edges():>10,}")
        print(f"  Communities      : {n_communities:>10,}")
        density = nx.density(G)
        print(f"  Density          : {density:>10.6f}")
        try:
            avg_cc = nx.average_clustering(G_und)
            print(f"  Avg. Clustering  : {avg_cc:>10.4f}")
        except Exception:
            pass
        print("-" * 55)
        for metric, top in top_nodes.items():
            print(f"  Top-3 by {metric}:")
            for rank, (node, val) in enumerate(top, 1):
                print(f"      {rank}. {node:<25s} {val:.4f}")
        print("=" * 55 + "\n")

        # --- Visualización -------------------------------------------------------
        # Limitamos el grafo a los 100 nodos de mayor PageRank para no colapsar matplotlib
        top100 = sorted(pr, key=pr.get, reverse=True)[:100]
        subG   = G.to_undirected().subgraph(top100).copy()

        node_colors = [partition.get(n, 0) for n in subG.nodes()]
        node_sizes  = [3000 * pr.get(n, 0) + 20 for n in subG.nodes()]

        fig, axes = plt.subplots(1, 2, figsize=(18, 8))

        # Subplot 1: grafo de interacciones
        ax1 = axes[0]
        pos = nx.spring_layout(subG, seed=42, k=0.5)
        nx.draw_networkx(
            subG, pos=pos, ax=ax1,
            node_color=node_colors, node_size=node_sizes,
            cmap=cm.tab20, font_size=6, font_color='black',
            edge_color='#aaaaaa', alpha=0.85,
            with_labels=len(subG.nodes()) <= 40,
            arrows=False,
        )
        ax1.set_title("Interaction Graph – Top 100 nodes by PageRank\n(color = community)", fontsize=11)
        ax1.axis('off')

        # Subplot 2: distribución de grados (in-degree)
        ax2 = axes[1]
        in_degrees = [d for _, d in G.in_degree()]
        ax2.hist(in_degrees, bins=40, color='steelblue', edgecolor='white', log=True)
        ax2.set_xlabel('In-Degree (mentions received)')
        ax2.set_ylabel('Number of nodes (log scale)')
        ax2.set_title('In-Degree Distribution (power-law typical of social networks)', fontsize=11)

        plt.suptitle('Network Analysis – Bitcoin Tweets Interaction Graph', fontsize=13, fontweight='bold')
        plt.tight_layout()
        plt.savefig('network_analysis.png', dpi=120, bbox_inches='tight')
        plt.show()
        print("[Graph] Visualization saved to 'network_analysis.png'")

        return {
            'in_degree'    : in_deg,
            'out_degree'   : out_deg,
            'betweenness'  : between,
            'pagerank'     : pr,
            'communities'  : partition,
            'top_nodes'    : top_nodes,
            'n_communities': n_communities,
        }

    # Usamos in-degree porque en Twitter recibir muchas menciones es señal de influencia real.
    # Betweenness mide nodos "puente" que conectan grupos distintos: actores clave en difusión
    # de información.  PageRank pondera no solo cuántos enlaces recibes, sino la importancia de
    # quienes te mencionan – el mismo algoritmo que usa Google. La detección de comunidades
    # (Louvain) agrupa usuarios que interactúan más entre sí, revelando "clústeres" temáticos
    # o sociales. Limitamos la visualización a 100 nodos para que sea legible.

    def generate_prompt_from_network(self, G: "nx.DiGraph") -> str:
        """
        Genera un prompt estructurado para el LLM a partir de los insights del análisis
        de redes.

        Extrae automáticamente:
        - Top-3 nodos por centralidad (PageRank y betweenness)
        - Hashtag más frecuente del dataset
        - Número de comunidades detectadas

        Parameters
        ----------
        G : nx.DiGraph  – grafo devuelto por build_interaction_graph()

        Returns
        -------
        str – prompt listo para pasarse a chat_local_llm()
        """
        import networkx as nx

        if G.number_of_nodes() == 0:
            raise ValueError("Empty graph – run build_interaction_graph() first.")

        # --- PageRank & betweenness sobre el grafo completo ----------------------
        pr        = nx.pagerank(G, alpha=0.85, max_iter=200)
        G_und     = G.to_undirected()
        between   = nx.betweenness_centrality(G_und, normalized=True)

        top3_pr   = sorted(pr.items(),      key=lambda x: x[1], reverse=True)[:3]
        top3_bt   = sorted(between.items(), key=lambda x: x[1], reverse=True)[:3]

        # --- Detección de comunidades --------------------------------------------
        try:
            from community import best_partition
            partition     = best_partition(G_und)
            n_communities = len(set(partition.values()))
        except ImportError:
            communities_gen = nx.algorithms.community.greedy_modularity_communities(G_und)
            n_communities   = sum(1 for _ in communities_gen)

        # --- Hashtag más frecuente del dataset -----------------------------------
        top_hashtag = "N/A"
        if self.data is not None and 'text' in self.data.columns:
            analytics   = self.analytics_hashtags_extended()
            overall     = analytics['overall']
            if not overall.empty:
                top_hashtag = overall.iloc[0]['hashtag']

        # --- Construcción del prompt ---------------------------------------------
        pr_lines = "\n".join(
            f"   {i+1}. @{node}  (PageRank={val:.4f})"
            for i, (node, val) in enumerate(top3_pr)
        )
        bt_lines = "\n".join(
            f"   {i+1}. @{node}  (Betweenness={val:.4f})"
            for i, (node, val) in enumerate(top3_bt)
        )

        prompt = f"""You are a social media analyst specializing in cryptocurrency communities.

I have analyzed a Twitter interaction network built from Bitcoin-related tweets.
Below are the key insights extracted from the graph analysis:

NETWORK STATS
-------------
- Total nodes (users): {G.number_of_nodes():,}
- Total edges (mention interactions): {G.number_of_edges():,}
- Detected communities (Louvain): {n_communities}

TOP-3 USERS BY PAGERANK (most influential – receiving high-quality mentions):
{pr_lines}

TOP-3 USERS BY BETWEENNESS CENTRALITY (key bridges between communities):
{bt_lines}

MOST FREQUENT HASHTAG: #{top_hashtag}

Based on these findings, please:
1. Explain what the network structure (density, communities) tells us about the Bitcoin Twitter community.
2. Speculate on why these specific users hold central positions – are they likely journalists, influencers, or bots?
3. Discuss what the dominant hashtag (#{ top_hashtag}) reveals about current community sentiment.
4. Suggest what marketing or research actions would be most effective given this network topology.

Provide a concise but insightful analysis (around 300 words)."""

        print("[Prompt] Generated successfully.")
        print("-" * 60)
        print(prompt)
        print("-" * 60)
        return prompt

    # El prompt está diseñado para aprovechar los insights más relevantes del análisis de red:
    # PageRank identifica usuarios con impacto real (no solo los que más tuitean), mientras que
    # betweenness señala intermediarios clave en la difusión.  Pasamos estos datos al LLM para
    # que genere interpretaciones cualitativas que un algoritmo no puede producir directamente:
    # "¿por qué este usuario es central?" requiere razonamiento contextual.

    def chat_local_llm(self, prompt: str = None,
                       model_name: str = "google/gemma-2-2b-it",
                       max_new_tokens: int = 512,
                       temperature: float = 0.7) -> None:
        """
        Levanta un modelo LLM preentrenado (por defecto Gemma-2-2B-it, compatible con
        la mayoría de GPUs de consumo y con Google Colab gratuito) y permite la
        interacción en modo chat interactivo.

        Si se proporciona `prompt` (generado por generate_prompt_from_network), se usa
        como mensaje inicial y el modelo genera una respuesta automática que se añade
        al historial de conversación.  Después el usuario puede continuar dialogando
        en un bucle interactivo (escribe 'exit' para salir).

        Nota sobre el modelo
        --------------------
        El enunciado menciona "google/gemma-4-E2B-it".  En la práctica ese modelo no
        existe públicamente en HuggingFace; el equivalente descargable es
        "google/gemma-2-2b-it" (2 B parámetros, requiere ~6 GB VRAM / ~8 GB RAM).
        Para sistemas sin GPU suficiente se puede sustituir por:
            - "TinyLlama/TinyLlama-1.1B-Chat-v1.0"  (muy ligero, <4 GB RAM)
            - Llamada a la API de Gemini (ver api_llm_fallback())

        Parameters
        ----------
        prompt          : str  – mensaje inicial (opcional).
        model_name      : str  – identificador HuggingFace del modelo.
        max_new_tokens  : int  – tokens máximos a generar por respuesta.
        temperature     : float– creatividad del modelo (0=determinista, 1=aleatorio).
        """
        try:
            import torch
            from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
        except ImportError:
            raise ImportError(
                "transformers and torch are required.\n"
                "Install with: pip install transformers torch accelerate"
            )

        print(f"\n[LLM] Loading model '{model_name}' …")
        print("      (first run downloads weights; may take a few minutes)\n")

        device = "cuda" if torch.cuda.is_available() else "cpu"
        dtype  = torch.float16 if device == "cuda" else torch.float32

        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model     = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=dtype,
            device_map="auto" if device == "cuda" else None,
            low_cpu_mem_usage=True,
        )
        if device == "cpu":
            model = model.to(device)

        model.eval()
        print(f"[LLM] Model loaded on {device.upper()}.\n")

        # Historial de conversación en formato chat
        history: list[dict] = []

        def _generate(user_message: str) -> str:
            """Genera una respuesta dado el historial actual."""
            history.append({"role": "user", "content": user_message})

            # Construimos el prompt en formato instruction-following estándar
            chat_prompt = ""
            for turn in history:
                role    = turn["role"]
                content = turn["content"]
                if role == "user":
                    chat_prompt += f"<start_of_turn>user\n{content}<end_of_turn>\n"
                else:
                    chat_prompt += f"<start_of_turn>model\n{content}<end_of_turn>\n"
            chat_prompt += "<start_of_turn>model\n"

            inputs = tokenizer(chat_prompt, return_tensors="pt").to(device)
            with torch.no_grad():
                output_ids = model.generate(
                    **inputs,
                    max_new_tokens=max_new_tokens,
                    temperature=temperature,
                    do_sample=temperature > 0,
                    pad_token_id=tokenizer.eos_token_id,
                )
            # Decodificamos solo los tokens nuevos (respuesta del modelo)
            new_ids  = output_ids[0][inputs["input_ids"].shape[1]:]
            response = tokenizer.decode(new_ids, skip_special_tokens=True).strip()
            history.append({"role": "assistant", "content": response})
            return response

        # --- Prompt inicial automático (desde análisis de red) -------------------
        if prompt:
            print("=" * 60)
            print("  INITIAL PROMPT (from network analysis)")
            print("=" * 60)
            print(prompt)
            print("\n[LLM] Generating response…\n")
            response = _generate(prompt)
            print("[LLM RESPONSE]")
            print("-" * 60)
            print(response)
            print("-" * 60 + "\n")

        # --- Chat interactivo ----------------------------------------------------
        print("  Interactive chat started. Type 'exit' to quit.\n")
        while True:
            try:
                user_input = input("You: ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\n[LLM] Session ended.")
                break

            if user_input.lower() in ('exit', 'quit', 'q', 'salir'):
                print("[LLM] Session ended.")
                break
            if not user_input:
                continue

            response = _generate(user_input)
            print(f"\nModel: {response}\n")

    # Usamos Gemma-2-2B-it porque es el modelo instrucción-tuneado de Google más accesible
    # sin necesidad de licencia especial.  El formato de chat <start_of_turn>user … <end_of_turn>
    # es el estándar de Gemma; otros modelos (LLaMA, Mistral) usan [INST]…[/INST].
    # Mantener history[] como lista de dicts (rol + contenido) permite conversación multi-turno
    # coherente: el modelo "recuerda" lo dicho antes porque todo el historial se re-tokeniza
    # en cada turno.  Esto consume más tokens con el tiempo pero es la aproximación estándar
    # hasta que se implementa memoria externa (RAG, etc.).

    def api_llm_fallback(self, prompt: str,
                         model: str = "gemini-1.5-flash",
                         api_key_env: str = "GEMINI_API_KEY") -> str:
        """
        Alternativa a chat_local_llm() cuando no hay GPU suficiente.
        Llama a la API de Gemini (Google AI Studio) con la clave almacenada en
        la variable de entorno GEMINI_API_KEY.

        Parameters
        ----------
        prompt      : str  – prompt a enviar.
        model       : str  – modelo Gemini a usar.
        api_key_env : str  – nombre de la variable de entorno con la API key.

        Returns
        -------
        str – texto de respuesta del modelo.
        """
        api_key = os.environ.get(api_key_env, "")
        if not api_key:
            raise EnvironmentError(
                f"Set '{api_key_env}' env var with your Google AI Studio key.\n"
                "Get a free key at: https://aistudio.google.com/app/apikey"
            )

        url     = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        headers = {"Content-Type": "application/json"}
        params  = {"key": api_key}

        resp = requests.post(url, json=payload, headers=headers, params=params, timeout=30)
        resp.raise_for_status()

        data = resp.json()
        try:
            text = data["candidates"][0]["content"]["parts"][0]["text"]
        except (KeyError, IndexError) as e:
            raise ValueError(f"Unexpected Gemini response format: {e}\n{data}")

        print("[Gemini API Response]")
        print("-" * 60)
        print(text)
        print("-" * 60)
        return text

    # Fallback para entornos sin GPU (Colab gratuito, portátiles sin VRAM suficiente).
    # Gemini Flash tiene contexto de 1M tokens y es gratuito hasta 15 peticiones/minuto,
    # más que suficiente para las pruebas de esta actividad.  Usamos requests directamente
    # (sin SDK) para mantener la dependencia mínima y la lógica autocontenida en la clase.

    def export_results(self, output_dir: str = "output") -> None:
        """Export all results: clean data, hashtag analytics, sentiment, summary."""
        if self.data is None:
            raise RuntimeError("No data loaded.")

        out = Path(output_dir)
        out.mkdir(parents=True, exist_ok=True)

        if 'clean_text' not in self.data.columns:
            self.data['clean_text'] = self.data['text'].apply(self.clean_text)

        self.data.to_csv(out / 'tweets_clean.csv', index=False, encoding='utf-8')
        print(f" tweets_clean.csv ({len(self.data):,} rows)")

        analytics = self.analytics_hashtags_extended()
        for key, fname in [('overall', 'hashtags_overall.csv'), ('by_user', 'hashtags_by_user.csv'), ('by_date', 'hashtags_by_date.csv')]:
            analytics[key].to_csv(out / fname, index=False, encoding='utf-8')
            print(f" {fname} ({len(analytics[key]):,} rows)")

        if 'sentiment_polarity' in self.data.columns:
            cols = [c for c in ['user_name', 'date', 'text', 'clean_text', 'sentiment_polarity', 'sentiment_subjectivity'] if c in self.data.columns]
            self.data[cols].to_csv(out / 'sentiment_results.csv', index=False, encoding='utf-8')
            print(f" sentiment_results.csv ({len(self.data):,} rows)")

        summary = self.parse_and_summarize(summary_ratio=0.01)
        (out / 'summary.txt').write_text(summary, encoding='utf-8')
        print(f" summary.txt ({len(summary.split())} words)\n✅ Results in '{out.resolve()}'")

    # export_results guarda: tweets limpios, análisis de hashtags (global / por usuario / por fecha),
    # resultados de sentimiento y el resumen extractivo. Centralizar la exportación en un solo método
    # facilita la reproducibilidad: con una llamada tienes todos los artefactos del análisis en disco.
