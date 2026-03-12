from __future__ import annotations

import csv
from pathlib import Path


DATA = Path(__file__).resolve().parents[2] / "datasets" / "ventas.csv"


def main() -> None:
    totals: dict[str, int] = {}

    with open(DATA, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            vendedor = row["vendedor"]
            ventas = int(row["ventas"])
            totals[vendedor] = totals.get(vendedor, 0) + ventas

    # TODO: top vendedor
    top_vendedor = max(totals, key=totals.get)
    print("Totales:", totals)
    print("Top:", top_vendedor, totals[top_vendedor])


if __name__ == "__main__":
    main()
