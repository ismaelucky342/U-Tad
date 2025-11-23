#====================================================================================================#
#                                                                                                    #
#                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        #
#      Competición - ABDB                                ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       #
#                                                        ██║   ██║█████╗██║   ███████║██║  ██║       #
#      created:        19/11/2025  -  05:00:00           ██║   ██║╚════╝██║   ██╔══██║██║  ██║       #
#      last change:    23/11/2025  -  11:34:43           ╚██████╔╝      ██║   ██║  ██║██████╔╝       #
#                                                         ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        #
#                                                                                                    #
#      Ismael Hernandez Clemente                         ismael.hernandez@live.u-tad.com             #
#                                                                                                    #
#      Github:                                           https://github.com/ismaelucky342            #
#                                                                                                    #
#====================================================================================================# 

import subprocess
import os

def print_title(title):
    print("\n" + "="*60)
    print(f"EJECUTANDO: {title}")
    print("="*60)

def print_desc(desc):
    print(f"-> {desc}")

def run_script(path):
    print_title(os.path.basename(path))
    print_desc(f"Ejecutando {path} ...")
    try:
        result = subprocess.run(["python3", path], capture_output=True, text=True, timeout=30)
        print("--- SALIDA STDOUT ---")
        print(result.stdout)
        print("--- SALIDA STDERR ---")
        print(result.stderr)
        if result.returncode == 0:
            print("[OK] Ejecución exitosa.")
        else:
            print(f"[ERROR] Código de salida: {result.returncode}")
    except Exception as e:
        print(f"[ERROR] Excepción al ejecutar {path}: {e}")

print("=== AEC3 tester: validando scripts de implementacion ===")

scripts = [
    "01_vehiculos.py",
    "02_reservas.py",
    "03_sesiones.py",
    "04_metricas.py",
    "05_rankings.py",
    "06_mantenimiento.py",
    "07_notificaciones.py",
    "08_transacciones.py",
    "09_cache_policies.py"
]
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../implementacion/"))
for script in scripts:
    script_path = os.path.join(base_path, script)
    if os.path.exists(script_path):
        run_script(script_path)
    else:
        print(f"[ADVERTENCIA] No se encontró {script_path}")

print_title("Fin de la validación")
print_desc("Tester finalizado.")