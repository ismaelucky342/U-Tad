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

import tempfile
import os
import io
import pandas as pd
import networkx as nx
import requests
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from wordcloud import WordCloud

from src import DataExtractor


# ─────────────────────────────────────────────────────────────────────────────
# Configuración de página
# ─────────────────────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="Bitcoin Tweets – Dashboard AEC3",
    page_icon="₿",
    layout="wide",
)

st.title("₿ Bitcoin Tweets – Dashboard AEC3")
st.caption("BAIN · Análisis de Sentimiento, Redes e Integración LLM")

# ─────────────────────────────────────────────────────────────────────────────
# Sidebar: carga de datos y parámetros
# ─────────────────────────────────────────────────────────────────────────────

st.sidebar.header("⚙️ Configuración")

uploaded = st.sidebar.file_uploader(
    "Sube el CSV de tweets",
    type=["csv"],
    help="Formato esperado: columnas user_name, date, text",
)

st.sidebar.subheader("Parámetros de visualización")
top_n        = st.sidebar.slider("Top N hashtags",         5,  50,  20)
max_words_wc = st.sidebar.slider("WordCloud – max words", 20, 200, 100)
max_nodes    = st.sidebar.slider("Red – max nodos (top PageRank)", 20, 150, 60)

st.sidebar.subheader("LLM – Ollama")
ollama_url   = st.sidebar.text_input("URL de Ollama", value="http://localhost:11434")
llm_model    = st.sidebar.text_input("Modelo",        value="gemma3")

if uploaded is None:
    st.info("👆 Sube el CSV de Bitcoin tweets en la barra lateral para comenzar.")
    st.stop()


# ─────────────────────────────────────────────────────────────────────────────
# Carga y análisis de datos (con caché)
# ─────────────────────────────────────────────────────────────────────────────

@st.cache_data(show_spinner="⏳ Procesando tweets…")
def load_and_analyse(file_bytes: bytes):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.csv') as tmp:
        tmp.write(file_bytes)
        tmp_path = tmp.name
    try:
        ext = DataExtractor(tmp_path, chunksize=100_000)
        ext.load_data()
        analytics = ext.analytics_hashtags_extended()
        n_tweets  = len(ext.data)
        # Guardar datos para uso posterior fuera del caché
        data_copy = ext.data.copy()
    finally:
        os.unlink(tmp_path)
    return analytics, n_tweets, data_copy


@st.cache_data(show_spinner="🕸️ Construyendo grafo de interacciones…")
def build_graph(data_json: str):
    """Reconstruye DataExtractor desde JSON para poder cachear el resultado."""
    import io
    df  = pd.read_json(io.StringIO(data_json))
    ext = DataExtractor()
    ext.data = df
    G   = ext.build_interaction_graph()
    return G


@st.cache_data(show_spinner="📐 Calculando métricas de red…")
def compute_metrics(data_json: str):
    import io
    df  = pd.read_json(io.StringIO(data_json))
    ext = DataExtractor()
    ext.data = df
    G = ext.build_interaction_graph()
    in_deg   = nx.in_degree_centrality(G)
    pagerank = nx.pagerank(G, weight='weight', max_iter=200)
    betw     = nx.betweenness_centrality(G, weight='weight', normalized=True)
    density  = nx.density(G)
    n_nodes  = G.number_of_nodes()
    n_edges  = G.number_of_edges()

    try:
        from community import best_partition
        partition     = best_partition(G.to_undirected(), weight='weight')
        n_communities = len(set(partition.values()))
    except Exception:
        from networkx.algorithms.community import greedy_modularity_communities
        comms = list(greedy_modularity_communities(G.to_undirected(), weight='weight'))
        n_communities = len(comms)
        partition = {}
        for idx, comm in enumerate(comms):
            for node in comm:
                partition[node] = idx

    top3_in  = sorted(in_deg.items(),   key=lambda x: x[1], reverse=True)[:3]
    top3_pr  = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)[:3]
    top3_btw = sorted(betw.items(),     key=lambda x: x[1], reverse=True)[:3]

    return {
        'n_nodes': n_nodes, 'n_edges': n_edges, 'density': density,
        'n_communities': n_communities, 'partition': partition,
        'pagerank': pagerank, 'in_deg': in_deg, 'betw': betw,
        'top3_in': top3_in, 'top3_pr': top3_pr, 'top3_btw': top3_btw,
    }, G


# ─────────────────────────────────────────────────────────────────────────────
# Ejecutar análisis
# ─────────────────────────────────────────────────────────────────────────────

analytics, n_tweets, data = load_and_analyse(uploaded.read())
overall   = analytics['overall']
by_user   = analytics['by_user']
by_date   = analytics['by_date']

# Serializar para pasar a funciones cacheadas
data_json = data.to_json()

# ─────────────────────────────────────────────────────────────────────────────
# KPIs globales
# ─────────────────────────────────────────────────────────────────────────────

col1, col2, col3 = st.columns(3)
col1.metric("Tweets totales",    f"{n_tweets:,}")
col2.metric("Hashtags únicos",   f"{len(overall):,}")
col3.metric("Usuarios únicos",   f"{by_user['user_name'].nunique():,}")

st.divider()

# ─────────────────────────────────────────────────────────────────────────────
# Tabs
# ─────────────────────────────────────────────────────────────────────────────

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📊 Top Hashtags",
    "☁️ WordCloud",
    "📈 Evolución",
    "🤖 Bots",
    "🕸️ Red de Menciones",
    "💬 Chat LLM",
])

# ── Tab 1 – Top Hashtags ─────────────────────────────────────────────────────
with tab1:
    st.subheader(f"Top {top_n} Hashtags – Frecuencia global")
    top_df = overall.head(top_n)

    fig, ax = plt.subplots(figsize=(9, top_n * 0.38 + 1))
    bars = ax.barh(top_df['hashtag'][::-1], top_df['frequency'][::-1], color='steelblue')
    ax.bar_label(bars, fmt='%d', padding=3, fontsize=8)
    ax.set_xlabel('Frecuencia')
    ax.set_title(f'Top {top_n} Hashtags', fontsize=13, fontweight='bold')
    plt.tight_layout()
    st.pyplot(fig)

    with st.expander("📋 Ver datos"):
        st.dataframe(top_df, use_container_width=True)

# ── Tab 2 – WordCloud ────────────────────────────────────────────────────────
with tab2:
    st.subheader("Nube de palabras – Hashtags")
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

# ── Tab 3 – Evolución temporal ───────────────────────────────────────────────
with tab3:
    st.subheader("Evolución diaria – Top 5 hashtags")
    top5  = overall.head(5)['hashtag'].tolist()
    pivot = (
        by_date[by_date['hashtag'].isin(top5)]
        .pivot_table(index='date', columns='hashtag',
                     values='frequency', aggfunc='sum')
        .fillna(0).sort_index()
    )

    if pivot.empty:
        st.warning("No hay suficientes datos temporales para trazar la evolución.")
    else:
        fig3, ax3 = plt.subplots(figsize=(12, 4))
        pivot.plot(ax=ax3, linewidth=1.5, alpha=0.85)
        ax3.set_xlabel('Fecha')
        ax3.set_ylabel('Frecuencia')
        ax3.set_title('Frecuencia diaria – Top 5 hashtags', fontsize=13, fontweight='bold')
        plt.xticks(rotation=30, ha='right')
        plt.tight_layout()
        st.pyplot(fig3)

# ── Tab 4 – Detección de bots ────────────────────────────────────────────────
with tab4:
    st.subheader("Detección de posibles bots")
    st.markdown(
        "Usuarios que publican un número desproporcionado de hashtags "
        "pueden ser cuentas automatizadas."
    )

    user_totals = (
        by_user.groupby('user_name', as_index=False)['frequency']
               .sum()
               .sort_values('frequency', ascending=False)
    )
    total    = user_totals['frequency'].sum()
    top1_n   = max(1, int(len(user_totals) * 0.01))
    top1_sum = user_totals.head(top1_n)['frequency'].sum()

    c1, c2 = st.columns(2)
    c1.metric("Top 1% de usuarios cubre", f"{top1_sum / total * 100:.1f}% del uso de hashtags")
    c2.metric("Usuarios en top 1%",       f"{top1_n:,}")

    st.subheader("Top 20 usuarios más activos (por volumen de hashtags)")
    st.dataframe(user_totals.head(20), use_container_width=True)

# ── Tab 5 – Red de menciones ─────────────────────────────────────────────────
with tab5:
    st.subheader("🕸️ Red de interacciones (menciones entre usuarios)")

    st.info(
        "Se construye un grafo dirigido donde cada nodo es un usuario y cada "
        "arista representa una mención. El tamaño del nodo refleja su PageRank."
    )

    if st.button("🔨 Construir grafo y calcular métricas"):
        with st.spinner("Construyendo grafo…"):
            metrics, G = compute_metrics(data_json)

        # ── KPIs de red ──────────────────────────────────────────────────────
        mc1, mc2, mc3, mc4 = st.columns(4)
        mc1.metric("Nodos",        f"{metrics['n_nodes']:,}")
        mc2.metric("Aristas",      f"{metrics['n_edges']:,}")
        mc3.metric("Densidad",     f"{metrics['density']:.4f}")
        mc4.metric("Comunidades",  f"{metrics['n_communities']}")

        # ── Tablas de centralidad ────────────────────────────────────────────
        col_a, col_b, col_c = st.columns(3)

        with col_a:
            st.markdown("**Top 3 – In-degree centrality**")
            df_in = pd.DataFrame(metrics['top3_in'], columns=['Usuario', 'Centralidad'])
            df_in['Usuario'] = df_in['Usuario'].apply(lambda x: f"@{x}")
            st.dataframe(df_in, use_container_width=True)

        with col_b:
            st.markdown("**Top 3 – PageRank**")
            df_pr = pd.DataFrame(metrics['top3_pr'], columns=['Usuario', 'PageRank'])
            df_pr['Usuario'] = df_pr['Usuario'].apply(lambda x: f"@{x}")
            st.dataframe(df_pr, use_container_width=True)

        with col_c:
            st.markdown("**Top 3 – Betweenness centrality**")
            df_bt = pd.DataFrame(metrics['top3_btw'], columns=['Usuario', 'Betweenness'])
            df_bt['Usuario'] = df_bt['Usuario'].apply(lambda x: f"@{x}")
            st.dataframe(df_bt, use_container_width=True)

        # ── Visualización del grafo ──────────────────────────────────────────
        st.markdown("---")
        st.subheader("Visualización del grafo")

        pagerank  = metrics['pagerank']
        partition = metrics['partition']

        # Subgrafo con top N nodos por PageRank
        top_nodes = sorted(pagerank, key=pagerank.get, reverse=True)[:max_nodes]
        subG      = G.subgraph(top_nodes).copy()
        subpart   = {n: partition.get(n, 0) for n in top_nodes}

        fig_g, axes = plt.subplots(1, 2, figsize=(16, 7))

        # Panel izquierdo: grafo coloreado por comunidad
        ax1 = axes[0]
        try:
            pos = nx.spring_layout(subG, seed=42, k=0.6)
        except Exception:
            pos = nx.random_layout(subG, seed=42)

        n_comms = max(subpart.values()) + 1 if subpart else 1
        cmap    = cm.get_cmap('tab20', n_comms)
        colors  = [cmap(subpart.get(n, 0) % n_comms) for n in subG.nodes()]
        sizes   = [200 + pagerank.get(n, 0) * 12000 for n in subG.nodes()]
        weights = [subG[u][v]['weight'] for u, v in subG.edges()]
        max_w   = max(weights) if weights else 1

        nx.draw_networkx_nodes(subG, pos, ax=ax1, node_color=colors,
                               node_size=sizes, alpha=0.85)
        nx.draw_networkx_edges(subG, pos, ax=ax1,
                               width=[0.5 + 2 * (w / max_w) for w in weights],
                               alpha=0.35, arrows=True,
                               arrowstyle='->', arrowsize=8, edge_color='gray')
        top10_labels = {n: f"@{n}" for n in
                        sorted(pagerank, key=pagerank.get, reverse=True)[:10]
                        if n in subG.nodes()}
        nx.draw_networkx_labels(subG, pos, labels=top10_labels,
                                ax=ax1, font_size=7, font_weight='bold')
        ax1.set_title(f"Red de menciones – {max_nodes} nodos (coloreado por comunidad)",
                      fontsize=11)
        ax1.axis('off')

        # Panel derecho: histograma de in-degree
        ax2  = axes[1]
        degs = [d for _, d in G.in_degree()]
        ax2.hist(degs, bins=min(50, max(degs) + 1) if degs else 10,
                 color='steelblue', edgecolor='white', alpha=0.85)
        ax2.set_xlabel("In-degree (veces mencionado)", fontsize=11)
        ax2.set_ylabel("Número de nodos",              fontsize=11)
        ax2.set_title("Distribución de in-degree",     fontsize=11)
        ax2.set_yscale('log')

        plt.suptitle("Análisis de red de interacciones en Twitter",
                     fontsize=13, fontweight='bold')
        plt.tight_layout()
        st.pyplot(fig_g)

        # Guardar métricas en session_state para usarlas en el tab LLM
        st.session_state['network_metrics'] = metrics
        st.session_state['network_G_nodes'] = list(G.nodes())
        st.session_state['network_G_edges'] = [(u, v, d) for u, v, d in G.edges(data=True)]
        st.success("✅ Grafo construido. Ve al tab '💬 Chat LLM' para el análisis interpretativo.")

# ── Tab 6 – Chat LLM ─────────────────────────────────────────────────────────
with tab6:
    st.subheader("💬 Chat con LLM local (Ollama – gemma3)")

    st.info(
        f"Conecta con tu instancia de Ollama en `{ollama_url}` usando el modelo `{llm_model}`. "
        "Asegúrate de que Ollama está en ejecución y de que el modelo está descargado."
    )

    # ── Verificar conexión con Ollama ────────────────────────────────────────
    col_ping, col_info = st.columns([1, 3])
    with col_ping:
        if st.button("🔌 Verificar conexión con Ollama"):
            try:
                ping = requests.get(f"{ollama_url.rstrip('/')}/api/tags", timeout=5)
                models_available = [m['name'] for m in ping.json().get('models', [])]
                if any(llm_model in m for m in models_available):
                    st.success(f"✅ Conectado. Modelo '{llm_model}' disponible.")
                else:
                    st.warning(
                        f"⚠️ Ollama activo pero '{llm_model}' no está descargado.\n"
                        f"Modelos disponibles: {models_available}\n"
                        f"Ejecuta: ollama pull {llm_model}"
                    )
            except Exception as e:
                st.error(f"❌ No se puede conectar a Ollama: {e}")

    st.markdown("---")

    # ── Generar prompt desde la red ──────────────────────────────────────────
    st.subheader("1. Generar prompt desde el análisis de red")

    if 'network_metrics' not in st.session_state:
        st.warning("⚠️ Primero construye el grafo en el tab '🕸️ Red de Menciones'.")
    else:
        metrics = st.session_state['network_metrics']

        if st.button("📝 Generar prompt de análisis de red"):
            # Reconstruir grafo mínimo para el método generate_prompt_from_network
            G_mini = nx.DiGraph()
            for node in st.session_state.get('network_G_nodes', []):
                G_mini.add_node(node)
            for u, v, d in st.session_state.get('network_G_edges', []):
                G_mini.add_edge(u, v, **d)

            ext = DataExtractor()
            ext.data = data

            prompt = ext.generate_prompt_from_network(G_mini, metrics={
                'top3_in_degree':  metrics['top3_in'],
                'top3_pagerank':   metrics['top3_pr'],
                'n_nodes':         metrics['n_nodes'],
                'n_edges':         metrics['n_edges'],
                'density':         metrics['density'],
                'n_communities':   metrics['n_communities'],
            })
            st.session_state['generated_prompt'] = prompt
            st.success("✅ Prompt generado.")

        if 'generated_prompt' in st.session_state:
            with st.expander("📄 Ver prompt generado"):
                st.text_area("Prompt", st.session_state['generated_prompt'],
                             height=300, disabled=True)

    st.markdown("---")

    # ── Chat interactivo ─────────────────────────────────────────────────────
    st.subheader("2. Chat con el LLM")

    # Inicializar historial de conversación
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    # Mostrar historial existente
    for msg in st.session_state['chat_history']:
        role  = msg['role']
        icon  = "👤" if role == 'user' else "🤖"
        label = "Tú" if role == 'user' else llm_model
        with st.chat_message(role):
            st.markdown(f"**{icon} {label}**\n\n{msg['content']}")

    # Botón para enviar el prompt de red como primer mensaje
    if ('generated_prompt' in st.session_state and
            not st.session_state.get('prompt_sent', False)):
        if st.button("🚀 Enviar análisis de red al LLM"):
            prompt_text = st.session_state['generated_prompt']
            st.session_state['chat_history'].append(
                {'role': 'user', 'content': prompt_text}
            )
            with st.spinner(f"⏳ {llm_model} está analizando la red…"):
                try:
                    payload = {
                        "model":    llm_model,
                        "messages": st.session_state['chat_history'],
                        "stream":   False,
                    }
                    resp = requests.post(
                        f"{ollama_url.rstrip('/')}/api/chat",
                        json=payload, timeout=300
                    )
                    resp.raise_for_status()
                    answer = resp.json().get('message', {}).get('content', '')
                    st.session_state['chat_history'].append(
                        {'role': 'assistant', 'content': answer}
                    )
                    st.session_state['prompt_sent'] = True
                    st.rerun()
                except Exception as e:
                    st.error(f"Error al conectar con Ollama: {e}")

    # Input para preguntas de seguimiento
    user_input = st.chat_input("Escribe tu mensaje…")
    if user_input:
        st.session_state['chat_history'].append(
            {'role': 'user', 'content': user_input}
        )
        with st.spinner(f"⏳ {llm_model} está pensando…"):
            try:
                payload = {
                    "model":    llm_model,
                    "messages": st.session_state['chat_history'],
                    "stream":   False,
                }
                resp = requests.post(
                    f"{ollama_url.rstrip('/')}/api/chat",
                    json=payload, timeout=300
                )
                resp.raise_for_status()
                answer = resp.json().get('message', {}).get('content', '')
                st.session_state['chat_history'].append(
                    {'role': 'assistant', 'content': answer}
                )
                st.rerun()
            except Exception as e:
                st.error(f"Error al conectar con Ollama: {e}")

    # Botón para limpiar el historial
    if st.session_state.get('chat_history'):
        if st.button("🗑️ Limpiar conversación"):
            st.session_state['chat_history'] = []
            st.session_state.pop('prompt_sent', None)
            st.rerun()
