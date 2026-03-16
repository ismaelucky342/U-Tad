#!/usr/bin/env bash
set -euo pipefail

# Enunciado: comparar job con y sin combiner.
# Objetivo: reducir trafico en el shuffle.

HDFS_BASE="/piscine_hadoop"
LOCAL_DIR="${LOCAL_DIR:-$PWD/piscine_hadoop_local}"
CB_DIR="$LOCAL_DIR/combiner"

mkdir -p "$CB_DIR"

cat > "$CB_DIR/eventos.csv" <<'EOF'
login,ok
login,ok
compra,ok
login,fail
compra,ok
EOF

cat > "$CB_DIR/mapper.py" <<'EOF'
#!/usr/bin/env python3
import sys
for line in sys.stdin:
    categoria = line.strip().split(",", 1)[0]
    if categoria:
        print(f"{categoria}\t1")
EOF

cat > "$CB_DIR/reducer.py" <<'EOF'
#!/usr/bin/env python3
import sys
current = None
count = 0
for line in sys.stdin:
    key, value = line.strip().split("\t", 1)
    if current is None:
        current = key
    if key != current:
        print(f"{current}\t{count}")
        current = key
        count = 0
    count += int(value)
if current is not None:
    print(f"{current}\t{count}")
EOF

chmod +x "$CB_DIR/mapper.py" "$CB_DIR/reducer.py"

hdfs dfs -mkdir -p "$HDFS_BASE/data" "$HDFS_BASE/output"
hdfs dfs -put -f "$CB_DIR/eventos.csv" "$HDFS_BASE/data/"

if [[ -z "${HADOOP_HOME:-}" ]]; then
    echo "HADOOP_HOME is not set. Please export HADOOP_HOME and re-run."
    exit 1
fi

STREAMING_JAR=$(ls "$HADOOP_HOME"/share/hadoop/tools/lib/hadoop-streaming*.jar 2>/dev/null | head -n 1)
if [[ -z "$STREAMING_JAR" ]]; then
    echo "Hadoop streaming jar not found under HADOOP_HOME."
    exit 1
fi

hdfs dfs -rm -r -f "$HDFS_BASE/output/combiner_off"

# Run without combiner
hadoop jar "$STREAMING_JAR" \
  -input "$HDFS_BASE/data/eventos.csv" \
  -output "$HDFS_BASE/output/combiner_off" \
  -mapper "$CB_DIR/mapper.py" \
  -reducer "$CB_DIR/reducer.py"

hdfs dfs -rm -r -f "$HDFS_BASE/output/combiner_on"

# Run with combiner (same as reducer)
hadoop jar "$STREAMING_JAR" \
  -input "$HDFS_BASE/data/eventos.csv" \
  -output "$HDFS_BASE/output/combiner_on" \
  -mapper "$CB_DIR/mapper.py" \
  -reducer "$CB_DIR/reducer.py" \
  -combiner "$CB_DIR/reducer.py"

hdfs dfs -cat "$HDFS_BASE/output/combiner_on/part-00000"
