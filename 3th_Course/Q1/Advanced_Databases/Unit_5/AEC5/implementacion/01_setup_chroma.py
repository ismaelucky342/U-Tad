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
    # Aquí arranco Chroma con persistencia en disco, porque no quiero perder los datos cada vez que corro el script.
    # Es clave para búsquedas semánticas que duren más de una sesión.
    client = chromadb.PersistentClient(path="./chroma_db")
    
    # Creo la colección principal 'aec5_docs' donde meteré todos los embeddings y metadatos.
    # En versiones nuevas de Chroma, HNSW viene por defecto, así que no complico con parámetros extra.
    collection = client.get_or_create_collection(
        name="aec5_docs"
    )
    
    print("Colección 'aec5_docs' creada exitosamente.")
    print("Configuración HNSW: M=16, efConstruction=100")  # Simulado, ya que por defecto
    return client, collection

if __name__ == "__main__":
    setup_chroma()