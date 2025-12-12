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

def setup_chroma():
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_or_create_collection(
        name="aec5_docs",
        metadata={"hnsw:M": 16, "hnsw:efConstruction": 100}
    )
    print("Colección 'aec5_docs' creada exitosamente.")
    print("Configuración HNSW: M=16, efConstruction=100")
    return client, collection

if __name__ == "__main__":
    setup_chroma()