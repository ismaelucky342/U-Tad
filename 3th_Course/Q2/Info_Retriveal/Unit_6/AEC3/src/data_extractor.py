#====================================================================================================#
#                                                                                                    #
#                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        #
#      AEC3 - BAIN                                       ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       #
#                                                        ██║   ██║█████╗██║   ███████║██║  ██║       #
#      created:        22/05/2026  -  01:00:51           ██║   ██║╚════╝██║   ██╔══██║██║  ██║       #
#      last change:    31/05/2026  -  22:14:43           ╚██████╔╝      ██║   ██║  ██║██████╔╝       #
#                                                         ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        #
#                                                                                                    #
#      Ismael Hernandez Clemente                         ismael.hernandez@live.u-tad.com             #
#                                                                                                    #
#      Github:                                           https://github.com/ismaelucky342            #
#                                                                                                    #
#====================================================================================================# 

import os
import pandas as pd
import requests
from pathlib import Path

# Importaciones modulares locales
from src.nlp_core import (clean_text, extract_hashtags, extract_mentions,
                          analytics_hashtags_extended, generate_hashtag_wordcloud,
                          model_topics, analyze_sentiment, parse_and_summarize)
from src.network_core import build_interaction_graph, analyze_network
from src.llm_core import generate_prompt_from_network, chat_local_llm

class DataExtractor:
    def __init__(self, source: str = None, chunksize: int = 100_000):
        self.source = source
        self.data = None
        self.chunksize = chunksize

    def _parse_api_response(self, response_json: dict) -> list:
        tweets_list = None
        for key in ['tweets', 'data', 'timeline', 'results', 'statuses']:
            if key in response_json and isinstance(response_json[key], list):
                tweets_list = response_json[key]
                break

        if tweets_list is None:
            raise ValueError(f"No se encontro lista de tweets. Claves disponibles: {list(response_json.keys())}")

        rows = []
        for t in tweets_list:
            if not isinstance(t, dict):
                continue
            text = t.get('text') or t.get('full_text') or t.get('body') or ''
            user = (t.get('user_name') or t.get('author_id') or t.get('user', {}).get('name') or 'unknown')
            date = t.get('date') or t.get('created_at') or t.get('timestamp') or ''
            if text.strip():
                rows.append({'user_name': str(user).strip(), 'date': str(date).strip(), 'text': str(text).strip()})
        if not rows:
            raise ValueError("La respuesta de la API no contiene tweets validos.")
        return rows

    def load_data_api(self, query: str, max_results: int = 100, output_file: str = "tweets.csv") -> pd.DataFrame:
        try:
            resp = requests.get(
                "https://twitter-api45.p.rapidapi.com/search.php",
                headers={"X-RapidAPI-Key": os.environ.get("RAPIDAPI_KEY", ""),
                         "X-RapidAPI-Host": "twitter-api45.p.rapidapi.com"},
                params={"query": query, "count": max_results},
                timeout=15
            )
            resp.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Fallo en la peticion a la API: {e}")

        rows = self._parse_api_response(resp.json())
        self.data = pd.DataFrame(rows)
        self.data.to_csv(output_file, index=False, encoding="utf-8")
        self.source = output_file
        print(f"[OK] {len(self.data)} tweets extraidos y guardados en '{output_file}'")
        return self.data

    def load_data(self) -> pd.DataFrame:
        ext = Path(self.source).suffix.lower()
        if ext == '.json':
            self.data = pd.read_json(self.source, encoding='utf-8')
        elif ext == '.csv':
            chunks = pd.read_csv(self.source, encoding='utf-8', chunksize=self.chunksize, low_memory=False)
            self.data = pd.concat(chunks, ignore_index=True)
        else:
            raise ValueError(f"Formato no soportado: '{ext}'. Usa CSV o JSON.")

        self.data.columns = [c.strip().replace('\r', '') for c in self.data.columns]
        print(f"[OK] {len(self.data):,} filas cargadas – columnas: {list(self.data.columns)}")
        return self.data

    # --- Delegacion a modulos (Wrapper methods) ---
    
    def clean_text(self, text: str) -> str:
        return clean_text(text)

    def extract_hashtags(self, text: str) -> list:
        return extract_hashtags(text)

    def _extract_mentions(self, text: str) -> list:
        return extract_mentions(text)

    def analytics_hashtags_extended(self) -> dict:
        return analytics_hashtags_extended(self.data)

    def generate_hashtag_wordcloud(self, overall_df: pd.DataFrame = None, max_words: int = 100, figsize: tuple = (10, 6)):
        if overall_df is None:
            overall_df = self.analytics_hashtags_extended()['overall']
        generate_hashtag_wordcloud(overall_df, max_words, figsize)

    def model_topics(self, num_topics: int = 5, passes: int = 10, min_word_len: int = 3) -> list:
        return model_topics(self.data, num_topics, passes, min_word_len)

    def analyze_sentiment(self, method: str = 'textblob') -> pd.DataFrame:
        self.data = analyze_sentiment(self.data, method)
        return self.data

    def parse_and_summarize(self, summary_ratio: float = 0.05, max_length: int = 500) -> str:
        return parse_and_summarize(self.data, summary_ratio, max_length)

    def build_interaction_graph(self):
        return build_interaction_graph(self.data)

    def analyze_network(self, G):
        return analyze_network(G)

    def generate_prompt_from_network(self, G, metrics=None) -> str:
        top_hashtag = "N/D"
        if self.data is not None:
            try:
                analytics = self.analytics_hashtags_extended()
                if not analytics['overall'].empty:
                    top_hashtag = analytics['overall'].iloc[0]['hashtag']
            except Exception:
                pass
        return generate_prompt_from_network(G, metrics, top_hashtag)

    def chat_local_llm(self, prompt: str = None, model: str = "gemma3", ollama_url: str = "http://localhost:11434", stream: bool = True) -> str:
        return chat_local_llm(prompt, model, ollama_url, stream)

    def export_results(self, output_dir: str = "output", topics: list = None) -> None:
        if self.data is None:
            raise RuntimeError("Sin datos cargados.")

        out = Path(output_dir)
        out.mkdir(parents=True, exist_ok=True)

        if 'clean_text' not in self.data.columns:
            self.data['clean_text'] = self.data['text'].apply(self.clean_text)

        self.data.to_csv(out / 'tweets_clean.csv', index=False, encoding='utf-8')
        
        analytics = self.analytics_hashtags_extended()
        for key, fname in [('overall', 'hashtags_overall.csv'), ('by_user', 'hashtags_by_user.csv'), ('by_date', 'hashtags_by_date.csv')]:
            analytics[key].to_csv(out / fname, index=False, encoding='utf-8')

        if 'sentiment_polarity' in self.data.columns:
            cols = [c for c in ['user_name', 'date', 'text', 'clean_text', 'sentiment_polarity', 'sentiment_subjectivity'] if c in self.data.columns]
            self.data[cols].to_csv(out / 'sentiment_results.csv', index=False, encoding='utf-8')

        if topics:
            lines = ["LDA Topics\n" + "=" * 40 + "\n"]
            for i, topic in enumerate(topics, 1):
                lines.append(f"Topic {i}: {', '.join(topic)}\n")
            (out / 'topics_lda.txt').write_text(''.join(lines), encoding='utf-8')

        summary = self.parse_and_summarize(summary_ratio=0.01)
        (out / 'summary.txt').write_text(summary, encoding='utf-8')
        print(f"[OK] Todos los resultados exportados a '{out.resolve()}'")