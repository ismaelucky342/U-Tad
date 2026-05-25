"""NLP analysis module: sentiment, topic modeling, summarization."""

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud


class NLPAnalyzer:
    """Sentiment analysis, topic modeling, and text summarization."""

    @staticmethod
    def generate_wordcloud(hashtag_freq: dict, max_words: int = 100, figsize: tuple = (10, 6)):
        """
        Generate and display a wordcloud from hashtag frequencies.
        
        Args:
            hashtag_freq: Dict mapping hashtag → frequency
            max_words: Max words in wordcloud
            figsize: Figure size (width, height)
        """
        wc = WordCloud(
            width=figsize[0] * 100, height=figsize[1] * 100,
            max_words=max_words,
            background_color='white', colormap='viridis'
        ).generate_from_frequencies(hashtag_freq)

        plt.figure(figsize=figsize)
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.tight_layout()
        plt.show()

    @staticmethod
    def analyze_sentiment(df: pd.DataFrame, method: str = 'textblob') -> pd.DataFrame:
        """
        Analyze sentiment (polarity & subjectivity) of tweets.
        
        Args:
            df: DataFrame with 'clean_text' column
            method: 'textblob' (fast) or 'spacy' (slower, more accurate)
            
        Returns:
            DataFrame with added 'sentiment_polarity' and 'sentiment_subjectivity' columns
        """
        if 'clean_text' not in df.columns:
            raise ValueError("DataFrame must have 'clean_text' column. Run clean_data() first.")

        if method == 'textblob':
            from textblob import TextBlob
            df['sentiment_polarity'] = df['clean_text'].apply(
                lambda x: TextBlob(x).sentiment.polarity
            )
            df['sentiment_subjectivity'] = df['clean_text'].apply(
                lambda x: TextBlob(x).sentiment.subjectivity
            )
        
        elif method == 'spacy':
            try:
                import spacy
                from spacytextblob.spacytextblob import SpacyTextBlob
            except ImportError:
                raise ImportError("spacy and spacytextblob required. Install via: pip install spacy spacytextblob")
            
            nlp = spacy.load('en_core_web_sm')
            nlp.add_pipe('spacytextblob')
            df['sentiment_polarity'] = df['clean_text'].apply(lambda x: nlp(x)._.polarity)
            df['sentiment_subjectivity'] = df['clean_text'].apply(lambda x: nlp(x)._.subjectivity)
        
        else:
            raise ValueError(f"Method '{method}' not supported. Use 'textblob' or 'spacy'.")

        print(f"[NLPAnalyzer] Sentiment analysis complete (method: {method})")
        return df

    @staticmethod
    def model_topics(df: pd.DataFrame, num_topics: int = 5, passes: int = 10) -> list:
        """
        Discover topics using LDA (Latent Dirichlet Allocation).
        
        Args:
            df: DataFrame with 'clean_text' column
            num_topics: Number of topics to extract
            passes: Number of LDA passes for convergence
            
        Returns:
            List of topics, each topic is a list of 10 words
        """
        try:
            from gensim import corpora
            import gensim
        except ImportError:
            raise ImportError("gensim required. Install via: pip install gensim")

        if 'clean_text' not in df.columns:
            raise ValueError("DataFrame must have 'clean_text' column.")

        # Tokenize by splitting on spaces
        texts = df['clean_text'].dropna().apply(lambda x: x.split()).tolist()
        
        if not texts:
            raise ValueError("No texts to model. Corpus is empty after cleaning.")

        dictionary = corpora.Dictionary(texts)
        corpus = [dictionary.doc2bow(text) for text in texts]

        lda_model = gensim.models.LdaModel(
            corpus, num_topics=num_topics, id2word=dictionary,
            passes=passes, random_state=42, workers=1
        )

        topics = []
        for t in lda_model.show_topics(num_topics=num_topics, num_words=10, formatted=False):
            topics.append([w for w, _ in t[1]])

        print(f"[NLPAnalyzer] LDA: {num_topics} topics discovered ({len(texts)} documents)")
        return topics

    @staticmethod
    def parse_and_summarize(df: pd.DataFrame, summary_ratio: float = 0.05, max_length: int = 500) -> str:
        """
        Generate extractive summary from corpus.
        Ranks sentences by word frequency and selects top ones.
        
        Args:
            df: DataFrame with 'clean_text' column
            summary_ratio: Fraction of original sentences to select (0.05 = 5%)
            max_length: Max words in final summary
            
        Returns:
            Summary text (extractive)
        """
        try:
            import nltk
            from nltk.tokenize import sent_tokenize, word_tokenize
            from nltk.corpus import stopwords
            import string
        except ImportError:
            raise ImportError("nltk required. Install via: pip install nltk")

        nltk.download('punkt', quiet=True)
        nltk.download('punkt_tab', quiet=True)
        nltk.download('stopwords', quiet=True)

        if 'clean_text' not in df.columns:
            raise ValueError("DataFrame must have 'clean_text' column.")

        # Combine all tweets into one document
        text = ' '.join(df['clean_text'].dropna().tolist())
        sentences = sent_tokenize(text)
        
        if not sentences:
            return "[Empty summary]"

        stop_words = set(stopwords.words('english'))

        # Calculate word frequencies
        word_freq = {}
        for sent in sentences:
            for word in word_tokenize(sent.lower()):
                if word not in stop_words and word not in string.punctuation:
                    word_freq[word] = word_freq.get(word, 0) + 1

        if not word_freq:
            return "[Empty summary]"

        # Score sentences by word frequency
        sent_scores = {
            sent: sum(word_freq.get(w, 0) for w in word_tokenize(sent.lower()) if w not in string.punctuation)
            for sent in sentences
        }

        # Select top sentences
        n_select = max(1, int(len(sentences) * summary_ratio))
        ranked = sorted([s for s in sent_scores if sent_scores[s] > 0], 
                       key=lambda s: sent_scores[s], reverse=True)
        selected = sorted(ranked[:n_select], key=sentences.index)

        # Build summary respecting max_length
        result_words, final = 0, []
        for sent in selected:
            sent_len = len(sent.split())
            if result_words + sent_len <= max_length:
                final.append(sent)
                result_words += sent_len
            elif result_words < max_length:
                final.append(sent)
                break

        print(f"[NLPAnalyzer] Summary: {len(final)} sentences, {result_words} words")
        return ' '.join(final) if final else "[Empty summary]"
