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

def basic_search():
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_collection("aec5_docs")
    model = SentenceTransformer('all-MiniLM-L6-v2')

    query = "álgebra lineal"
    query_embedding = model.encode(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=5
    )

    print(f"Query: \"{query}\"")
    print("Top 5 resultados:")
    for i, (doc, sim) in enumerate(zip(results['documents'][0], results['distances'][0])):
        print(f"{i+1}. {doc} (sim: {1-sim:.2f})")  # Cosine similarity approx

if __name__ == "__main__":
    basic_search()