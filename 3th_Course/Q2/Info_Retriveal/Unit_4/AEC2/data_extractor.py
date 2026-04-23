#====================================================================================================#
#                                                                                                    #
#                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        #
#      AEC2 - BAIN                                       ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       #
#                                                        ██║   ██║█████╗██║   ███████║██║  ██║       #
#      created:        08/04/2026  -  01:00:51           ██║   ██║╚════╝██║   ██╔══██║██║  ██║       #
#      last change:    23/04/2026  -  12:14:43           ╚██████╔╝      ██║   ██║  ██║██████╔╝       #
#                                                         ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        #
#                                                                                                    #
#      Ismael Hernandez Clemente                         ismael.hernandez@live.u-tad.com             #
#                                                                                                    #
#      Github:                                           https://github.com/ismaelucky342            #
#                                                                                                    #
#====================================================================================================# 

import os
import requests
import pandas as pd
from pathlib import Path
import re
import unicodedata


class DataExtractor:
    """
    Clase central donde centralizo toda la lógica del proyecto: extracción de datos
    (local o vía API), limpieza de texto, análisis de hashtags, modelado de tópicos,
    análisis de sentimiento y resumen extractivo.

    Atributos
    ---------
    source : str
        Ruta al archivo local de datos (CSV o JSON). Tras extraer por API,
        apunto aquí al CSV guardado.
    data : pd.DataFrame or None
        DataFrame con los datos cargados.
    chunksize : int
        Tamaño de chunk para leer CSVs grandes sin reventar la memoria.
    """

    # Compilo los patrones una sola vez para no repetirlo en cada llamada.
    _RE_URL     = re.compile(r'https?://\S+|www\.\S+', re.IGNORECASE)
    _RE_MENTION = re.compile(r'@\w+')
    _RE_HASHTAG = re.compile(r'#(\w+)')
    _RE_SPECIAL = re.compile(r'[^\w\s#]', re.UNICODE)
    _RE_SPACES  = re.compile(r'\s+')

    def __init__(self, source: str = None, chunksize: int = 100_000):
        """
        Inicializo el extractor.

        Parámetros
        ----------
        source : str, opcional
            Ruta al archivo local (CSV o JSON). Puedo dejarlo None si voy
            a extraer datos directamente de la API.
        chunksize : int, opcional
            Tamaño del chunk para leer CSVs grandes (default 100 000).
        """
        self.source = source
        self.data = None
        self.chunksize = chunksize

    # -------------------------------------------------------------------------
    # Extracción de datos
    # -------------------------------------------------------------------------

    def load_data_api(self, query: str, max_results: int = 100, output_file: str = "tweets_from_api.csv") -> pd.DataFrame:
        """
        Me conecto a la API de Twitter a través de RapidAPI y extraigo tweets
        en tiempo real. Guardo el resultado en un CSV local para reutilizarlo
        luego con el resto de métodos.

        La clave la leo de la variable de entorno RAPIDAPI_KEY para no
        exponerla en el código (nunca la pongo hardcodeada aquí).

        Parámetros
        ----------
        query : str
            Palabra clave o hashtag a buscar (ej. "#bitcoin").
        max_results : int
            Número máximo de tweets a extraer (default 100).
        output_file : str
            Ruta del CSV donde guardo los datos extraídos.

        Devuelve
        --------
        pd.DataFrame con los tweets extraídos.
        """
        url = "https://twitter-api45.p.rapidapi.com/search.php"
        headers = {
            "X-RapidAPI-Key": os.environ.get("RAPIDAPI_KEY", ""),
            "X-RapidAPI-Host": "twitter-api45.p.rapidapi.com"
        }
        params = {
            "query": query,
            "count": max_results
        }

        # Hago la petición y compruebo que ha ido bien antes de seguir.
        response = requests.get(url, headers=headers, params=params, timeout=15)
        if response.status_code != 200:
            raise RuntimeError(f"API request failed: {response.status_code} {response.text}")

        data_json = response.json()

        # La API puede devolver los tweets bajo 'tweets' o 'data' según la versión.
        tweets = data_json.get("tweets") or data_json.get("data")
        if not tweets:
            raise ValueError("No tweets found in API response.")

        # Adapto las columnas al formato mínimo que usa el resto de métodos.
        rows = []
        for t in tweets:
            rows.append({
                "user_name": t.get("user_name") or t.get("author_id"),
                "date": t.get("date") or t.get("created_at"),
                "text": t.get("text")
            })

        df = pd.DataFrame(rows)
        df.to_csv(output_file, index=False, encoding="utf-8")

        # Actualizo self.data y self.source para que el resto de métodos funcionen.
        self.data = df
        self.source = output_file

        print(f"[load_data_api] Extracted {len(df)} tweets -> saved to '{output_file}'")
        return self.data

    def load_data(self) -> pd.DataFrame:
        """
        Cargo los datos desde el archivo local en self.source.
        Detecto automáticamente si es CSV o JSON, y para CSVs grandes
        uso chunksize para no cargar todo de golpe.

        Devuelve
        --------
        pd.DataFrame con los datos cargados.
        """
        path = Path(self.source)
        ext  = path.suffix.lower()

        if ext == '.json':
            self.data = pd.read_json(self.source, encoding='utf-8')
        elif ext == '.csv':
            # Leo en chunks y concateno para no reventar la RAM con archivos grandes.
            chunks = pd.read_csv(
                self.source,
                encoding='utf-8',
                low_memory=False,
                chunksize=self.chunksize,
                lineterminator='\n',
            )
            self.data = pd.concat(chunks, ignore_index=True)
        else:
            raise ValueError(f"Unsupported format: '{ext}'. Use CSV or JSON.")

        # Limpio el '\r' de los nombres de columna por si el CSV viene con CRLF.
        self.data.columns = [c.strip().replace('\r', '') for c in self.data.columns]

        print(f"[load_data] Loaded {len(self.data):,} rows – columns: {list(self.data.columns)}")
        return self.data

    # -------------------------------------------------------------------------
    # Limpieza y extracción de features
    # -------------------------------------------------------------------------

    def clean_text(self, text: str) -> str:
        """
        Limpio y normalizo un tweet en varios pasos:
        1. Convierto a string y elimino espacios al inicio/fin.
        2. Paso a minúsculas.
        3. Elimino URLs.
        4. Quito menciones (@usuario).
        5. Elimino emojis y símbolos con categorías Unicode So/Sk/Cs.
        6. Elimino caracteres especiales salvo letras, dígitos, espacios y '#'.
        7. Colapso espacios redundantes.

        Conservo los hashtags porque son la base del análisis.
        """
        if not isinstance(text, str):
            text = str(text) if pd.notna(text) else ''

        text = text.strip().lower()
        text = self._RE_URL.sub(' ', text)
        text = self._RE_MENTION.sub(' ', text)

        # Quito emojis y símbolos raros mirando la categoría Unicode de cada carácter.
        text = ''.join(ch for ch in text if unicodedata.category(ch) not in ('So', 'Sk', 'Cs'))

        text = self._RE_SPECIAL.sub(' ', text)
        return self._RE_SPACES.sub(' ', text).strip()

    def extract_hashtags(self, text: str) -> list:
        """
        Extraigo los hashtags presentes en el texto usando el patrón #(\\w+).
        Devuelvo una lista en minúsculas y sin duplicados, manteniendo el orden
        de aparición.
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

    # -------------------------------------------------------------------------
    # Análisis de hashtags
    # -------------------------------------------------------------------------

    def analytics_hashtags_extended(self) -> dict:
        """
        Hago un análisis avanzado de hashtags sobre self.data. Calculo tres
        vistas:
        - overall: frecuencia global de cada hashtag.
        - by_user: frecuencia por (usuario, hashtag).
        - by_date: evolución temporal (fecha, hashtag).

        Devuelve
        --------
        dict con claves 'overall', 'by_user', 'by_date' (cada una es un DataFrame).
        """
        if self.data is None:
            raise RuntimeError("No hay datos cargados. Llama a load_data() o load_data_api() primero.")

        df = self.data.copy()

        # Limpio, extraigo hashtags y normalizo fechas antes de explotar y agrupar.
        df['clean_text'] = df['text'].apply(self.clean_text)
        df['hashtags']   = df['clean_text'].apply(self.extract_hashtags)
        df['date']       = pd.to_datetime(df['date'], utc=True, errors='coerce').dt.date

        df_exp = df.explode('hashtags').dropna(subset=['hashtags'])
        df_exp = df_exp[df_exp['hashtags'].str.strip() != ''].rename(columns={'hashtags': 'hashtag'})

        overall = (df_exp.groupby('hashtag', as_index=False).size()
                         .rename(columns={'size': 'frequency'})
                         .sort_values('frequency', ascending=False).reset_index(drop=True))

        by_user = (df_exp.groupby(['user_name', 'hashtag'], as_index=False).size()
                         .rename(columns={'size': 'frequency'})
                         .sort_values('frequency', ascending=False).reset_index(drop=True))

        by_date = (df_exp.groupby(['date', 'hashtag'], as_index=False).size()
                         .rename(columns={'size': 'frequency'})
                         .sort_values(['date', 'frequency'], ascending=[True, False]).reset_index(drop=True))

        print(f"[analytics] {len(overall)} hashtags únicos encontrados.")
        return {'overall': overall, 'by_user': by_user, 'by_date': by_date}

    # -------------------------------------------------------------------------
    # Visualización
    # -------------------------------------------------------------------------

    def generate_hashtag_wordcloud(self, overall_df: pd.DataFrame = None, max_words: int = 100, figsize: tuple = (10, 6)) -> None:
        """
        Genero y muestro una wordcloud con los hashtags más frecuentes.
        Si no le paso overall_df, lo calculo yo solo llamando a analytics_hashtags_extended.

        Parámetros
        ----------
        overall_df : DataFrame, opcional
            Tabla con columnas ['hashtag', 'frequency']. Si es None, se calcula.
        max_words : int
            Número máximo de palabras en la nube.
        figsize : tuple
            Tamaño de la figura matplotlib.
        """
        import matplotlib.pyplot as plt
        from wordcloud import WordCloud

        if overall_df is None:
            analytics = self.analytics_hashtags_extended()
            overall_df = analytics['overall']

        # Paso el DataFrame a dict {hashtag: frecuencia} para alimentar la WordCloud.
        freq_dict = dict(zip(overall_df['hashtag'], overall_df['frequency']))

        wc = WordCloud(
            width=figsize[0] * 100, height=figsize[1] * 100,
            max_words=max_words,
            background_color='white',
            colormap='viridis'
        ).generate_from_frequencies(freq_dict)

        plt.figure(figsize=figsize)
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.tight_layout()
        plt.show()

    # -------------------------------------------------------------------------
    # Análisis avanzado (AEC2)
    # -------------------------------------------------------------------------

    def model_topics(self, num_topics: int = 5, passes: int = 10) -> list:
        """
        Aplico LDA con gensim para descubrir los temas principales del corpus.

        Pasos:
        1. Me aseguro de que 'clean_text' existe (la genero si hace falta).
        2. Tokenizo cada texto dividiendo por espacios.
        3. Creo el diccionario y el corpus bag-of-words.
        4. Entreno el modelo LDA.
        5. Devuelvo los tópicos como listas de palabras.

        Parámetros
        ----------
        num_topics : int
            Número de tópicos a descubrir (default 5).
        passes : int
            Iteraciones de entrenamiento (default 10).

        Devuelve
        --------
        list de listas: cada tópico es una lista de las 10 palabras más relevantes.
        """
        import gensim
        from gensim import corpora

        # Si no tengo clean_text, la genero aquí.
        if 'clean_text' not in self.data.columns:
            self.data['clean_text'] = self.data['text'].apply(self.clean_text)

        texts = self.data['clean_text'].dropna().apply(lambda x: x.split()).tolist()
        dictionary = corpora.Dictionary(texts)
        corpus = [dictionary.doc2bow(text) for text in texts]

        lda_model = gensim.models.LdaModel(
            corpus, num_topics=num_topics,
            id2word=dictionary, passes=passes, random_state=42
        )

        # Extraigo las palabras de cada tópico y las devuelvo como listas limpias.
        topics = []
        for t in lda_model.show_topics(num_topics=num_topics, num_words=10, formatted=False):
            topic_words = [w for w, _ in t[1]]
            topics.append(topic_words)

        return topics

    def analyze_sentiment(self, method: str = 'textblob') -> pd.DataFrame:
        """
        Analizo el sentimiento de cada tweet: calculo polaridad y subjetividad
        y las añado como columnas al DataFrame.

        Parámetros
        ----------
        method : str
            'textblob' (rápido) o 'spacy' (más preciso con spacytextblob).

        Devuelve
        --------
        pd.DataFrame actualizado con las columnas 'sentiment_polarity' y
        'sentiment_subjectivity'.
        """
        # Me aseguro de tener la columna limpia antes de analizar.
        if 'clean_text' not in self.data.columns:
            self.data['clean_text'] = self.data['text'].apply(self.clean_text)

        if method == 'textblob':
            from textblob import TextBlob
            self.data['sentiment_polarity'] = self.data['clean_text'].apply(
                lambda x: TextBlob(x).sentiment.polarity
            )
            self.data['sentiment_subjectivity'] = self.data['clean_text'].apply(
                lambda x: TextBlob(x).sentiment.subjectivity
            )

        elif method == 'spacy':
            import spacy
            from spacytextblob.spacytextblob import SpacyTextBlob
            nlp = spacy.load('en_core_web_sm')
            nlp.add_pipe('spacytextblob')
            self.data['sentiment_polarity'] = self.data['clean_text'].apply(
                lambda x: nlp(x)._.polarity
            )
            self.data['sentiment_subjectivity'] = self.data['clean_text'].apply(
                lambda x: nlp(x)._.subjectivity
            )

        else:
            raise ValueError(f"Método no soportado: '{method}'. Usa 'textblob' o 'spacy'.")

        return self.data

    def export_results(self, output_dir: str = "output") -> None:
        """
        Exporto todos los resultados del análisis a archivos en una carpeta
        de salida. Así dejo todo listo para revisión sin depender de que el
        notebook se haya ejecutado entero.

        Genera:
        - tweets_clean.csv       → dataset completo con texto limpio
        - hashtags_overall.csv   → frecuencia global de hashtags
        - hashtags_by_user.csv   → frecuencia por usuario
        - hashtags_by_date.csv   → frecuencia por fecha
        - sentiment_results.csv  → tweets con polaridad y subjetividad
        - summary.txt            → resumen extractivo del corpus

        Parámetros
        ----------
        output_dir : str
            Carpeta donde guardo los archivos (se crea si no existe).
        """
        from pathlib import Path

        out = Path(output_dir)
        out.mkdir(parents=True, exist_ok=True)

        if self.data is None:
            raise RuntimeError("No hay datos cargados. Llama a load_data() o load_data_api() primero.")

        # 1. Dataset limpio.
        if 'clean_text' not in self.data.columns:
            self.data['clean_text'] = self.data['text'].apply(self.clean_text)
        clean_path = out / 'tweets_clean.csv'
        self.data.to_csv(clean_path, index=False, encoding='utf-8')
        print(f"[export] {clean_path} ({len(self.data):,} filas)")

        # 2. Tablas de hashtags.
        analytics = self.analytics_hashtags_extended()
        for key, fname in [('overall', 'hashtags_overall.csv'),
                           ('by_user',  'hashtags_by_user.csv'),
                           ('by_date',  'hashtags_by_date.csv')]:
            p = out / fname
            analytics[key].to_csv(p, index=False, encoding='utf-8')
            print(f"[export] {p} ({len(analytics[key]):,} filas)")

        # 3. Resultados de sentimiento (solo si ya se calcularon).
        if 'sentiment_polarity' in self.data.columns:
            sent_path = out / 'sentiment_results.csv'
            cols = ['user_name', 'date', 'text', 'clean_text',
                    'sentiment_polarity', 'sentiment_subjectivity']
            cols_ok = [c for c in cols if c in self.data.columns]
            self.data[cols_ok].to_csv(sent_path, index=False, encoding='utf-8')
            print(f"[export] {sent_path} ({len(self.data):,} filas)")
        else:
            print("[export] Sentimiento no calculado, saltando sentiment_results.csv")

        # 4. Resumen extractivo.
        summary_path = out / 'summary.txt'
        summary = self.parse_and_summarize(summary_ratio=0.01)
        summary_path.write_text(summary, encoding='utf-8')
        print(f"[export] {summary_path} ({len(summary.split())} palabras)")

        print(f"\n✅ Resultados exportados en '{out.resolve()}'")

    def export_topics(self, topics: list, output_dir: str = "output") -> None:
        """
        Guardo los tópicos LDA en un archivo de texto legible.
        Lo separo de export_results porque los tópicos se calculan aparte
        y no siempre se tienen disponibles en el mismo flujo.

        Parámetros
        ----------
        topics : list
            Lista devuelta por model_topics().
        output_dir : str
            Carpeta de salida (se crea si no existe).
        """
        from pathlib import Path

        out = Path(output_dir)
        out.mkdir(parents=True, exist_ok=True)

        topics_path = out / 'topics_lda.txt'
        lines = ["Tópicos descubiertos por LDA\n", "=" * 40 + "\n"]
        for i, topic in enumerate(topics, 1):
            lines.append(f"Tópico {i}: {', '.join(topic)}\n")
        topics_path.write_text(''.join(lines), encoding='utf-8')
        print(f"[export] {topics_path}")

    def parse_and_summarize(self, summary_ratio: float = 0.3) -> str:
        """
        Genero un resumen extractivo del corpus completo usando NLTK.

        El proceso es:
        1. Concateno todos los textos limpios en un solo string.
        2. Divido en oraciones con sent_tokenize.
        3. Calculo la frecuencia de palabras (sin stopwords).
        4. Puntúo cada oración por la suma de frecuencias de sus palabras.
        5. Selecciono las mejores oraciones según summary_ratio.
        6. Las reordeno según su posición original para que el resumen tenga sentido.

        Parámetros
        ----------
        summary_ratio : float
            Proporción de oraciones a retener (ej. 0.3 = 30%).

        Devuelve
        --------
        str con el resumen generado.
        """
        import nltk
        from nltk.tokenize import sent_tokenize, word_tokenize
        from nltk.corpus import stopwords
        import string

        nltk.download('punkt', quiet=True)
        nltk.download('punkt_tab', quiet=True)
        nltk.download('stopwords', quiet=True)

        # Genero clean_text si no existe.
        if 'clean_text' not in self.data.columns:
            self.data['clean_text'] = self.data['text'].apply(self.clean_text)

        # Junto todo el corpus en un único texto para analizar el vocabulario global.
        text = ' '.join(self.data['clean_text'].dropna().tolist())
        sentences = sent_tokenize(text)

        stop_words = set(stopwords.words('english'))

        # Cuento la frecuencia de cada palabra no vacía.
        word_freq = {}
        for sent in sentences:
            words = word_tokenize(sent.lower())
            for word in words:
                if word in stop_words or word in string.punctuation:
                    continue
                word_freq[word] = word_freq.get(word, 0) + 1

        # Puntúo cada oración sumando las frecuencias de sus palabras.
        sent_scores = {}
        for sent in sentences:
            words = word_tokenize(sent.lower())
            sent_scores[sent] = sum(word_freq.get(w, 0) for w in words)

        # Selecciono las N mejores y las reordeno por posición original.
        n_select = max(1, int(len(sentences) * summary_ratio))
        ranked   = sorted(sent_scores, key=sent_scores.get, reverse=True)
        selected = sorted(ranked[:n_select], key=sentences.index)

        return ' '.join(selected)
