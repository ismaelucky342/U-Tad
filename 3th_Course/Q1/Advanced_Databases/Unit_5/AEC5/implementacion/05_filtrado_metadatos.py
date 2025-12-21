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

def filtered_search():
    # Conecto y tomo la colección.
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_collection("aec5_docs")
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # Query sobre cálculo, pero filtro por asignatura para acotar.
    query = "cálculo"
    query_embedding = model.encode(query)

    # Búsqueda híbrida: similitud + filtro por metadatos. Esto reduce ruido.
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=5,
        where={"asignatura": "Calculus"}
    )

    print(f"Query filtrada: \"{query}\" where asignatura=\"Calculus\"")
    print(f"Resultados: {len(results['documents'][0])} docs relevantes")
    for doc in results['documents'][0]:
        print(f"- {doc}")

if __name__ == "__main__":
    filtered_search()