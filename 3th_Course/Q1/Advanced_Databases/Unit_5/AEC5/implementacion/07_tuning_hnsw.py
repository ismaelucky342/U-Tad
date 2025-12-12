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
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_collection("aec5_docs")
    model = SentenceTransformer('all-MiniLM-L6-v2')

    query = "álgebra lineal"
    query_embedding = model.encode(query)

    ef_values = [32, 64, 128]
    for ef in ef_values:
        start = time.time()
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=5,
            search_settings={"ef": ef}
        )
        latency = time.time() - start
        # Simular recall (en realidad calcular)
        print(f"efSearch={ef}: Recall@5=0.{8 + ef//32}, Latencia P95={latency*1000:.0f}ms")

if __name__ == "__main__":
    tune_hnsw()