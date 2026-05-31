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

import re
import unicodedata
import string
import pandas as pd

# Patrones compilados
RE_URL     = re.compile(r'https?://\S+|www\.\S+', re.IGNORECASE)
RE_MENTION = re.compile(r'@(\w+)')
RE_HASHTAG = re.compile(r'#(\w+)')
RE_SPECIAL = re.compile(r'[^\w\s#]', re.UNICODE)
RE_SPACES  = re.compile(r'\s+')

def clean_text(text: str) -> str:
    if not isinstance(text, str):
        text = str(text) if pd.notna(text) else ''
    text = text.strip().lower()
    text = RE_URL.sub(' ', text)
    text = RE_MENTION.sub(' ', text)
    text = ''.join(ch for ch in text if unicodedata.category(ch) not in ('So', 'Sk', 'Cs'))
    text = RE_SPECIAL.sub(' ', text)
    return RE_SPACES.sub(' ', text).strip()

def extract_hashtags(text: str) -> list:
    if not isinstance(text, str):
        return []
    seen, result = set(), []
    for tag in RE_HASHTAG.findall(text):
        t = tag.lower()
        if t not in seen:
            seen.add(t)
            result.append(t)
    return result

def extract_mentions(text: str) -> list:
    if not isinstance(text, str):
        return []
    seen, result = set(), []
    for mention in RE_MENTION.findall(text):
        m = mention.lower()
        if m not in seen:
            seen.add(m)
            result.append(m)
    return result

def analytics_hashtags_extended(df: pd.DataFrame) -> dict:
    df_copy = df.copy()
    if 'clean_text' not in df_copy.columns:
        df_copy['clean_text'] = df_copy['text'].apply(clean_text)
        
    df_copy['hashtags'] = df_copy['clean_text'].apply(extract_hashtags)
    df_copy['date'] = pd.to_datetime(df_copy['date'], utc=True, errors='coerce').dt.date

    df_exp = df_copy.explode('hashtags').dropna(subset=['hashtags'])
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

    print(f"[INFO] {len(overall)} hashtags unicos encontrados.")
    return {'overall': overall, 'by_user': by_user, 'by_date': by_date}

def generate_hashtag_wordcloud(overall_df: pd.DataFrame, max_words: int = 100, figsize: tuple = (10, 6)):
    import matplotlib.pyplot as plt
    from wordcloud import WordCloud

    freq_dict = dict(zip(overall_df['hashtag'], overall_df['frequency']))
    wc = WordCloud(width=figsize[0] * 100, height=figsize[1] * 100,
                   max_words=max_words, background_color='white',
                   colormap='viridis').generate_from_frequencies(freq_dict)

    plt.figure(figsize=figsize)
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('wordcloud_hashtags.png', dpi=150, bbox_inches='tight')
    plt.show()

def model_topics(df: pd.DataFrame, num_topics: int = 5, passes: int = 10, min_word_len: int = 3) -> list:
    import gensim
    from gensim import corpora
    import nltk
    from nltk.corpus import stopwords
    
    nltk.download('stopwords', quiet=True)
    stop_words = set(stopwords.words('english'))

    df_copy = df.copy()
    if 'clean_text' not in df_copy.columns:
        df_copy['clean_text'] = df_copy['text'].apply(clean_text)

    texts = []
    for text in df_copy['clean_text'].dropna():
        words = [w.lower() for w in text.split()
                 if (len(w) >= min_word_len
                     and not w.startswith('#')
                     and not w.isdigit()
                     and w not in stop_words
                     and not all(c.isdigit() or c in '-.' for c in w))]
        if words:
            texts.append(words)

    if not texts:
        raise ValueError("No quedan palabras despues del filtrado. Corpus demasiado pequeno.")

    dictionary = corpora.Dictionary(texts)
    corpus     = [dictionary.doc2bow(text) for text in texts]
    lda_model  = gensim.models.LdaModel(corpus, num_topics=num_topics,
                                        id2word=dictionary, passes=passes,
                                        random_state=42, workers=1)

    topics = [[w for w, _ in t[1]] for t in lda_model.show_topics(num_topics=num_topics, num_words=10, formatted=False)]
    print(f"[INFO] LDA completado: {num_topics} topicos ({len(texts)} documentos)")
    return topics

def analyze_sentiment(df: pd.DataFrame, method: str = 'textblob') -> pd.DataFrame:
    df_copy = df.copy()
    if 'clean_text' not in df_copy.columns:
        df_copy['clean_text'] = df_copy['text'].apply(clean_text)

    if method == 'textblob':
        from textblob import TextBlob
        df_copy['sentiment_polarity'] = df_copy['clean_text'].apply(lambda x: TextBlob(x).sentiment.polarity)
        df_copy['sentiment_subjectivity'] = df_copy['clean_text'].apply(lambda x: TextBlob(x).sentiment.subjectivity)
    elif method == 'spacy':
        import spacy
        from spacytextblob.spacytextblob import SpacyTextBlob
        nlp = spacy.load('en_core_web_sm')
        nlp.add_pipe('spacytextblob')
        df_copy['sentiment_polarity'] = df_copy['clean_text'].apply(lambda x: nlp(x)._.polarity)
        df_copy['sentiment_subjectivity'] = df_copy['clean_text'].apply(lambda x: nlp(x)._.subjectivity)
    else:
        raise ValueError(f"Metodo '{method}' no soportado.")
    return df_copy

def parse_and_summarize(df: pd.DataFrame, summary_ratio: float = 0.05, max_length: int = 500) -> str:
    import nltk
    from nltk.tokenize import sent_tokenize, word_tokenize
    from nltk.corpus import stopwords

    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)

    df_copy = df.copy()
    if 'clean_text' not in df_copy.columns:
        df_copy['clean_text'] = df_copy['text'].apply(clean_text)

    text = ' '.join(df_copy['clean_text'].dropna().tolist())
    sentences = sent_tokenize(text)
    if not sentences:
        return "[Corpus vacio – no se genero resumen]"

    stop_words = set(stopwords.words('english'))
    word_freq  = {}
    for sent in sentences:
        for word in word_tokenize(sent.lower()):
            if (len(word) >= 3 and not word.startswith('#') and not word.isdigit() 
                and word not in stop_words and word not in string.punctuation):
                word_freq[word] = word_freq.get(word, 0) + 1

    if not word_freq:
        return "[Corpus vacio – no se genero resumen]"

    sent_scores = {sent: sum(word_freq.get(w, 0) for w in word_tokenize(sent.lower()) if w not in string.punctuation)
                   for sent in sentences}

    ranked   = sorted([s for s in sent_scores if sent_scores[s] > 0], key=lambda s: sent_scores[s], reverse=True)
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

    return ' '.join(final) if final else "[Resumen vacio]"