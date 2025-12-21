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
import subprocess

def run_script(script_name):
    try:
        result = subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), '..', 'implementacion', script_name)], 
                                capture_output=True, text=True, cwd=os.path.join(os.path.dirname(__file__), '..'))
        if result.returncode == 0:
            print(f"[OK] {script_name} ejecutado\n{result.stdout}")
            return True
        else:
            print(f"[KO] Error en {script_name}: {result.stderr}")
            return False
    except Exception as e:
        print(f"[KO] Error ejecutando {script_name}: {e}")
        return False

def run_tests():
    print("=== Ejecutando tests para AEC5 ===\n")

    scripts = [
        ("01_setup_chroma.py", "Setup Chroma"),
        ("02_embeddings.py", "Embeddings"),
        ("03_poblado_db.py", "Poblado DB"),
        ("04_busquedas_basicas.py", "Búsquedas Básicas"),
        ("05_filtrado_metadatos.py", "Filtrado Metadatos"),
        ("06_metricas_recall.py", "Métricas Recall"),
        ("07_tuning_hnsw.py", "Tuning HNSW"),
        ("08_cuantizacion_pq.py", "Cuantización PQ"),
        ("09_mmr_diversidad.py", "MMR Diversidad"),
        ("10_chunking_rag.py", "Chunking RAG")
    ]

    for script, desc in scripts:
        print(f"{desc}")
        if not run_script(script):
            print(f"Falló en {desc}\n")
        else:
            print()

    print("=== Tests finalizados ===")

if __name__ == "__main__":
    run_tests()