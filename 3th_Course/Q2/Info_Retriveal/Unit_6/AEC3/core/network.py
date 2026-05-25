"""Network analysis module: graph construction and metrics."""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import networkx as nx
from utils.constants import MENTION_EXTRACT


class NetworkAnalyzer:
    """Builds and analyzes interaction graphs using NetworkX."""

    @staticmethod
    def build_interaction_graph(df: pd.DataFrame) -> nx.DiGraph:
        """
        Build directed graph of user mentions from tweets.
        
        Each tweet "author mentions @target" creates edge: author → target
        Edge weight = number of mentions (author → target)
        
        Args:
            df: DataFrame with 'user_name' and 'text' columns
            
        Returns:
            nx.DiGraph with nodes=users, edges=mentions
        """
        G = nx.DiGraph()

        for _, row in df.iterrows():
            author = str(row['user_name']).strip().lower()
            text = str(row['text']) if pd.notna(row['text']) else ''
            
            # Extract mentions (e.g., @bitcoin)
            mentioned = {m.lower() for m in MENTION_EXTRACT.findall(text)}

            # Add author node (even if isolated)
            if not G.has_node(author):
                G.add_node(author)

            # Add mention edges
            for target in mentioned:
                if target == author:
                    continue  # Ignore self-mentions
                
                if not G.has_node(target):
                    G.add_node(target)
                
                if G.has_edge(author, target):
                    G[author][target]['weight'] += 1
                else:
                    G.add_edge(author, target, weight=1)

        print(f"[NetworkAnalyzer] Graph built: {G.number_of_nodes():,} nodes, {G.number_of_edges():,} edges")
        return G

    @staticmethod
    def analyze_network(G: nx.DiGraph) -> dict:
        """
        Calculate network metrics and detect communities.
        
        Metrics:
        - in_degree_centrality: importance (who mentions you)
        - out_degree_centrality: activity (who you mention)
        - betweenness_centrality: bridge nodes between communities
        - pagerank: propagated influence
        - Louvain community detection
        
        Args:
            G: Directed graph from build_interaction_graph()
            
        Returns:
            Dict with: in_degree, out_degree, betweenness, pagerank, 
                       communities, top_nodes, n_communities
        """
        if G.number_of_nodes() == 0:
            raise ValueError("Empty graph – nothing to analyze.")

        # --- Centrality metrics ---
        in_deg = nx.in_degree_centrality(G)
        out_deg = nx.out_degree_centrality(G)
        G_und = G.to_undirected()
        between = nx.betweenness_centrality(G_und, normalized=True)
        pr = nx.pagerank(G, alpha=0.85, max_iter=200)

        # --- Community detection (Louvain) ---
        try:
            from community import best_partition
            partition = best_partition(G_und)
            n_communities = len(set(partition.values()))
        except ImportError:
            # Fallback to greedy modularity
            communities_gen = nx.algorithms.community.greedy_modularity_communities(G_und)
            partition = {}
            for cid, members in enumerate(communities_gen):
                for node in members:
                    partition[node] = cid
            n_communities = len(set(partition.values()))

        # --- Top-3 nodes per metric ---
        def _top3(metric_dict):
            return sorted(metric_dict.items(), key=lambda x: x[1], reverse=True)[:3]

        top_nodes = {
            'in_degree': _top3(in_deg),
            'out_degree': _top3(out_deg),
            'betweenness': _top3(between),
            'pagerank': _top3(pr),
        }

        # --- Print statistics ---
        print("\n" + "=" * 55)
        print("  NETWORK ANALYSIS REPORT")
        print("=" * 55)
        print(f"  Nodes: {G.number_of_nodes():>10,}")
        print(f"  Edges: {G.number_of_edges():>10,}")
        print(f"  Communities: {n_communities:>10,}")
        print(f"  Density: {nx.density(G):>10.6f}")
        try:
            avg_cc = nx.average_clustering(G_und)
            print(f"  Avg. Clustering: {avg_cc:>10.4f}")
        except:
            pass
        print("-" * 55)
        for metric, top in top_nodes.items():
            print(f"  Top-3 by {metric}:")
            for rank, (node, val) in enumerate(top, 1):
                print(f"      {rank}. {node:<25s} {val:.4f}")
        print("=" * 55 + "\n")

        # --- Visualization ---
        top100 = sorted(pr, key=pr.get, reverse=True)[:100]
        subG = G.to_undirected().subgraph(top100).copy()

        node_colors = [partition.get(n, 0) for n in subG.nodes()]
        node_sizes = [3000 * pr.get(n, 0) + 20 for n in subG.nodes()]

        fig, axes = plt.subplots(1, 2, figsize=(18, 8))

        # Subplot 1: Interaction graph
        ax1 = axes[0]
        pos = nx.spring_layout(subG, seed=42, k=0.5)
        nx.draw_networkx(
            subG, pos=pos, ax=ax1,
            node_color=node_colors, node_size=node_sizes,
            cmap=cm.tab20, font_size=6, font_color='black',
            edge_color='#aaaaaa', alpha=0.85,
            with_labels=len(subG.nodes()) <= 40,
            arrows=False,
        )
        ax1.set_title("Interaction Graph – Top 100 nodes by PageRank\n(color = community)", fontsize=11)
        ax1.axis('off')

        # Subplot 2: In-degree distribution
        ax2 = axes[1]
        in_degrees = [d for _, d in G.in_degree()]
        ax2.hist(in_degrees, bins=40, color='steelblue', edgecolor='white', log=True)
        ax2.set_xlabel('In-Degree (mentions received)')
        ax2.set_ylabel('Number of nodes (log scale)')
        ax2.set_title('In-Degree Distribution (power-law typical of social networks)', fontsize=11)

        plt.suptitle('Network Analysis – Bitcoin Tweets Interaction Graph', fontsize=13, fontweight='bold')
        plt.tight_layout()
        plt.savefig('outputs/network_graph.png', dpi=120, bbox_inches='tight')
        plt.show()

        return {
            'in_degree': in_deg,
            'out_degree': out_deg,
            'betweenness': between,
            'pagerank': pr,
            'communities': partition,
            'top_nodes': top_nodes,
            'n_communities': n_communities,
        }

    @staticmethod
    def generate_prompt_from_network(G: nx.DiGraph, hashtag_freq: dict = None) -> str:
        """
        Generate structured prompt for LLM from network insights.
        
        Extracts:
        - Top-3 users by PageRank and Betweenness
        - Most frequent hashtag
        - Number of communities
        
        Args:
            G: Directed graph from build_interaction_graph()
            hashtag_freq: Dict of hashtag → frequency (optional)
            
        Returns:
            Prompt string ready for LLM
        """
        if G.number_of_nodes() == 0:
            raise ValueError("Empty graph – run build_interaction_graph() first.")

        pr = nx.pagerank(G, alpha=0.85, max_iter=200)
        G_und = G.to_undirected()
        between = nx.betweenness_centrality(G_und, normalized=True)

        top3_pr = sorted(pr.items(), key=lambda x: x[1], reverse=True)[:3]
        top3_bt = sorted(between.items(), key=lambda x: x[1], reverse=True)[:3]

        # Community detection
        try:
            from community import best_partition
            partition = best_partition(G_und)
            n_communities = len(set(partition.values()))
        except ImportError:
            communities_gen = nx.algorithms.community.greedy_modularity_communities(G_und)
            n_communities = sum(1 for _ in communities_gen)

        # Most frequent hashtag
        top_hashtag = "bitcoin"  # Default
        if hashtag_freq and isinstance(hashtag_freq, dict):
            top_hashtag = max(hashtag_freq.items(), key=lambda x: x[1])[0]

        # Build prompt
        pr_lines = "\n".join(
            f"   {i+1}. @{node}  (PageRank={val:.4f})"
            for i, (node, val) in enumerate(top3_pr)
        )
        bt_lines = "\n".join(
            f"   {i+1}. @{node}  (Betweenness={val:.4f})"
            for i, (node, val) in enumerate(top3_bt)
        )

        prompt = f"""You are a social media analyst specializing in cryptocurrency communities.

I have analyzed a Twitter interaction network built from Bitcoin-related tweets.
Below are the key insights extracted from the graph analysis:

NETWORK STATS
-------------
- Total nodes (users): {G.number_of_nodes():,}
- Total edges (mention interactions): {G.number_of_edges():,}
- Detected communities (Louvain): {n_communities}
- Network density: {nx.density(G):.4f}

TOP-3 USERS BY PAGERANK (most influential – receiving high-quality mentions):
{pr_lines}

TOP-3 USERS BY BETWEENNESS CENTRALITY (key bridges between communities):
{bt_lines}

MOST FREQUENT HASHTAG: #{top_hashtag}

Based on these findings, please:
1. Explain what the network structure (density, communities) tells us about the Bitcoin Twitter community.
2. Speculate on why these specific users hold central positions – are they likely journalists, influencers, or automated accounts?
3. Discuss what the dominant hashtag (#{top_hashtag}) reveals about current community sentiment and engagement.
4. Suggest what marketing or research actions would be most effective given this network topology.

Provide a concise but insightful analysis (around 300-400 words)."""

        print("[NetworkAnalyzer] Prompt generated successfully")
        return prompt
