"""Text cleaning and hashtag extraction module."""

import unicodedata
import pandas as pd
from utils.constants import RE_URL, RE_MENTION, RE_HASHTAG, RE_SPECIAL, RE_SPACES


class TextCleaner:
    """Text normalization and hashtag extraction utilities."""

    @staticmethod
    def clean_text(text: str) -> str:
        """
        Normalize tweet text: lowercase, remove URLs/mentions/emojis, keep hashtags.
        
        Args:
            text: Raw tweet text
            
        Returns:
            Cleaned text (lowercase, no URLs, no mentions, no emojis, no special chars except #)
        """
        if not isinstance(text, str):
            text = str(text) if pd.notna(text) else ''
        
        text = text.strip().lower()
        text = RE_URL.sub(' ', text)
        text = RE_MENTION.sub(' ', text)
        # Remove emoji (Unicode categories So=Symbol/other, Sk=Symbol/modifier, Cs=Other/surrogate)
        text = ''.join(ch for ch in text if unicodedata.category(ch) not in ('So', 'Sk', 'Cs'))
        text = RE_SPECIAL.sub(' ', text)
        return RE_SPACES.sub(' ', text).strip()

    @staticmethod
    def extract_hashtags(text: str) -> list:
        """
        Extract unique hashtags from text in order of appearance.
        
        Args:
            text: Text to extract hashtags from
            
        Returns:
            List of unique hashtags (lowercase)
        """
        if not isinstance(text, str):
            return []
        
        seen, result = set(), []
        for tag in RE_HASHTAG.findall(text):
            t = tag.lower()
            if t not in seen:
                seen.add(t)
                result.append(t)
        return result

    @staticmethod
    def analyze_hashtags(df: pd.DataFrame) -> dict:
        """
        Analyze hashtag frequencies: global, by user, by date.
        
        Args:
            df: DataFrame with 'user_name', 'date', 'text' columns
            
        Returns:
            Dict with DataFrames: {'overall': ..., 'by_user': ..., 'by_date': ...}
        """
        df = df.copy()
        df['clean_text'] = df['text'].apply(TextCleaner.clean_text)
        df['hashtags'] = df['clean_text'].apply(TextCleaner.extract_hashtags)
        df['date'] = pd.to_datetime(df['date'], utc=True, errors='coerce').dt.date

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

        print(f"[TextCleaner] {len(overall)} unique hashtags found")
        return {'overall': overall, 'by_user': by_user, 'by_date': by_date}
