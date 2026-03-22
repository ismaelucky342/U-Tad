from pathlib import Path

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# ---- Importo DataExtractor aqui para que sea autocontenido -------------------
# Asi no dependo de que el notebook este en el PYTHONPATH.
import re
import unicodedata


class DataExtractor:
    """Copia minima de DataExtractor para el dashboard (misma logica)."""

    _RE_URL     = re.compile(r'https?://\S+|www\.\S+', re.IGNORECASE)
    _RE_MENTION = re.compile(r'@\w+')
    _RE_HASHTAG = re.compile(r'#(\w+)')
    _RE_SPECIAL = re.compile(r'[^\w\s#]', re.UNICODE)
    _RE_SPACES  = re.compile(r'\s+')

    def __init__(self, source_file: str, chunksize: int = 100_000):
        self.source_file = source_file
        self.data = None
        self.chunksize = chunksize

    def load_data(self) -> pd.DataFrame:
        path = Path(self.source_file)
        ext  = path.suffix.lower()
        if ext == '.json':
            self.data = pd.read_json(self.source_file, encoding='utf-8')
        elif ext == '.csv':
            chunks = pd.read_csv(
                self.source_file,
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


# ---- Interfaz Streamlit -----------------------------------------------------

st.set_page_config(
    page_title="Bitcoin Tweets – Hashtag Dashboard",
    page_icon="₿",
    layout="wide",
)

st.title("₿ Bitcoin Tweets – Hashtag Analysis Dashboard")
st.caption("AEC1 · Information Retrieval · 3rd Course Q2")

# ---- Barra lateral: carga del CSV ------------------------------------------
st.sidebar.header("Configuration")
uploaded = st.sidebar.file_uploader(
    "Upload CSV dataset",
    type=["csv"],
    help="Upload Bitcoin_tweets_dataset_2.csv",
)
top_n = st.sidebar.slider("Top N hashtags", min_value=5, max_value=50, value=20)
max_words_wc = st.sidebar.slider("WordCloud max words", min_value=20, max_value=200, value=100)

if uploaded is None:
    st.info("Sube el CSV de Bitcoin tweets en la barra lateral para empezar.")
    st.stop()

# ---- Cargo y cacheo los datos ----------------------------------------------
@st.cache_data(show_spinner="Loading and processing data...")
def load_and_analyse(file_bytes: bytes) -> dict:
    import tempfile, os
    with tempfile.NamedTemporaryFile(delete=False, suffix='.csv') as tmp:
        tmp.write(file_bytes)
        tmp_path = tmp.name
    try:
        ext = DataExtractor(tmp_path, chunksize=100_000)
        ext.load_data()
        analytics = ext.analytics_hashtags_extended()
        n_tweets = len(ext.data)
    finally:
        os.unlink(tmp_path)
    return {'analytics': analytics, 'n_tweets': n_tweets}


result    = load_and_analyse(uploaded.read())
analytics = result['analytics']
n_tweets  = result['n_tweets']
overall   = analytics['overall']
by_user   = analytics['by_user']
by_date   = analytics['by_date']

# ---- KPIs -------------------------------------------------------------------
col1, col2, col3 = st.columns(3)
col1.metric("Total tweets",    f"{n_tweets:,}")
col2.metric("Unique hashtags", f"{len(overall):,}")
col3.metric("Unique users",    f"{by_user['user_name'].nunique():,}")

st.divider()

# ---- Tabs -------------------------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs(["📊 Top Hashtags", "☁️ WordCloud", "📈 Evolution", "🤖 Bot Analysis"])

# Tab 1 – Bar chart -----------------------------------------------------------
with tab1:
    st.subheader(f"Top {top_n} Hashtags – Global Frequency")
    top_df = overall.head(top_n)

    fig, ax = plt.subplots(figsize=(9, top_n * 0.38 + 1))
    bars = ax.barh(top_df['hashtag'][::-1], top_df['frequency'][::-1], color='steelblue')
    ax.bar_label(bars, fmt='%d', padding=3, fontsize=8)
    ax.set_xlabel('Frequency')
    ax.set_title(f'Top {top_n} Hashtags', fontsize=13, fontweight='bold')
    plt.tight_layout()
    st.pyplot(fig)

    with st.expander("Show raw data"):
        st.dataframe(top_df, use_container_width=True)

# Tab 2 – WordCloud -----------------------------------------------------------
with tab2:
    st.subheader("Hashtag WordCloud")
    freq_dict = dict(zip(overall['hashtag'], overall['frequency']))
    wc = WordCloud(
        width=1200, height=600, max_words=max_words_wc,
        background_color='white', colormap='viridis',
    ).generate_from_frequencies(freq_dict)

    fig2, ax2 = plt.subplots(figsize=(12, 6))
    ax2.imshow(wc, interpolation='bilinear')
    ax2.axis('off')
    plt.tight_layout()
    st.pyplot(fig2)

# Tab 3 – Evolucion -----------------------------------------------------------
with tab3:
    st.subheader("Daily Evolution of Top 5 Hashtags")
    top5 = overall.head(5)['hashtag'].tolist()

    pivot = (
        by_date[by_date['hashtag'].isin(top5)]
        .pivot_table(index='date', columns='hashtag', values='frequency', aggfunc='sum')
        .fillna(0)
        .sort_index()
    )

    if pivot.empty:
        st.warning("Not enough date data to plot evolution.")
    else:
        fig3, ax3 = plt.subplots(figsize=(12, 4))
        pivot.plot(ax=ax3, linewidth=1.5, alpha=0.85)
        ax3.set_xlabel('Date')
        ax3.set_ylabel('Frequency')
        ax3.set_title('Daily Hashtag Frequency – Top 5', fontsize=13, fontweight='bold')
        plt.xticks(rotation=30, ha='right')
        plt.tight_layout()
        st.pyplot(fig3)

# Tab 4 – Posibles bots -------------------------------------------------------
with tab4:
    st.subheader("Potential Bot Detection")
    st.markdown(
        "Users that post a disproportionate number of hashtag-containing tweets "
        "may be automated accounts (bots)."
    )

    user_totals = (
        by_user.groupby('user_name', as_index=False)['frequency']
               .sum()
               .sort_values('frequency', ascending=False)
    )
    total = user_totals['frequency'].sum()
    top1  = max(1, int(len(user_totals) * 0.01))
    top1_sum = user_totals.head(top1)['frequency'].sum()

    col_a, col_b = st.columns(2)
    col_a.metric("Top 1% users cover", f"{top1_sum / total * 100:.1f}% of hashtag uses")
    col_b.metric("Users in top 1%", f"{top1:,}")

    st.subheader("Top 20 most active users (by hashtag volume)")
    st.dataframe(user_totals.head(20), use_container_width=True)
