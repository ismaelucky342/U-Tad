#!/usr/bin/env bash
set -euo pipefail

# Enunciado: media de temperatura por sensor.

HDFS_BASE="/piscine_hadoop"
LOCAL_DIR="${LOCAL_DIR:-$PWD/piscine_hadoop_local}"
EX_DIR="$LOCAL_DIR/extra_02"

mkdir -p "$EX_DIR"

cat > "$EX_DIR/temps.csv" <<'EOF'
s1,20
s1,25
s2,18
s2,22
s2,20
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
count = 0
for line in sys.stdin:
    key, value = line.strip().split("\t", 1)
    value = float(value)
    if current is None:
        current = key
    if key != current:
        mean = total / count if count else 0
        print(f"{current}\tmedia={mean:.2f}")
        current = key
        total = 0
        count = 0
    total += value
    count += 1
if current is not None:
    mean = total / count if count else 0
    print(f"{current}\tmedia={mean:.2f}")
EOF

chmod +x "$EX_DIR/mapper.py" "$EX_DIR/reducer.py"

hdfs dfs -mkdir -p "$HDFS_BASE/data" "$HDFS_BASE/output"
hdfs dfs -put -f "$EX_DIR/temps.csv" "$HDFS_BASE/data/"

if [[ -z "${HADOOP_HOME:-}" ]]; then
    echo "HADOOP_HOME is not set. Please export HADOOP_HOME and re-run."
    exit 1
fi

STREAMING_JAR=$(ls "$HADOOP_HOME"/share/hadoop/tools/lib/hadoop-streaming*.jar 2>/dev/null | head -n 1)
if [[ -z "$STREAMING_JAR" ]]; then
    echo "Hadoop streaming jar not found under HADOOP_HOME."
    exit 1
fi

hdfs dfs -rm -r -f "$HDFS_BASE/output/extra_02"

hadoop jar "$STREAMING_JAR" \
  -input "$HDFS_BASE/data/temps.csv" \
  -output "$HDFS_BASE/output/extra_02" \
  -mapper "$EX_DIR/mapper.py" \
  -reducer "$EX_DIR/reducer.py"

hdfs dfs -cat "$HDFS_BASE/output/extra_02/part-00000"
