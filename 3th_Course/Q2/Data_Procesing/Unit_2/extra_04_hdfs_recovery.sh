#!/usr/bin/env bash
set -euo pipefail

# Enunciado: simular replicacion y recuperacion en HDFS.

HDFS_BASE="/piscine_hadoop"
LOCAL_DIR="${LOCAL_DIR:-$PWD/piscine_hadoop_local}"
EX_DIR="$LOCAL_DIR/extra_04"

mkdir -p "$EX_DIR"

cat > "$EX_DIR/recovery.txt" <<'EOF'
linea uno
linea dos
linea tres
EOF

hdfs dfs -mkdir -p "$HDFS_BASE/data"
hdfs dfs -put -f "$EX_DIR/recovery.txt" "$HDFS_BASE/data/"

hdfs dfs -setrep -w 1 "$HDFS_BASE/data/recovery.txt"
hdfs fsck "$HDFS_BASE/data/recovery.txt" -files -blocks -locations

hdfs dfs -setrep -w 2 "$HDFS_BASE/data/recovery.txt"
hdfs fsck "$HDFS_BASE/data/recovery.txt" -files -blocks -locations
