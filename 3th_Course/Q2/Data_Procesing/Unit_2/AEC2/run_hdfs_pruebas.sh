#====================================================================================================#
#                                                                                                    #
#                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        #
#      AEC2 - PRDT                                       ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       #
#                                                        ██║   ██║█████╗██║   ███████║██║  ██║       #
#      created:        19/03/2026  -  21:45:15           ██║   ██║╚════╝██║   ██╔══██║██║  ██║       #
#      last change:    22/03/2026  -  00:55:42           ╚██████╔╝      ██║   ██║  ██║██████╔╝       #
#                                                         ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        #
#                                                                                                    #
#      Ismael Hernandez Clemente                         ismael.hernandez@live.u-tad.com             #
#                                                                                                    #
#      Github:                                           https://github.com/ismaelucky342            #
#                                                                                                    #
#====================================================================================================#

#!/usr/bin/env bash

set -u
set -o pipefail

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DATA_DIR="$BASE_DIR/datos"
EVID_DIR="$BASE_DIR/evidencias"
LOG_FILE="$EVID_DIR/hdfs_sesion.log"
HDFS_BLOCK_FILE="$BASE_DIR/bloques/01_hdfs.txt"
MAPREDUCE_BLOCK_FILE="$BASE_DIR/bloques/02_mapreduce.txt"
CAP_BLOCK_FILE="$BASE_DIR/bloques/03_cap.txt"

mkdir -p "$DATA_DIR" "$EVID_DIR"

pause_shot() {
  read -r -p ">> Captura pantalla ahora y pulsa Enter para continuar..." _
}

run_cmd() {
  echo -e "\n$ $*" | tee -a "$LOG_FILE"
  "$@" 2>&1 | tee -a "$LOG_FILE"
}

run_hdfs() {
  if [[ ! -f "$HDFS_BLOCK_FILE" ]]; then
    echo "No se encuentra el archivo de comandos: $HDFS_BLOCK_FILE" | tee -a "$LOG_FILE"
    return 1
  fi

  echo "Iniciando practica HDFS..." | tee -a "$LOG_FILE"

  while IFS= read -r line || [[ -n "$line" ]]; do
    case "$line" in
      "" ) continue ;;
      \#* ) continue ;;
      PAUSE ) pause_shot ;;
      * ) run_cmd bash -c "$line" ;;
    esac
  done < "$HDFS_BLOCK_FILE"

  echo "Fin de la practica HDFS. Log guardado en: $LOG_FILE" | tee -a "$LOG_FILE"
}

show_block() {
  local file="$1"
  echo
  echo "---"
  cat "$file"
  echo "---"
  echo
}

run_all() {
  show_block "$HDFS_BLOCK_FILE"
  pause_shot
  run_hdfs
  show_block "$MAPREDUCE_BLOCK_FILE"
  pause_shot
  show_block "$CAP_BLOCK_FILE"
}

while true; do
  echo ""
  echo "==============================="
  echo "  AEC2 - Procesamiento Datos"
  echo "==============================="
  echo "1) Ejecutar bloque HDFS (con pausas para capturas)"
  echo "2) Ver bloque MapReduce"
  echo "3) Ver bloque CAP"
  echo "4) Ejecutar todo (bloques + HDFS)"
  echo "0) Salir"
  echo ""
  read -r -p "Selecciona una opcion: " opt

  case "$opt" in
    1) run_hdfs ;;
    2) show_block "$MAPREDUCE_BLOCK_FILE" ;;
    3) show_block "$CAP_BLOCK_FILE" ;;
    4) run_all ;;
    0) echo "Hasta luego"; exit 0 ;;
    *) echo "Opcion no valida" ;;
  esac
done
