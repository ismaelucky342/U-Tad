from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
JSONL_PATH = ROOT / "datasets" / "docs.jsonl"
PARQUET_PATH = ROOT / "datasets" / "docs.parquet"


def main() -> None:
    rows: list[dict] = []
    with open(JSONL_PATH, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))

    df = pd.DataFrame(rows)
    df.to_parquet(PARQUET_PATH, index=False)
    print("Wrote:", PARQUET_PATH)


if __name__ == "__main__":
    main()
