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

import requests
import json
import networkx as nx

def generate_prompt_from_network(G: nx.DiGraph, metrics: dict, top_hashtag: str = "N/D") -> str:
    if metrics is None:
        return "[Error: metricas no proveidas]"
    
    top3_in       = metrics.get('top3_in_degree', [])
    top3_pr       = metrics.get('top3_pagerank',  [])
    n_nodes       = metrics.get('n_nodes',        G.number_of_nodes())
    n_edges       = metrics.get('n_edges',        G.number_of_edges())
    density       = metrics.get('density',        nx.density(G))
    n_communities = metrics.get('n_communities',  "N/D")

    top3_in_str = ", ".join([f"@{n} ({v:.4f})" for n, v in top3_in]) or "N/D"
    top3_pr_str = ", ".join([f"@{n} ({v:.4f})" for n, v in top3_pr]) or "N/D"

    prompt = f"""Eres un experto en analisis de redes sociales y comportamiento en Twitter/X.
A continuacion te proporciono los resultados de un analisis de red de menciones.

=== DATOS DE LA RED ===
- Total de nodos (usuarios): {n_nodes}
- Total de aristas (menciones): {n_edges}
- Densidad de la red: {density:.4f}
- Comunidades detectadas: {n_communities}

=== NODOS MAS INFLUYENTES ===
Top 3 por in-degree centrality (usuarios mas mencionados):
{top3_in_str}

Top 3 por PageRank (usuarios con mayor influencia ponderada):
{top3_pr_str}

=== TENDENCIAS DE CONTENIDO ===
Hashtag mas frecuente en el dataset: #{top_hashtag}

=== PREGUNTA ===
Con base en estos datos:
1. Que patrones de comportamiento social observas en esta red de menciones?
2. Por que crees que estos usuarios tienen tanta centralidad?
3. Que nos dice la densidad de la red sobre la cohesion de esta comunidad en Twitter?
4. Como podrian las {n_communities} comunidades detectadas reflejar distintas posturas?

Por favor, da un analisis interpretativo detallado basado en estos insights."""

    print(f"[INFO] Prompt generado ({len(prompt.split())} palabras)")
    return prompt

def chat_local_llm(prompt: str = None, model: str = "gemma3", ollama_url: str = "http://localhost:11434", stream: bool = True) -> str:
    api_chat_url = f"{ollama_url.rstrip('/')}/api/chat"

    def _call_ollama(messages: list) -> str:
        payload = {"model": model, "messages": messages, "stream": stream}
        try:
            resp = requests.post(api_chat_url, json=payload, timeout=300, stream=stream)
            resp.raise_for_status()
        except Exception as e:
            raise RuntimeError(f"Error al conectar con Ollama: {e}")

        full_response = ""
        if stream:
            print(f"\n[Modelo {model}]: ", end="", flush=True)
            for line in resp.iter_lines():
                if line:
                    try:
                        chunk = json.loads(line.decode('utf-8'))
                        token = chunk.get('message', {}).get('content', '')
                        print(token, end="", flush=True)
                        full_response += token
                        if chunk.get('done', False):
                            break
                    except json.JSONDecodeError:
                        continue
            print()
        else:
            data = resp.json()
            full_response = data.get('message', {}).get('content', '')
            print(f"\n[Modelo {model}]: {full_response}")
        return full_response

    conversation = []
    last_response = ""

    if prompt:
        print("\n[INFO] Enviando analisis de red al LLM...")
        conversation.append({"role": "user", "content": prompt})
        last_response = _call_ollama(conversation)
        conversation.append({"role": "assistant", "content": last_response})

    print("\n[INFO] Chat interactivo iniciado (escribe 'salir' para terminar)")
    while True:
        try:
            user_input = input("\n[Tu]: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n[INFO] Chat terminado.")
            break

        if user_input.lower() in ('salir', 'exit', 'quit', 'q', ''):
            print("[INFO] Chat terminado.")
            break

        conversation.append({"role": "user", "content": user_input})
        last_response = _call_ollama(conversation)
        conversation.append({"role": "assistant", "content": last_response})

    return last_response