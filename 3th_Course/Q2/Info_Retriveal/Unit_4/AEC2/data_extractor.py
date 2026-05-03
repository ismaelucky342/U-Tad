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

    # Exporto todos los resultados del análisis en archivos separados en una carpeta output_dir.
        out = Path(output_dir)
        out.mkdir(parents=True, exist_ok=True)
        
        lines = ["LDA Topics\n" + "=" * 40 + "\n"]
        for i, topic in enumerate(topics, 1):
            lines.append(f"Topic {i}: {', '.join(topic)}\n")
        
        (out / 'topics_lda.txt').write_text(''.join(lines), encoding='utf-8')
        print(f" topics_lda.txt")

    # Exporto los tópicos LDA a un archivo de texto legible. Cada tópico aparece en una línea
    # con sus palabras más relevantes separadas por comas. Se lo separo de export_results/()
    # porque los tópicos se generan por separado con model_topics() y no todos los pipelines
    # necesariamente los calculan.
