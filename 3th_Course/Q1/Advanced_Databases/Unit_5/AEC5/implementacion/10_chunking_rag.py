#====================================================================================================#
#                                                                                                    #
#                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        #
#      AEC5 - ABDB                                       ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       #
#                                                        ██║   ██║█████╗██║   ███████║██║  ██║       #
#      created:        12/12/2025  -  18:00:34           ██║   ██║╚════╝██║   ██╔══██║██║  ██║       #
#      last change:    20/12/2025  -  13:21:12           ╚██████╔╝      ██║   ██║  ██║██████╔╝       #
#                                                         ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        #
#                                                                                                    #
#      Ismael Hernandez Clemente                         ismael.hernandez@live.u-tad.com             #
#                                                                                                    #
#      Github:                                           https://github.com/ismaelucky342            #
#                                                                                                    #
#====================================================================================================# 

from sentence_transformers import SentenceTransformer
import re

def chunk_text(text, chunk_size=512, overlap=50):
    # Función para dividir texto en chunks con overlap para preservar contexto.
    # Evita perder ideas entre chunks.
    words = re.findall(r'\b\w+\b', text)
    chunks = []
    start = 0
    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunk = ' '.join(words[start:end])
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks

def rag_chunking():
    # Demo de chunking para RAG: divido texto en pedazos y embeddo cada uno.
    # Overlap evita cortes bruscos.
    model = SentenceTransformer('all-MiniLM-L6-v2')
    sample_text = "Álgebra lineal es una rama de las matemáticas que estudia conceptos tales como vectores, matrices, espacios vectoriales y transformaciones lineales."
    chunks = chunk_text(sample_text)
    print(f"Chunks generados: {len(chunks)} con overlap=50")
    for i, chunk in enumerate(chunks):
        embedding = model.encode(chunk)
        print(f"Chunk {i+1}: {chunk[:50]}... (embedding len: {len(embedding)})")
    print("Riesgo evitado: Contexto preservado en transiciones")

if __name__ == "__main__":
    rag_chunking()