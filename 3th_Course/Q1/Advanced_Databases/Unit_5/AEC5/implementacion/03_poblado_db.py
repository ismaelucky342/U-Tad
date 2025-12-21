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
    # Me conecto a la DB persistente y agarro la colección que creé antes.
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_collection("aec5_docs")
    
    # Cargo el modelo otra vez para generar embeddings de los chunks.
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # Simulo chunks de mis apuntes universitarios: álgebra, cálculo, bases de datos, etc.
    # En la vida real, esto vendría de chunking PDFs o MDs con overlap.
    documents = [
        "Matrices y determinantes en álgebra lineal",
        "Espacios vectoriales y transformaciones",
        "Cálculo diferencial e integral",
        "Bases de datos relacionales y NoSQL"
    ]
    
    # Metadatos para filtrar: asignatura, tipo de archivo, fecha. Esto permite búsquedas híbridas.
    metadatas = [
        {"asignatura": "Algebra", "tipo": "PDF", "fecha": "2023-09-01"},
        {"asignatura": "Algebra", "tipo": "MD", "fecha": "2023-09-02"},
        {"asignatura": "Calculus", "tipo": "PDF", "fecha": "2023-09-03"},
        {"asignatura": "Databases", "tipo": "MD", "fecha": "2023-09-04"}
    ]
    
    # IDs simples para cada doc.
    ids = [f"doc_{i}" for i in range(len(documents))]

    # Genero embeddings para cada chunk. Aquí es donde el texto se vuelve vector.
    embeddings = [model.encode(doc) for doc in documents]

    # Meto todo en la colección: docs, embeddings, metadatos, ids. Chroma se encarga del indexado HNSW.
    collection.add(
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas,
        ids=ids
    )
    
    print(f"Documentos añadidos: {len(documents)} chunks")
    print("Metadatos: {'asignatura': 'Algebra', 'tipo': 'PDF', 'fecha': '2023-09-01'}")

if __name__ == "__main__":
    populate_db()