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

def evaluate_recall():
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_collection("aec5_docs")
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # Queries de prueba con ground truth
    queries = ["álgebra", "cálculo"]
    ground_truth = {
        "álgebra": ["doc_0", "doc_1"],
        "cálculo": ["doc_2"]
    }

    for query in queries:
        query_embedding = model.encode(query)
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=5
        )
        retrieved = results['ids'][0][:5]
        relevant = ground_truth[query]
        recall_5 = len(set(retrieved) & set(relevant)) / len(relevant)
        print(f"Recall@5 para '{query}': {recall_5:.2f}")

if __name__ == "__main__":
    evaluate_recall()