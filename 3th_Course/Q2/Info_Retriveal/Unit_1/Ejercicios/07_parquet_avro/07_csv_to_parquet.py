from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
CSV_PATH = ROOT / "datasets" / "ventas.csv"
PARQUET_PATH = ROOT / "datasets" / "ventas.parquet"


def main() -> None:
    df = pd.read_csv(CSV_PATH)
    df.to_parquet(PARQUET_PATH, index=False)
    print("Wrote:", PARQUET_PATH)


if __name__ == "__main__":
    main()
