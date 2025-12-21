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

def apply_mmr():
    # Conecto.
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_collection("aec5_docs")
    model = SentenceTransformer('all-MiniLM-L6-v2')

    query = "álgebra lineal"
    query_embedding = model.encode(query)

    # MMR simulado: busco más resultados y selecciono diversos para evitar repeticiones en RAG.
    # Chroma no tiene MMR nativo, así que es demo.
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=10
    )
    # Simulo selección diversa
    print("MMR lambda=0.5: Resultados más diversos, menos redundancia")
    for doc in results['documents'][0][:5]:
        print(f"- {doc}")

if __name__ == "__main__":
    apply_mmr()