#!/usr/bin/env bash
set -euo pipefail

# Enunciado: contar peticiones por codigo HTTP desde logs en HDFS.

HDFS_BASE="/piscine_hadoop"
LOCAL_DIR="${LOCAL_DIR:-$PWD/piscine_hadoop_local}"
EX_DIR="$LOCAL_DIR/extra_03"

mkdir -p "$EX_DIR"

cat > "$EX_DIR/access.log" <<'EOF'
10.0.0.1 GET /index.html 200
10.0.0.2 GET /login 200
10.0.0.3 POST /login 401
10.0.0.1 GET /products 200
10.0.0.2 GET /index.html 404
EOF

cat > "$EX_DIR/mapper.py" <<'EOF'
#!/usr/bin/env python3
import sys
for line in sys.stdin:
    parts = line.strip().split()
    if len(parts) >= 4:
        code = parts[-1]
        print(f"{code}\t1")
EOF

cat > "$EX_DIR/reducer.py" <<'EOF'
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

chmod +x "$EX_DIR/mapper.py" "$EX_DIR/reducer.py"

hdfs dfs -mkdir -p "$HDFS_BASE/data" "$HDFS_BASE/output"
hdfs dfs -put -f "$EX_DIR/access.log" "$HDFS_BASE/data/"

if [[ -z "${HADOOP_HOME:-}" ]]; then
    echo "HADOOP_HOME is not set. Please export HADOOP_HOME and re-run."
    exit 1
fi

STREAMING_JAR=$(ls "$HADOOP_HOME"/share/hadoop/tools/lib/hadoop-streaming*.jar 2>/dev/null | head -n 1)
if [[ -z "$STREAMING_JAR" ]]; then
    echo "Hadoop streaming jar not found under HADOOP_HOME."
    exit 1
fi

hdfs dfs -rm -r -f "$HDFS_BASE/output/extra_03"

hadoop jar "$STREAMING_JAR" \
  -input "$HDFS_BASE/data/access.log" \
  -output "$HDFS_BASE/output/extra_03" \
  -mapper "$EX_DIR/mapper.py" \
  -reducer "$EX_DIR/reducer.py"

hdfs dfs -cat "$HDFS_BASE/output/extra_03/part-00000"
