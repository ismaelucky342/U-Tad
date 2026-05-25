"""Data loading module: API and local file handling."""

import os
import pandas as pd
import requests
from pathlib import Path


class DataLoader:
    """Handles loading tweets from API or local CSV/JSON files."""

    @staticmethod
    def load_from_api(query: str, max_results: int = 100, output_file: str = "tweets.csv") -> pd.DataFrame:
        """
        Extract tweets from RapidAPI Twitter endpoint.
        
        Args:
            query: Search query (e.g., "#bitcoin")
            max_results: Max tweets to fetch
            output_file: Path to save CSV
            
        Returns:
            pd.DataFrame with columns: user_name, date, text
        """
        try:
            resp = requests.get(
                "https://twitter-api45.p.rapidapi.com/search.php",
                headers={
                    "X-RapidAPI-Key": os.environ.get("RAPIDAPI_KEY", ""),
                    "X-RapidAPI-Host": "twitter-api45.p.rapidapi.com"
                },
                params={"query": query, "count": max_results},
                timeout=15
            )
            resp.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"API request failed: {e}")

        response_json = resp.json()
        tweets_list = None
        for key in ['tweets', 'data', 'timeline', 'results', 'statuses']:
            if key in response_json and isinstance(response_json[key], list):
                tweets_list = response_json[key]
                break

        if tweets_list is None:
            raise ValueError(f"No tweets found. Response keys: {list(response_json.keys())}")

        rows = []
        for t in tweets_list:
            if not isinstance(t, dict):
                continue
            text = t.get('text') or t.get('full_text') or t.get('body') or ''
            user = t.get('user_name') or t.get('author_id') or t.get('user', {}).get('name') or 'unknown'
            date = t.get('date') or t.get('created_at') or t.get('timestamp') or ''
            if text.strip():
                rows.append({
                    'user_name': str(user).strip(),
                    'date': str(date).strip(),
                    'text': str(text).strip()
                })

        if not rows:
            raise ValueError("No valid tweets extracted from API response")

        df = pd.DataFrame(rows)
        df.to_csv(output_file, index=False, encoding="utf-8")
        print(f"[DataLoader] {len(df)} tweets extracted → '{output_file}'")
        return df

    @staticmethod
    def load_from_file(source: str, chunksize: int = 100_000) -> pd.DataFrame:
        """
        Load tweets from local CSV or JSON file.
        For large CSVs, uses chunksize to avoid memory overload.
        
        Args:
            source: Path to CSV or JSON
            chunksize: Chunk size for reading large files
            
        Returns:
            pd.DataFrame with tweet data
        """
        path = Path(source)
        ext = path.suffix.lower()

        if ext == '.json':
            data = pd.read_json(source, encoding='utf-8')
        elif ext == '.csv':
            chunks = pd.read_csv(source, encoding='utf-8', chunksize=chunksize, low_memory=False)
            data = pd.concat(chunks, ignore_index=True)
        else:
            raise ValueError(f"Unsupported format: '{ext}'. Use .csv or .json")

        # Clean column names
        data.columns = [c.strip().replace('\r', '') for c in data.columns]
        print(f"[DataLoader] {len(data):,} rows loaded – columns: {list(data.columns)}")
        return data
