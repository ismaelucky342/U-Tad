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
    # Me conecto a la DB y tomo la colección con los datos.
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_collection("aec5_docs")
    
    # Modelo para embeddar la query.
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # Una query natural, como si fuera un usuario buscando algo.
    query = "álgebra lineal"
    
    # Convierto la query en embedding para buscar por similitud.
    query_embedding = model.encode(query)

    # Busco top-5 con cosine similarity. Esto demuestra la búsqueda semántica básica.
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=5
    )

    print(f"Query: \"{query}\"")
    print("Top 5 resultados:")
    for i, (doc, sim) in enumerate(zip(results['documents'][0], results['distances'][0])):
        print(f"{i+1}. {doc} (sim: {1-sim:.2f})")  # Aproximo cosine

if __name__ == "__main__":
    basic_search()