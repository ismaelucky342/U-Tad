#!/usr/bin/env bash
set -euo pipefail

# Enunciado: observar splits y numero de mappers.
# Objetivo: relacionar bloques, splits y paralelismo.

HDFS_BASE="/piscine_hadoop"
LOCAL_DIR="${LOCAL_DIR:-$PWD/piscine_hadoop_local}"
WC_DIR="$LOCAL_DIR/wordcount"

mkdir -p "$LOCAL_DIR" "$WC_DIR"

cat > "$WC_DIR/mapper.py" <<'EOF'
#!/usr/bin/env python3
import sys
for line in sys.stdin:
    for word in line.strip().split():
        if word:
            print(f"{word}\t1")
EOF

cat > "$WC_DIR/reducer.py" <<'EOF'
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

chmod +x "$WC_DIR/mapper.py" "$WC_DIR/reducer.py"

# Create a ~3MB text file
yes "lorem ipsum dolor sit amet" | head -c 3145728 > "$LOCAL_DIR/archivo_grande.txt"

hdfs dfs -mkdir -p "$HDFS_BASE/data" "$HDFS_BASE/output"
hdfs dfs -put -f "$LOCAL_DIR/archivo_grande.txt" "$HDFS_BASE/data/"

hdfs dfs -stat %b "$HDFS_BASE/data/archivo_grande.txt"

if [[ -z "${HADOOP_HOME:-}" ]]; then
    echo "HADOOP_HOME is not set. Please export HADOOP_HOME and re-run."
    exit 1
fi

STREAMING_JAR=$(ls "$HADOOP_HOME"/share/hadoop/tools/lib/hadoop-streaming*.jar 2>/dev/null | head -n 1)
if [[ -z "$STREAMING_JAR" ]]; then
    echo "Hadoop streaming jar not found under HADOOP_HOME."
    exit 1
fi

hdfs dfs -rm -r -f "$HDFS_BASE/output/splits_small"

# Force small split size (1MB) to increase mappers
hadoop jar "$STREAMING_JAR" \
  -D mapreduce.input.fileinputformat.split.maxsize=1048576 \
  -input "$HDFS_BASE/data/archivo_grande.txt" \
  -output "$HDFS_BASE/output/splits_small" \
  -mapper "$WC_DIR/mapper.py" \
  -reducer "$WC_DIR/reducer.py"

hdfs dfs -cat "$HDFS_BASE/output/splits_small/part-00000" | head -n 5
