import os
import requests
import pandas as pd
from pathlib import Path
import re
import unicodedata

class DataExtractor:
        def generate_hashtag_wordcloud(self, overall_df: pd.DataFrame = None, max_words: int = 100, figsize: tuple = (10, 6)) -> None:
            """
            Genera y muestra una WordCloud basada en el análisis global de hashtags.
            """
            import matplotlib.pyplot as plt
            from wordcloud import WordCloud
            if overall_df is None:
                analytics = self.analytics_hashtags_extended()
                overall_df = analytics['overall']
            freq_dict = dict(zip(overall_df['hashtag'], overall_df['frequency']))
            wc = WordCloud(width=figsize[0]*100, height=figsize[1]*100, max_words=max_words,
                          background_color='white', colormap='viridis').generate_from_frequencies(freq_dict)
            plt.figure(figsize=figsize)
            plt.imshow(wc, interpolation='bilinear')
            plt.axis('off')
            plt.tight_layout()
            plt.show()

        def model_topics(self, num_topics: int = 5, passes: int = 10) -> list:
            """
            Aplica el modelo LDA para descubrir tópicos en el corpus.
            """
            import gensim
            from gensim import corpora
            # Asegurarse de que la columna 'clean_text' existe
            if 'clean_text' not in self.data.columns:
                self.data['clean_text'] = self.data['text'].apply(self.clean_text)
            # Tokenización simple
            texts = self.data['clean_text'].dropna().apply(lambda x: x.split()).tolist()
            dictionary = corpora.Dictionary(texts)
            corpus = [dictionary.doc2bow(text) for text in texts]
            lda_model = gensim.models.LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=passes, random_state=42)
            topics = []
            for t in lda_model.show_topics(num_topics=num_topics, num_words=10, formatted=False):
                topic_words = [w for w, _ in t[1]]
                topics.append(topic_words)
            return topics

        def analyze_sentiment(self, method: str = 'textblob') -> pd.DataFrame:
            """
            Analiza el sentimiento de cada tweet utilizando el método especificado.
            """
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
                raise ValueError("Método de sentimiento no soportado: usa 'textblob' o 'spacy'")
            return self.data

        def parse_and_summarize(self, summary_ratio: float = 0.3) -> str:
            """
            Realiza un análisis de parsing y genera un resumen extractivo del corpus.
            """
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
            stop_words = set(stopwords.words('english'))
            word_freq = {}
            for sent in sentences:
                words = word_tokenize(sent.lower())
                for word in words:
                    if word in stop_words or word in string.punctuation:
                        continue
                    word_freq[word] = word_freq.get(word, 0) + 1
            sent_scores = {}
            for sent in sentences:
                words = word_tokenize(sent.lower())
                score = sum(word_freq.get(word, 0) for word in words)
                sent_scores[sent] = score
            n_select = max(1, int(len(sentences) * summary_ratio))
            ranked = sorted(sent_scores, key=sent_scores.get, reverse=True)
            selected = sorted(ranked[:n_select], key=sentences.index)
            summary = ' '.join(selected)
            return summary
    """Extractor de datos para análisis de tweets, ampliado con conexión a API."""

    _RE_URL     = re.compile(r'https?://\S+|www\.\S+', re.IGNORECASE)
    _RE_MENTION = re.compile(r'@\w+')
    _RE_HASHTAG = re.compile(r'#(\w+)')
    _RE_SPECIAL = re.compile(r'[^\w\s#]', re.UNICODE)
    _RE_SPACES  = re.compile(r'\s+')

    def __init__(self, source: str = None, chunksize: int = 100_000):
        self.source = source
        self.data = None
        self.chunksize = chunksize

    def load_data_api(self, query: str, max_results: int = 100, output_file: str = "tweets_from_api.csv"):
        """
        Conecta con la API de Twitter a través de RapidAPI para extraer tweets en tiempo real,
        y almacena los resultados en un archivo local.
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
        response = requests.get(url, headers=headers, params=params, timeout=15)
        if response.status_code != 200:
            raise RuntimeError(f"API request failed: {response.status_code} {response.text}")
        data_json = response.json()
        tweets = data_json.get("tweets") or data_json.get("data")
        if not tweets:
            raise ValueError("No tweets found in API response.")
        # Adaptar columnas mínimas
        rows = []
        for t in tweets:
            rows.append({
                "user_name": t.get("user_name") or t.get("author_id"),
                "date": t.get("date") or t.get("created_at"),
                "text": t.get("text")
            })
        df = pd.DataFrame(rows)
        df.to_csv(output_file, index=False, encoding="utf-8")
        self.data = df
        self.source = output_file
        return self.data

    def load_data(self) -> pd.DataFrame:
        path = Path(self.source)
        ext  = path.suffix.lower()
        if ext == '.json':
            self.data = pd.read_json(self.source, encoding='utf-8')
        elif ext == '.csv':
            chunks = pd.read_csv(
                self.source,
                encoding='utf-8',
                low_memory=False,
                chunksize=self.chunksize,
                lineterminator='\n',
            )
            self.data = pd.concat(chunks, ignore_index=True)
        else:
            raise ValueError(f"Unsupported format: '{ext}'")
        self.data.columns = [c.strip().replace('\r', '') for c in self.data.columns]
        return self.data

    def clean_text(self, text: str) -> str:
        if not isinstance(text, str):
            text = str(text) if pd.notna(text) else ''
        text = text.strip().lower()
        text = self._RE_URL.sub(' ', text)
        text = self._RE_MENTION.sub(' ', text)
        text = ''.join(ch for ch in text if unicodedata.category(ch) not in ('So', 'Sk', 'Cs'))
        text = self._RE_SPECIAL.sub(' ', text)
        return self._RE_SPACES.sub(' ', text).strip()

    def extract_hashtags(self, text: str) -> list:
        if not isinstance(text, str):
            return []
        seen, result = set(), []
        for tag in self._RE_HASHTAG.findall(text):
            t = tag.lower()
            if t not in seen:
                seen.add(t)
                result.append(t)
        return result

    def analytics_hashtags_extended(self) -> dict:
        df = self.data.copy()
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
        return {'overall': overall, 'by_user': by_user, 'by_date': by_date}
