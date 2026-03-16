#!/usr/bin/env bash
set -euo pipefail

# Enunciado: configurar salida clave-valor con separador tab.
# Objetivo: inspeccionar outputs en HDFS.

HDFS_BASE="/piscine_hadoop"
LOCAL_DIR="${LOCAL_DIR:-$PWD/piscine_hadoop_local}"
OUT_DIR="$LOCAL_DIR/output_sep"

mkdir -p "$OUT_DIR"

cat > "$OUT_DIR/input.txt" <<'EOF'
alpha beta
beta gamma
alpha
EOF

cat > "$OUT_DIR/mapper.py" <<'EOF'
#!/usr/bin/env python3
import sys
for line in sys.stdin:
    for word in line.strip().split():
        if word:
            print(f"{word}\t1")
EOF

cat > "$OUT_DIR/reducer.py" <<'EOF'
#!/usr/bin/env python3
import sys
current = None
count = 0
for line in sys.stdin:
    word, value = line.strip().split("\t", 1)
    if current is None:
        current = word
    if word != current:
        print(f"{current}\t{count}")
        current = word
        count = 0
    count += int(value)
if current is not None:
    print(f"{current}\t{count}")
EOF

chmod +x "$OUT_DIR/mapper.py" "$OUT_DIR/reducer.py"

hdfs dfs -mkdir -p "$HDFS_BASE/data" "$HDFS_BASE/output"
hdfs dfs -put -f "$OUT_DIR/input.txt" "$HDFS_BASE/data/"

if [[ -z "${HADOOP_HOME:-}" ]]; then
    echo "HADOOP_HOME is not set. Please export HADOOP_HOME and re-run."
    exit 1
fi

STREAMING_JAR=$(ls "$HADOOP_HOME"/share/hadoop/tools/lib/hadoop-streaming*.jar 2>/dev/null | head -n 1)
if [[ -z "$STREAMING_JAR" ]]; then
    echo "Hadoop streaming jar not found under HADOOP_HOME."
    exit 1
fi

hdfs dfs -rm -r -f "$HDFS_BASE/output/ej8"

hadoop jar "$STREAMING_JAR" \
  -D mapreduce.output.textoutputformat.separator=$'\t' \
  -input "$HDFS_BASE/data/input.txt" \
  -output "$HDFS_BASE/output/ej8" \
  -mapper "$OUT_DIR/mapper.py" \
  -reducer "$OUT_DIR/reducer.py"

hdfs dfs -cat "$HDFS_BASE/output/ej8/part-00000"

hdfs dfs -get -f "$HDFS_BASE/output/ej8/part-00000" "$OUT_DIR/salida_ej8.txt"

echo "Downloaded to $OUT_DIR/salida_ej8.txt"
