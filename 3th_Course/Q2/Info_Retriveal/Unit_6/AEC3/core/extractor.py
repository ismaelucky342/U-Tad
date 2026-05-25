"""Main DataExtractor class: unified interface for the entire pipeline."""

import pandas as pd
import networkx as nx
from pathlib import Path

from .loader import DataLoader
from .cleaner import TextCleaner
from .analyzer import NLPAnalyzer
from .network import NetworkAnalyzer
from .llm import LLMHandler


class DataExtractor:
    """
    Central class encapsulating the entire Twitter analysis pipeline.
    
    Pipeline steps:
    1. load_data / load_data_api    - Load tweets
    2. clean_data                   - Normalize text
    3. build_interaction_graph      - Create mention graph
    4. analyze_network              - Network metrics
    5. generate_prompt_from_network - Create LLM prompt
    6. chat_local_llm               - Interactive LLM chat
    7. export_results               - Save outputs
    
    Example:
        ext = DataExtractor(source_file="tweets.csv")
        ext.execute_pipeline()
    """

    def __init__(self, source_file: str = None, chunksize: int = 100_000):
        """
        Initialize extractor.
        
        Args:
            source_file: Path to CSV/JSON data file or None (for API mode)
            chunksize: Chunk size for reading large CSVs
        """
        self.source_file = source_file
        self.data = None
        self.graph = None
        self.network_metrics = None
        self.chunksize = chunksize

    # ===== Data Loading =====

    def load_data(self) -> pd.DataFrame:
        """Load tweets from local CSV or JSON file."""
        if not self.source_file:
            raise ValueError("source_file not set. Use load_data_api() or provide source_file.")
        
        self.data = DataLoader.load_from_file(self.source_file, self.chunksize)
        return self.data

    def load_data_api(self, query: str, max_results: int = 100, 
                      output_file: str = "tweets_from_api.csv") -> pd.DataFrame:
        """Load tweets from RapidAPI Twitter endpoint."""
        self.data = DataLoader.load_from_api(query, max_results, output_file)
        self.source_file = output_file
        return self.data

    # ===== Data Cleaning =====

    def clean_data(self) -> pd.DataFrame:
        """Clean tweet text and extract hashtags."""
        if self.data is None:
            raise RuntimeError("No data loaded. Call load_data() or load_data_api() first.")
        
        self.data['clean_text'] = self.data['text'].apply(TextCleaner.clean_text)
        self.data['hashtags'] = self.data['clean_text'].apply(TextCleaner.extract_hashtags)
        print("[DataExtractor] Data cleaned")
        return self.data

    def analyze_hashtags(self) -> dict:
        """Analyze hashtag frequencies (global, by user, by date)."""
        if self.data is None:
            raise RuntimeError("No data loaded.")
        
        return TextCleaner.analyze_hashtags(self.data)

    # ===== NLP Analysis =====

    def analyze_sentiment(self, method: str = 'textblob') -> pd.DataFrame:
        """Analyze sentiment of all tweets."""
        if self.data is None:
            raise RuntimeError("No data loaded.")
        
        return NLPAnalyzer.analyze_sentiment(self.data, method)

    def model_topics(self, num_topics: int = 5, passes: int = 10) -> list:
        """Discover topics using LDA."""
        if self.data is None:
            raise RuntimeError("No data loaded.")
        
        return NLPAnalyzer.model_topics(self.data, num_topics, passes)

    def parse_and_summarize(self, summary_ratio: float = 0.05, max_length: int = 500) -> str:
        """Generate extractive summary."""
        if self.data is None:
            raise RuntimeError("No data loaded.")
        
        return NLPAnalyzer.parse_and_summarize(self.data, summary_ratio, max_length)

    def generate_wordcloud(self, max_words: int = 100, figsize: tuple = (10, 6)):
        """Generate hashtag wordcloud."""
        if self.data is None:
            raise RuntimeError("No data loaded.")
        
        analytics = self.analyze_hashtags()
        freq_dict = dict(zip(analytics['overall']['hashtag'], analytics['overall']['frequency']))
        NLPAnalyzer.generate_wordcloud(freq_dict, max_words, figsize)

    # ===== Network Analysis =====

    def build_interaction_graph(self) -> nx.DiGraph:
        """Build directed graph from mentions."""
        if self.data is None:
            raise RuntimeError("No data loaded.")
        
        self.graph = NetworkAnalyzer.build_interaction_graph(self.data)
        return self.graph

    def analyze_network(self) -> dict:
        """Analyze network metrics and communities."""
        if self.graph is None:
            raise RuntimeError("No graph built. Call build_interaction_graph() first.")
        
        self.network_metrics = NetworkAnalyzer.analyze_network(self.graph)
        return self.network_metrics

    def generate_prompt_from_network(self) -> str:
        """Generate LLM prompt from network insights."""
        if self.graph is None:
            raise RuntimeError("No graph built.")
        
        # Get most frequent hashtag if available
        hashtag_freq = None
        if self.data is not None:
            analytics = self.analyze_hashtags()
            hashtag_freq = dict(zip(analytics['overall']['hashtag'], analytics['overall']['frequency']))
        
        return NetworkAnalyzer.generate_prompt_from_network(self.graph, hashtag_freq)

    # ===== LLM Interaction =====

    def chat_local_llm(self, prompt: str = None, model_name: str = None,
                       max_new_tokens: int = 512, temperature: float = 0.7) -> None:
        """Start interactive LLM chat."""
        if model_name is None:
            from utils.constants import DEFAULT_LLM_MODEL
            model_name = DEFAULT_LLM_MODEL
        
        LLMHandler.chat_local_llm(prompt, model_name, max_new_tokens, temperature)

    def chat_api_llm(self, prompt: str) -> str:
        """Use Gemini API as fallback."""
        return LLMHandler.chat_api_llm(prompt)

    # ===== Pipeline Orchestration =====

    def execute_pipeline(self, output_dir: str = "outputs", run_llm: bool = True) -> None:
        """
        Execute the complete analysis pipeline in order.
        
        Steps:
        1. Load data (if not already loaded)
        2. Clean data
        3. Analyze hashtags
        4. Build interaction graph
        5. Analyze network
        6. Generate prompt from network
        7. Chat with LLM (optional)
        8. Export results
        
        Args:
            output_dir: Where to save outputs
            run_llm: Whether to run interactive LLM chat
        """
        print("\n" + "=" * 60)
        print("  EXECUTING PIPELINE")
        print("=" * 60 + "\n")

        # Step 1: Load
        if self.data is None:
            print("[Pipeline] Step 1/8: Loading data…")
            self.load_data()
        else:
            print("[Pipeline] Step 1/8: Data already loaded")

        # Step 2: Clean
        print("[Pipeline] Step 2/8: Cleaning data…")
        self.clean_data()

        # Step 3: Hashtags
        print("[Pipeline] Step 3/8: Analyzing hashtags…")
        self.analyze_hashtags()

        # Step 4: Graph
        print("[Pipeline] Step 4/8: Building interaction graph…")
        self.build_interaction_graph()

        # Step 5: Network
        print("[Pipeline] Step 5/8: Analyzing network…")
        self.analyze_network()

        # Step 6: Prompt
        print("[Pipeline] Step 6/8: Generating prompt…")
        prompt = self.generate_prompt_from_network()

        # Step 7: LLM
        if run_llm:
            print("[Pipeline] Step 7/8: Launching LLM chat…")
            self.chat_local_llm(prompt=prompt)
        else:
            print("[Pipeline] Step 7/8: Skipping LLM (run_llm=False)")

        # Step 8: Export
        print("[Pipeline] Step 8/8: Exporting results…")
        self.export_results(output_dir)

        print("\n" + "=" * 60)
        print("  PIPELINE COMPLETE")
        print("=" * 60 + "\n")

    # ===== Export =====

    def export_results(self, output_dir: str = "outputs") -> None:
        """
        Export all analysis results to files.
        
        Outputs:
        - tweets_clean.csv: cleaned tweets
        - hashtags_*.csv: hashtag analyses
        - sentiment_results.csv: sentiment scores
        - network_graph.png: graph visualization
        - network_prompt.txt: LLM prompt
        - summary.txt: extractive summary
        """
        out = Path(output_dir)
        out.mkdir(parents=True, exist_ok=True)

        print(f"\n[Export] Saving results to '{output_dir}/'\n")

        # Cleaned tweets
        if 'clean_text' in self.data.columns:
            cols = ['user_name', 'date', 'text', 'clean_text', 'hashtags']
            cols = [c for c in cols if c in self.data.columns]
            self.data[cols].to_csv(out / 'tweets_clean.csv', index=False, encoding='utf-8')
            print(f"  ✓ tweets_clean.csv ({len(self.data):,} rows)")

        # Hashtag analysis
        analytics = self.analyze_hashtags()
        for key, fname in [
            ('overall', 'hashtags_overall.csv'),
            ('by_user', 'hashtags_by_user.csv'),
            ('by_date', 'hashtags_by_date.csv')
        ]:
            analytics[key].to_csv(out / fname, index=False, encoding='utf-8')
            print(f"  ✓ {fname} ({len(analytics[key]):,} rows)")

        # Sentiment
        if 'sentiment_polarity' in self.data.columns:
            cols = ['user_name', 'date', 'text', 'clean_text', 'sentiment_polarity', 'sentiment_subjectivity']
            cols = [c for c in cols if c in self.data.columns]
            self.data[cols].to_csv(out / 'sentiment_results.csv', index=False, encoding='utf-8')
            print(f"  ✓ sentiment_results.csv ({len(self.data):,} rows)")

        # Network prompt
        if self.graph is not None:
            prompt = self.generate_prompt_from_network()
            (out / 'network_prompt.txt').write_text(prompt, encoding='utf-8')
            print(f"  ✓ network_prompt.txt")

        # Summary
        summary = self.parse_and_summarize(summary_ratio=0.01)
        (out / 'summary.txt').write_text(summary, encoding='utf-8')
        print(f"  ✓ summary.txt ({len(summary.split())} words)")

        print(f"\n✅ Export complete!\n")
