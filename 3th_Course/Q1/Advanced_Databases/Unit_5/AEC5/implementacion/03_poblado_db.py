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
import os

def populate_db():
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_collection("aec5_docs")
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # Datos de ejemplo (simulando chunks de documentos)
    documents = [
        "Matrices y determinantes en álgebra lineal",
        "Espacios vectoriales y transformaciones",
        "Cálculo diferencial e integral",
        "Bases de datos relacionales y NoSQL"
    ]
    metadatas = [
        {"asignatura": "Algebra", "tipo": "PDF", "fecha": "2023-09-01"},
        {"asignatura": "Algebra", "tipo": "MD", "fecha": "2023-09-02"},
        {"asignatura": "Calculus", "tipo": "PDF", "fecha": "2023-09-03"},
        {"asignatura": "Databases", "tipo": "MD", "fecha": "2023-09-04"}
    ]
    ids = [f"doc_{i}" for i in range(len(documents))]

    embeddings = [model.encode(doc) for doc in documents]

    collection.add(
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas,
        ids=ids
    )
    print(f"Documentos añadidos: {len(documents)} chunks")
    print("Metadatos ejemplo:", metadatas[0])

if __name__ == "__main__":
    populate_db()