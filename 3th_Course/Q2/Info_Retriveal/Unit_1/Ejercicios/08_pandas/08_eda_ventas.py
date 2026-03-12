from __future__ import annotations

from pathlib import Path

import pandas as pd


DATA = Path(__file__).resolve().parents[2] / "datasets" / "ventas.csv"


def main() -> None:
    # TODO: carga
    df = pd.read_csv(DATA)

    # TODO: inspección
    print("shape:", df.shape)
    print(df.head())
    print(df.info())

    # TODO: ventas por ciudad
    ventas_ciudad = (
        df.groupby("ciudad")["ventas"].sum().sort_values(ascending=False).reset_index()
    )
    print("\nVentas por ciudad:\n", ventas_ciudad)

    # TODO: top vendedores
    ventas_vendedor = (
        df.groupby("vendedor")["ventas"].sum().sort_values(ascending=False).reset_index()
    )
    print("\nVentas por vendedor:\n", ventas_vendedor)
    print("\nTop 2:\n", ventas_vendedor.head(2))


if __name__ == "__main__":
    main()
