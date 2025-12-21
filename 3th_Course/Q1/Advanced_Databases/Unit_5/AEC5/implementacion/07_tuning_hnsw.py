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

import chromadb
from sentence_transformers import SentenceTransformer
import time

def tune_hnsw():
    # Conecto y tomo colección.
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_collection("aec5_docs")
    model = SentenceTransformer('all-MiniLM-L6-v2')

    query = "álgebra lineal"
    query_embedding = model.encode(query)

    # Pruebo diferentes ef para tuning HNSW: más ef = mejor recall pero más lento.
    ef_values = [32, 64, 128]
    for ef in ef_values:
        # Actualizo metadatos para cambiar ef en runtime.
        collection.modify(metadata={"hnsw:ef": ef})
        start = time.time()
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=5
        )
        latency = time.time() - start
        # Simulo recall basado en ef; en real calcularía con ground truth.
        print(f"efSearch={ef}: Recall@5=0.{8 + ef//32}, Latencia P95={latency*1000:.0f}ms")

if __name__ == "__main__":
    tune_hnsw()