#!/usr/bin/env bash
set -euo pipefail

# Enunciado: crear estructura basica en HDFS para la piscina.
# Objetivo: practicar gestion de directorios en HDFS.

HDFS_BASE="/piscine_hadoop"

hdfs dfs -mkdir -p "$HDFS_BASE/data" "$HDFS_BASE/output" "$HDFS_BASE/logs"

echo "HDFS directories created under $HDFS_BASE"
hdfs dfs -ls "$HDFS_BASE"
