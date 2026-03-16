#!/usr/bin/env bash
set -euo pipefail

# Enunciado: suma y maximo por categoria con MapReduce.

HDFS_BASE="/piscine_hadoop"
LOCAL_DIR="${LOCAL_DIR:-$PWD/piscine_hadoop_local}"
EX_DIR="$LOCAL_DIR/extra_01"

mkdir -p "$EX_DIR"

cat > "$EX_DIR/ventas.csv" <<'EOF'
catA,10
catB,7
catA,3
catB,12
catC,4
EOF

cat > "$EX_DIR/mapper.py" <<'EOF'
#!/usr/bin/env python3
import sys
for line in sys.stdin:
    key, value = line.strip().split(",", 1)
    if key:
        print(f"{key}\t{value}")
EOF

cat > "$EX_DIR/reducer.py" <<'EOF'
#!/usr/bin/env python3
import sys
current = None
total = 0
maxv = None
for line in sys.stdin:
    key, value = line.strip().split("\t", 1)
    value = int(value)
    if current is None:
        current = key
        maxv = value
    if key != current:
        print(f"{current}\tsuma={total}\tmax={maxv}")
        current = key
        total = 0
        maxv = value
    total += value
    if value > maxv:
        maxv = value
if current is not None:
    print(f"{current}\tsuma={total}\tmax={maxv}")
EOF

chmod +x "$EX_DIR/mapper.py" "$EX_DIR/reducer.py"

hdfs dfs -mkdir -p "$HDFS_BASE/data" "$HDFS_BASE/output"
hdfs dfs -put -f "$EX_DIR/ventas.csv" "$HDFS_BASE/data/"

if [[ -z "${HADOOP_HOME:-}" ]]; then
    echo "HADOOP_HOME is not set. Please export HADOOP_HOME and re-run."
    exit 1
fi

STREAMING_JAR=$(ls "$HADOOP_HOME"/share/hadoop/tools/lib/hadoop-streaming*.jar 2>/dev/null | head -n 1)
if [[ -z "$STREAMING_JAR" ]]; then
    echo "Hadoop streaming jar not found under HADOOP_HOME."
    exit 1
fi

hdfs dfs -rm -r -f "$HDFS_BASE/output/extra_01"

hadoop jar "$STREAMING_JAR" \
  -input "$HDFS_BASE/data/ventas.csv" \
  -output "$HDFS_BASE/output/extra_01" \
  -mapper "$EX_DIR/mapper.py" \
  -reducer "$EX_DIR/reducer.py"

hdfs dfs -cat "$HDFS_BASE/output/extra_01/part-00000"
