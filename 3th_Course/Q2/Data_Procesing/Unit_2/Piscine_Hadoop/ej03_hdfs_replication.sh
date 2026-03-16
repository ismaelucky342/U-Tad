#!/usr/bin/env bash
set -euo pipefail

# Enunciado: consultar y cambiar replicacion de un archivo.
# Objetivo: entender replicacion de HDFS y fsck.

HDFS_BASE="/piscine_hadoop"
LOCAL_DIR="${LOCAL_DIR:-$PWD/piscine_hadoop_local}"

mkdir -p "$LOCAL_DIR"

cat > "$LOCAL_DIR/datos_ciudades.csv" <<'EOF'
Madrid,2026-03-15,42
Valencia,2026-03-15,37
Sevilla,2026-03-15,29
EOF

hdfs dfs -mkdir -p "$HDFS_BASE/data"
hdfs dfs -put -f "$LOCAL_DIR/datos_ciudades.csv" "$HDFS_BASE/data/"

hdfs fsck "$HDFS_BASE/data/datos_ciudades.csv" -files -blocks -locations

hdfs dfs -setrep -w 2 "$HDFS_BASE/data/datos_ciudades.csv"

hdfs fsck "$HDFS_BASE/data/datos_ciudades.csv" -files -blocks -locations
