#====================================================================================================#
#                                    UTILITIES MODULE                                               #
#                          Funciones auxiliares de exportación y validación                          #
#====================================================================================================#

import json
import networkx as nx
from pathlib import Path
from typing import Dict, Optional


class ExportUtils:
    """Utilidades para exportación de resultados."""
    
    @staticmethod
    def export_network_analysis(output_dir: str, G: nx.DiGraph, analysis: Dict, 
                               prompt: str = "", llm_response: str = "") -> None:
        """
        Exporta todos los resultados del análisis de red.
        
        Parámetros:
            output_dir: Directorio de destino
            G: Grafo NetworkX
            analysis: Resultado de analyze_network()
            prompt: Prompt enviado al LLM (para auditoría)
            llm_response: Respuesta del LLM
        """
        out = Path(output_dir)
        out.mkdir(parents=True, exist_ok=True)
        
        # 1. Estadísticas en JSON
        stats_export = {
            'global_stats': analysis['global_stats'],
            'top_degree_centrality': [
                (node, float(val)) for node, val in analysis['top_degree_centrality']
            ],
            'top_betweenness': [
                (node, float(val)) for node, val in analysis['top_betweenness_centrality']
            ],
            'top_closeness': [
                (node, float(val)) for node, val in analysis['top_closeness_centrality']
            ],
        }
        (out / 'network_stats.json').write_text(
            json.dumps(stats_export, indent=2), 
            encoding='utf-8'
        )
        print(f"  Guardado: network_stats.json")
        
        # 2. Comunidades en JSON
        communities_export = analysis['communities'].copy()
        if 'communities' in communities_export:
            communities_export['communities'] = [
                list(c) for c in communities_export['communities']
            ]
        (out / 'communities.json').write_text(
            json.dumps(communities_export, indent=2, default=str), 
            encoding='utf-8'
        )
        print(f"  Guardado: communities.json")
        
        # 3. Prompt para referencia
        if prompt:
            (out / 'network_prompt.txt').write_text(prompt, encoding='utf-8')
            print(f"  Guardado: network_prompt.txt")
        
        # 4. Respuesta del LLM
        if llm_response:
            (out / 'llm_response.txt').write_text(llm_response, encoding='utf-8')
            print(f"  Guardado: llm_response.txt")
        
        # 5. Grafo en formato GEXF (visualizable en Gephi)
        try:
            nx.write_gexf(G, out / 'network_graph.gexf')
            print(f"  Guardado: network_graph.gexf (importable en Gephi)")
        except Exception as e:
            print(f"  Warning: No se pudo exportar GEXF: {e}")
    
    @staticmethod
    def validate_data(data) -> bool:
        """
        Valida que el DataFrame tenga las columnas necesarias.
        
        Parámetros:
            data: DataFrame a validar
        
        Retorna:
            bool: True si es válido
        """
        required_columns = {'user_name', 'text'}
        available_columns = set(data.columns)
        
        if not required_columns.issubset(available_columns):
            missing = required_columns - available_columns
            raise ValueError(f"Columnas faltantes en el DataFrame: {missing}")
        
        if len(data) == 0:
            raise ValueError("El DataFrame está vacío")
        
        return True


class ValidationUtils:
    """Utilidades para validación de datos."""
    
    @staticmethod
    def check_gpu_availability() -> bool:
        """Verifica disponibilidad de GPU."""
        return __import__('torch').cuda.is_available()
    
    @staticmethod
    def get_gpu_info() -> Optional[str]:
        """Retorna información de la GPU si está disponible."""
        try:
            import torch
            if torch.cuda.is_available():
                return {
                    'device': torch.cuda.get_device_name(0),
                    'version': torch.version.cuda,
                    'memory_gb': torch.cuda.get_device_properties(0).total_memory / 1e9
                }
        except:
            pass
        return None
    
    @staticmethod
    def check_credentials() -> Dict[str, bool]:
        """Verifica que las credenciales estén configuradas."""
        import os
        from dotenv import load_dotenv
        
        load_dotenv()
        
        return {
            'RAPIDAPI_KEY': bool(os.getenv('RAPIDAPI_KEY')),
            'GOOGLE_API_KEY': bool(os.getenv('GOOGLE_API_KEY'))
        }
