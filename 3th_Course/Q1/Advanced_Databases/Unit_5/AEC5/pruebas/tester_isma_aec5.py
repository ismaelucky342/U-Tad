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

#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'implementacion'))

from implementacion import (
    setup_chroma,
    embeddings,
    poblado_db,
    busquedas_basicas,
    filtrado_metadatos,
    metricas_recall,
    tuning_hnsw,
    cuantizacion_pq,
    mmr_diversidad,
    chunking_rag
)

def run_tests():
    print("=== Ejecutando tests para AEC5 ===\n")

    print("1. Setup Chroma")
    try:
        setup_chroma.setup_chroma()
        print("✓ Setup completado\n")
    except Exception as e:
        print(f"✗ Error en setup: {e}\n")

    print("2. Embeddings")
    try:
        model = embeddings.load_model()
        embeddings.generate_embedding(model, "Test chunk")
        print("✓ Embeddings generados\n")
    except Exception as e:
        print(f"✗ Error en embeddings: {e}\n")

    print("3. Poblado DB")
    try:
        poblado_db.populate_db()
        print("✓ DB poblada\n")
    except Exception as e:
        print(f"✗ Error en poblado: {e}\n")

    print("4. Búsquedas Básicas")
    try:
        busquedas_basicas.basic_search()
        print("✓ Búsquedas básicas completadas\n")
    except Exception as e:
        print(f"✗ Error en búsquedas: {e}\n")

    print("5. Filtrado Metadatos")
    try:
        filtrado_metadatos.filtered_search()
        print("✓ Filtrado completado\n")
    except Exception as e:
        print(f"✗ Error en filtrado: {e}\n")

    print("6. Métricas Recall")
    try:
        metricas_recall.evaluate_recall()
        print("✓ Recall evaluado\n")
    except Exception as e:
        print(f"✗ Error en recall: {e}\n")

    print("7. Tuning HNSW")
    try:
        tuning_hnsw.tune_hnsw()
        print("✓ Tuning completado\n")
    except Exception as e:
        print(f"✗ Error en tuning: {e}\n")

    print("8. Cuantización PQ")
    try:
        cuantizacion_pq.apply_pq()
        print("✓ PQ aplicado\n")
    except Exception as e:
        print(f"✗ Error en PQ: {e}\n")

    print("9. MMR Diversidad")
    try:
        mmr_diversidad.apply_mmr()
        print("✓ MMR aplicado\n")
    except Exception as e:
        print(f"✗ Error en MMR: {e}\n")

    print("10. Chunking RAG")
    try:
        chunking_rag.rag_chunking()
        print("✓ Chunking completado\n")
    except Exception as e:
        print(f"✗ Error en chunking: {e}\n")

    print("=== Tests finalizados ===")

if __name__ == "__main__":
    run_tests()