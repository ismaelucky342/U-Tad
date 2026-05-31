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

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pandas as pd
from src.nlp_core import extract_mentions

def build_interaction_graph(df: pd.DataFrame) -> nx.DiGraph:
    G = nx.DiGraph()
    tweet_counts = df['user_name'].value_counts().to_dict()

    for _, row in df.iterrows():
        source = str(row.get('user_name', '')).strip().lower()
        text   = str(row.get('text', ''))

        if not source or source == 'nan':
            continue

        if source not in G:
            G.add_node(source, tweet_count=tweet_counts.get(source, 0))

        mentions = extract_mentions(text)

        for target in mentions:
            if target == source:
                continue 

            if target not in G:
                G.add_node(target, tweet_count=tweet_counts.get(target, 0))

            if G.has_edge(source, target):
                G[source][target]['weight'] += 1
            else:
                G.add_edge(source, target, weight=1)

    print(f"[INFO] Grafo construido: {G.number_of_nodes()} nodos, {G.number_of_edges()} aristas")
    return G

def analyze_network(G: nx.DiGraph) -> dict:
    n_nodes = G.number_of_nodes()
    n_edges = G.number_of_edges()
    density = nx.density(G)
    n_components = nx.number_weakly_connected_components(G)

    in_degree_centrality  = nx.in_degree_centrality(G)
    betweenness           = nx.betweenness_centrality(G, weight='weight', normalized=True)
    pagerank              = nx.pagerank(G, weight='weight', max_iter=200)

    top3_in_degree   = sorted(in_degree_centrality.items(),  key=lambda x: x[1], reverse=True)[:3]
    top3_betweenness = sorted(betweenness.items(),           key=lambda x: x[1], reverse=True)[:3]
    top3_pagerank    = sorted(pagerank.items(),              key=lambda x: x[1], reverse=True)[:3]

    G_undirected = G.to_undirected(reciprocal=False)
    communities  = {}
    try:
        from community import best_partition
        partition = best_partition(G_undirected, weight='weight')
        n_communities = len(set(partition.values()))
        communities = partition
        print(f"[INFO] Louvain detecto {n_communities} comunidades")
    except ImportError:
        from networkx.algorithms.community import greedy_modularity_communities
        comms = list(greedy_modularity_communities(G_undirected, weight='weight'))
        partition = {}
        n_communities = len(comms)
        for idx, comm in enumerate(comms):
            for node in comm:
                partition[node] = idx
        communities = partition
        print(f"[INFO] Greedy modularity detecto {n_communities} comunidades")

    # Visualizacion
    MAX_NODES = 80
    if n_nodes > MAX_NODES:
        top_nodes = sorted(pagerank, key=pagerank.get, reverse=True)[:MAX_NODES]
        subG      = G.subgraph(top_nodes).copy()
        subpart   = {n: communities.get(n, 0) for n in top_nodes}
    else:
        subG    = G
        subpart = communities

    fig, axes = plt.subplots(1, 2, figsize=(18, 8))
    
    ax1 = axes[0]
    try:
        pos = nx.spring_layout(subG, seed=42, k=0.5)
    except Exception:
        pos = nx.random_layout(subG, seed=42)

    n_comms  = max(subpart.values()) + 1 if subpart else 1
    cmap     = cm.get_cmap('tab20', n_comms)
    colors   = [cmap(subpart.get(node, 0) % n_comms) for node in subG.nodes()]
    sizes    = [300 + pagerank.get(node, 0) * 15000 for node in subG.nodes()]
    weights  = [subG[u][v]['weight'] for u, v in subG.edges()]
    max_w    = max(weights) if weights else 1

    nx.draw_networkx_nodes(subG, pos, ax=ax1, node_color=colors, node_size=sizes, alpha=0.85)
    nx.draw_networkx_edges(subG, pos, ax=ax1, width=[0.5 + 2.5 * (w / max_w) for w in weights],
                           alpha=0.4, arrows=True, arrowstyle='->', arrowsize=10, edge_color='gray')
    top10_labels = {n: f"@{n}" for n in sorted(pagerank, key=pagerank.get, reverse=True)[:10] if n in subG.nodes()}
    nx.draw_networkx_labels(subG, pos, labels=top10_labels, ax=ax1, font_size=7, font_weight='bold')
    ax1.set_title("Red de menciones - Comunidades", fontsize=12)
    ax1.axis('off')

    ax2   = axes[1]
    degs  = [d for _, d in G.in_degree()]
    ax2.hist(degs, bins=min(50, max(degs) + 1) if degs else 10, color='steelblue', edgecolor='white', alpha=0.85)
    ax2.set_xlabel("In-degree (veces mencionado)", fontsize=11)
    ax2.set_ylabel("Numero de nodos", fontsize=11)
    ax2.set_title("Distribucion de in-degree", fontsize=12)
    ax2.set_yscale('log')

    plt.suptitle("Analisis de red de interacciones en Twitter", fontsize=14, fontweight='bold', y=1.01)
    plt.tight_layout()
    plt.savefig('network_analysis.png', dpi=150, bbox_inches='tight')
    plt.show()

    return {
        'n_nodes': n_nodes, 'n_edges': n_edges, 'density': density,
        'n_components': n_components, 'n_communities': n_communities,
        'communities': communities, 'in_degree_centrality': in_degree_centrality,
        'betweenness': betweenness, 'pagerank': pagerank,
        'top3_in_degree': top3_in_degree, 'top3_betweenness': top3_betweenness,
        'top3_pagerank': top3_pagerank,
    }