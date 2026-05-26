#====================================================================================================#
#                                                                                                    #
#                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        #
#      AEC3 - BAIN - Análisis de Redes + LLM                                                        #
#                                                        ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       #
#      Extención de AEC2 con NetworkX e Integración LLM                                             #
#                                                        ██║   ██║█████╗██║   ███████║██║  ██║       #
#      created:        26/05/2026  -  Basado en AEC2     ██║   ██║╚════╝██║   ██╔══██║██║  ██║       #
#                                                         ╚██████╔╝      ██║   ██║  ██║██████╔╝       #
#                                                         ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        #
#                                                                                                    #
#====================================================================================================# 

import os
import re
import unicodedata
import pandas as pd
import requests
from pathlib import Path
import json
import numpy as np

# Importar módulos especializados
from network_analysis import NetworkAnalyzer
from llm_integration import LLMIntegration
from utils import ExportUtils, ValidationUtils


class DataExtractor:
    """Extracción, limpieza, análisis de tweets + análisis de redes + integración LLM."""

    _RE_URL = re.compile(r'https?://\S+|www\.\S+', re.IGNORECASE)
    _RE_MENTION = re.compile(r'@\w+')
    _RE_HASHTAG = re.compile(r'#(\w+)')
    _RE_SPECIAL = re.compile(r'[^\w\s#]', re.UNICODE)
    _RE_SPACES = re.compile(r'\s+')

    def __init__(self, source: str = None, chunksize: int = 100_000):
        self.source = source
        self.data = None
        self.chunksize = chunksize
        self.interaction_graph = None

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
        print(f"✓ {len(self.data)} tweets extracted and saved to '{output_file}'")
        return self.data

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
        print(f"✓ Loaded {len(self.data):,} rows – {list(self.data.columns)}")
        return self.data

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

        print(f"✓ {len(overall)} unique hashtags found")
        return {'overall': overall, 'by_user': by_user, 'by_date': by_date}

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
        plt.title('Hashtag Word Cloud')
        plt.tight_layout()
        plt.show()

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
        print(f"✓ LDA: {num_topics} topics ({len(texts)} docs)")
        return topics

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

    def export_results(self, output_dir: str = "output") -> None:
        """Export all results: clean data, hashtag analytics, sentiment, summary."""
        if self.data is None:
            raise RuntimeError("No data loaded.")

        out = Path(output_dir)
        out.mkdir(parents=True, exist_ok=True)

        if 'clean_text' not in self.data.columns:
            self.data['clean_text'] = self.data['text'].apply(self.clean_text)

        self.data.to_csv(out / 'tweets_clean.csv', index=False, encoding='utf-8')
        print(f"✓ tweets_clean.csv ({len(self.data):,} rows)")

        analytics = self.analytics_hashtags_extended()
        for key, fname in [('overall', 'hashtags_overall.csv'), ('by_user', 'hashtags_by_user.csv'), ('by_date', 'hashtags_by_date.csv')]:
            analytics[key].to_csv(out / fname, index=False, encoding='utf-8')
            print(f"✓ {fname} ({len(analytics[key]):,} rows)")

        if 'sentiment_polarity' in self.data.columns:
            cols = [c for c in ['user_name', 'date', 'text', 'clean_text', 'sentiment_polarity', 'sentiment_subjectivity'] if c in self.data.columns]
            self.data[cols].to_csv(out / 'sentiment_results.csv', index=False, encoding='utf-8')
            print(f"✓ sentiment_results.csv ({len(self.data):,} rows)")

        summary = self.parse_and_summarize(summary_ratio=0.01)
        (out / 'summary.txt').write_text(summary, encoding='utf-8')
        print(f"✓ summary.txt ({len(summary.split())} words)\n✅ Results in '{out.resolve()}'")

    # ================================================================================================
    # NUEVOS MÉTODOS - UNIDAD 6: ANÁLISIS DE REDES + LLM
    # ================================================================================================

    def build_interaction_graph(self, mention_extraction: bool = True):
        """
        Construye un grafo de interacciones a partir de los datos.
        
        Delega al módulo NetworkAnalyzer para mantener código modular.
        """
        G = NetworkAnalyzer.build_interaction_graph(
            self.data,
            self.extract_hashtags,
            lambda text: self._RE_MENTION.findall(text),
            mention_extraction=mention_extraction
        )
        self.interaction_graph = G
        print(f"Grafo construido: {G.number_of_nodes()} nodos, {G.number_of_edges()} aristas")
        return G

    def analyze_network(self, G=None, top_k: int = 3) -> dict:
        """
        Calcula métricas de red y detecta comunidades.
        
        Delega al módulo NetworkAnalyzer.
        """
        if G is None:
            G = self.interaction_graph
        
        if G is None or G.number_of_nodes() == 0:
            raise RuntimeError("No hay grafo disponible. Llama a build_interaction_graph() primero.")
        
        analysis = NetworkAnalyzer.analyze_network(G, top_k=top_k)
        
        print(f"Análisis completado:")
        print(f"  - {analysis['global_stats']['num_nodes']} nodos")
        print(f"  - {analysis['global_stats']['num_edges']} aristas")
        print(f"  - Densidad: {analysis['global_stats']['density']:.4f}")
        print(f"  - Comunidades: {analysis['communities'].get('num_communities', 0)}")
        
        return analysis

    def generate_prompt_from_network(self, G=None, analysis: dict = None) -> str:
        """
        Genera un prompt para el LLM a partir del análisis de la red.
        
        Delega al módulo LLMIntegration.
        """
        if G is None:
            G = self.interaction_graph
        
        if G is None or G.number_of_nodes() == 0:
            raise RuntimeError("No hay grafo disponible.")
        
        if analysis is None:
            analysis = self.analyze_network(G, top_k=3)
        
        hashtags_stats = self.analytics_hashtags_extended()
        
        prompt = LLMIntegration.generate_prompt_from_network(G, analysis, hashtags_stats)
        return prompt

    def chat_local_llm(self, prompt: str = None, model_name: str = "google/gemma-2b-it",
                      max_tokens: int = 512, use_gpu: bool = True, temperature: float = 0.7) -> str:
        """
        Levanta un modelo LLM preentrenado y genera una respuesta.
        
        Delega al módulo LLMIntegration con fallback automático.
        """
        if prompt is None:
            prompt = self.generate_prompt_from_network()
            print("Prompt auto-generado a partir del análisis de red")
        
        # Intenta modelo local
        try:
            print(f"Cargando modelo local: {model_name}")
            tokenizer, model, device = LLMIntegration.load_local_llm(model_name, use_gpu)
            print(f"Modelo cargado en device: {device}")
            
            response = LLMIntegration.generate_llm_response(
                tokenizer, model, prompt, device, max_tokens, temperature
            )
            print(f"Respuesta generada ({len(response.split())} palabras)")
            return response
        
        except Exception as e:
            print(f"Error con modelo local: {e}")
            print("Usando fallback: Google Generative AI API")
            return LLMIntegration.chat_google_ai(prompt, max_tokens)

    def export_network_analysis(self, output_dir: str = "output", G=None,
                              analysis: dict = None) -> None:
        """
        Exporta el análisis de la red a archivos.
        
        Delega al módulo ExportUtils.
        """
        if G is None:
            G = self.interaction_graph
        
        if G is None:
            raise RuntimeError("No hay grafo disponible.")
        
        if analysis is None:
            analysis = self.analyze_network(G)
        
        prompt = self.generate_prompt_from_network(G, analysis)
        
        ExportUtils.export_network_analysis(
            output_dir, G, analysis, prompt, 
            llm_response="(generada por chat_local_llm)"
        )
        print(f"Resultados exportados a: {Path(output_dir).resolve()}")
