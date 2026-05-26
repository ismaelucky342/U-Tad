#====================================================================================================#
#                                    LLM INTEGRATION MODULE                                         #
#                          Métodos para integración con modelos LLM                                 #
#====================================================================================================#

import os
import torch
from typing import Optional, Dict, Any


class LLMIntegration:
    """Métodos especializados en integración con modelos de lenguaje."""
    
    @staticmethod
    def generate_prompt_from_network(G, analysis: Dict, hashtags_stats: Dict) -> str:
        """
        Genera un prompt contextualizado a partir del análisis de la red.
        
        El prompt incluye:
        - Estadísticas de la red
        - Nodos más influyentes
        - Hashtags principales
        - Comunidades detectadas
        
        Parámetros:
            G: Grafo NetworkX
            analysis: Resultado de analyze_network()
            hashtags_stats: Diccionario con 'overall' DataFrame de hashtags
        
        Retorna:
            str: Prompt formateado para el LLM
        """
        # Extraer top nodos
        top_nodes = [node for node, _ in analysis.get('top_degree_centrality', [])[:3]]
        
        # Hashtags principales
        top_hashtags = hashtags_stats['overall'].head(5)['hashtag'].tolist() \
                       if 'overall' in hashtags_stats else []
        
        # Info comunidades
        communities_info = analysis.get('communities', {})
        num_communities = communities_info.get('num_communities', 0)
        
        # Construir prompt
        prompt = f"""Based on the following social network analysis of Twitter data:

Network Metrics:
- Total nodes (users & hashtags): {analysis['global_stats']['num_nodes']}
- Total interactions (edges): {analysis['global_stats']['num_edges']}
- Network density: {analysis['global_stats']['density']:.4f}
- Number of communities detected: {num_communities}

Most Influential Nodes (by degree centrality):
1. {top_nodes[0] if len(top_nodes) > 0 else 'N/A'}
2. {top_nodes[1] if len(top_nodes) > 1 else 'N/A'}
3. {top_nodes[2] if len(top_nodes) > 2 else 'N/A'}

Top Hashtags:
{', '.join(f'#{tag}' for tag in top_hashtags) if top_hashtags else 'N/A'}

Analysis Task:
Please analyze these network statistics and explain:
1. What are the likely reasons behind the identified influential nodes/users?
2. What do the top hashtags and network communities suggest about the conversation themes?
3. What user behaviors or sentiment trends can you infer from the network structure?
4. Who are the key opinion leaders or bridges between communities based on centrality measures?

Provide a comprehensive, interpretive analysis."""
        
        return prompt
    
    @staticmethod
    def load_local_llm(model_name: str = "google/gemma-2b-it", use_gpu: bool = True):
        """
        Carga un modelo LLM local desde Hugging Face.
        
        Parámetros:
            model_name: Nombre del modelo en Hugging Face
            use_gpu: Si True, intenta usar CUDA
        
        Retorna:
            (tokenizer, model, device): Tokenizer, modelo, y device (cpu/cuda)
        
        Lanza:
            ImportError si las librerías no están disponibles
        """
        from transformers import AutoTokenizer, AutoModelForCausalLM
        
        device = "cuda" if use_gpu and torch.cuda.is_available() else "cpu"
        
        try:
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            model = AutoModelForCausalLM.from_pretrained(
                model_name,
                torch_dtype=torch.float16 if device == "cuda" else torch.float32,
                device_map="auto" if device == "cuda" else None
            )
            
            if device == "cpu":
                model = model.to(device)
            
            return tokenizer, model, device
        
        except Exception as e:
            raise ImportError(f"Error cargando modelo {model_name}: {e}")
    
    @staticmethod
    def generate_llm_response(tokenizer, model, prompt: str, device: str, 
                            max_tokens: int = 512, temperature: float = 0.7) -> str:
        """
        Genera una respuesta del modelo LLM.
        
        Parámetros:
            tokenizer: Tokenizer del modelo
            model: Modelo LLM
            prompt: Texto de entrada
            device: Device ('cpu' o 'cuda')
            max_tokens: Longitud máxima de la respuesta
            temperature: Creatividad (0.0-1.0)
        
        Retorna:
            str: Respuesta del modelo
        """
        inputs = tokenizer(prompt, return_tensors="pt").to(device)
        
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=max_tokens,
                temperature=temperature,
                top_p=0.95,
                do_sample=True,
                pad_token_id=tokenizer.eos_token_id
            )
        
        response_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        response = response_text[len(prompt):].strip()
        
        return response
    
    @staticmethod
    def chat_google_ai(prompt: str, max_tokens: int = 512) -> str:
        """
        Usa Google Generative AI como fallback cuando no hay GPU.
        
        Requiere GOOGLE_API_KEY en variables de entorno.
        
        Parámetros:
            prompt: Texto a procesar
            max_tokens: Longitud máxima de respuesta
        
        Retorna:
            str: Respuesta del modelo Google
        """
        try:
            import google.generativeai as genai
            
            api_key = os.environ.get("GOOGLE_API_KEY")
            if not api_key:
                return "[Error: No GOOGLE_API_KEY configurada en .env]"
            
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-pro')
            
            response = model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    max_output_tokens=max_tokens,
                    temperature=0.7
                )
            )
            
            return response.text
        
        except ImportError:
            return "[Error: google-generativeai no instalado]"
        except Exception as e:
            return f"[Error: {str(e)}]"
