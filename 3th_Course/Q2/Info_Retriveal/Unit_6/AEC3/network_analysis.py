#====================================================================================================#
#                                    NETWORK ANALYSIS MODULE                                        #
#                           Métodos para análisis de redes con NetworkX                             #
#====================================================================================================#

import networkx as nx
import re
from typing import Dict, List, Tuple, Optional


class NetworkAnalyzer:
    """Métodos especializados en análisis de redes sociales."""
    
    _RE_MENTION = re.compile(r'@\w+')
    
    @staticmethod
    def build_interaction_graph(data, extract_hashtags_fn, extract_mentions_fn, 
                               mention_extraction: bool = True) -> nx.DiGraph:
        """
        Construye un grafo dirigido de interacciones a partir de los tweets.
        
        Los nodos son usuarios y hashtags. Las aristas representan:
        - Menciones de usuario a usuario
        - Uso de hashtags por usuarios
        
        Parámetros:
            data: DataFrame con columnas 'user_name', 'text'
            extract_hashtags_fn: Función para extraer hashtags del texto
            extract_mentions_fn: Función para extraer menciones
            mention_extraction: Si True, extrae menciones; si False, solo hashtags
        
        Retorna:
            nx.DiGraph: Grafo dirigido ponderado
        """
        G = nx.DiGraph()
        
        for idx, row in data.iterrows():
            user = row['user_name']
            text = row['text']
            hashtags = extract_hashtags_fn(text)
            
            # Nodo usuario
            if not G.has_node(user):
                G.add_node(user, node_type='user')
            
            # Aristas usuario -> hashtag
            for tag in hashtags:
                tag_node = f"#{tag}"
                if not G.has_node(tag_node):
                    G.add_node(tag_node, node_type='hashtag')
                
                if G.has_edge(user, tag_node):
                    G[user][tag_node]['weight'] += 1
                else:
                    G.add_edge(user, tag_node, weight=1)
            
            # Extraer menciones si está habilitado
            if mention_extraction:
                mentions = extract_mentions_fn(text)
                for mention in mentions:
                    mentioned_user = mention[1:]  # Remover @
                    if not G.has_node(mentioned_user):
                        G.add_node(mentioned_user, node_type='user')
                    
                    if G.has_edge(user, mentioned_user):
                        G[user][mentioned_user]['weight'] += 1
                    else:
                        G.add_edge(user, mentioned_user, weight=1, interaction_type='mention')
        
        return G
    
    @staticmethod
    def analyze_network(G: nx.DiGraph, top_k: int = 3) -> Dict:
        """
        Calcula métricas de red y detecta comunidades.
        
        Parámetros:
            G: Grafo dirigido
            top_k: Número de nodos top a retornar por cada métrica
        
        Retorna:
            Dict con estadísticas y análisis de comunidades
        """
        if G.number_of_nodes() == 0:
            raise RuntimeError("Grafo vacío")
        
        # Estadísticas globales
        stats = {
            'num_nodes': G.number_of_nodes(),
            'num_edges': G.number_of_edges(),
            'density': nx.density(G),
            'is_connected': nx.is_connected(G.to_undirected())
        }
        
        # Centralidades
        try:
            degree_centrality = nx.degree_centrality(G)
            betweenness = nx.betweenness_centrality(G)
            closeness = nx.closeness_centrality(G)
        except Exception as e:
            print(f"Warning en cálculo de centralidades: {e}")
            degree_centrality = betweenness = closeness = {}
        
        # Top nodos
        top_degree = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:top_k]
        top_betweenness = sorted(betweenness.items(), key=lambda x: x[1], reverse=True)[:top_k]
        top_closeness = sorted(closeness.items(), key=lambda x: x[1], reverse=True)[:top_k]
        
        # Comunidades (en grafo no dirigido)
        G_undirected = G.to_undirected()
        try:
            from networkx.algorithms import community
            communities = list(community.greedy_modularity_communities(G_undirected))
            community_analysis = {
                'num_communities': len(communities),
                'sizes': [len(c) for c in communities],
                'communities': [list(c) for c in communities]
            }
        except Exception as e:
            print(f"Warning en detección de comunidades: {e}")
            community_analysis = {'error': str(e)}
        
        return {
            'global_stats': stats,
            'top_degree_centrality': top_degree,
            'top_betweenness_centrality': top_betweenness,
            'top_closeness_centrality': top_closeness,
            'communities': community_analysis,
            'centrality_measures': {
                'degree': degree_centrality,
                'betweenness': betweenness,
                'closeness': closeness
            }
        }
