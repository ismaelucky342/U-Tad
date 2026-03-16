#!/usr/bin/env bash
set -euo pipefail

# Enunciado: ejecutar WordCount con Hadoop Streaming.
# Objetivo: completar un job MapReduce de principio a fin.

HDFS_BASE="/piscine_hadoop"
LOCAL_DIR="${LOCAL_DIR:-$PWD/piscine_hadoop_local}"
WC_DIR="$LOCAL_DIR/wordcount"

mkdir -p "$WC_DIR"

cat > "$WC_DIR/input_wc.txt" <<'EOF'
hello hadoop
hello mapreduce
hello hdfs
EOF

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

hdfs dfs -mkdir -p "$HDFS_BASE/data" "$HDFS_BASE/output"
hdfs dfs -put -f "$WC_DIR/input_wc.txt" "$HDFS_BASE/data/"
hdfs dfs -rm -r -f "$HDFS_BASE/output/wc"

if [[ -z "${HADOOP_HOME:-}" ]]; then
    echo "HADOOP_HOME is not set. Please export HADOOP_HOME and re-run."
    exit 1
fi

STREAMING_JAR=$(ls "$HADOOP_HOME"/share/hadoop/tools/lib/hadoop-streaming*.jar 2>/dev/null | head -n 1)
if [[ -z "$STREAMING_JAR" ]]; then
    echo "Hadoop streaming jar not found under HADOOP_HOME."
    exit 1
fi

hadoop jar "$STREAMING_JAR" \
  -input "$HDFS_BASE/data/input_wc.txt" \
  -output "$HDFS_BASE/output/wc" \
  -mapper "$WC_DIR/mapper.py" \
  -reducer "$WC_DIR/reducer.py"

hdfs dfs -cat "$HDFS_BASE/output/wc/part-00000"
