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

from sentence_transformers import SentenceTransformer

def load_model():
    # Cargo el modelo 'all-MiniLM-L6-v2' porque es rápido y bueno para textos en español/inglés, como vimos en el temario.
    # Elegí este por su dimensionalidad baja (384) que no come mucha RAM.
    model = SentenceTransformer('all-MiniLM-L6-v2')
    print("Modelo cargado: sentence-transformers/all-MiniLM-L6-v2")
    return model

def generate_embedding(model, text):
    # Aquí convierto el texto en un vector denso. Es la magia de los embeddings: capturar significado.
    embedding = model.encode(text)
    print(f"Embedding generado para chunk 1: {embedding[:5]}... ({len(embedding)} dims)")
    return embedding

if __name__ == "__main__":
    model = load_model()
    sample_text = "Conceptos básicos de álgebra lineal"
    generate_embedding(model, sample_text)