from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="CLI de consulta booleana (mini)")
    parser.add_argument("mode", choices=["and", "or"], help="Modo booleano")
    parser.add_argument("terms", nargs="+", help="Términos de búsqueda")

    args = parser.parse_args()

    # TODO: construye o carga un índice invertido (puedes hardcodear 3 docs al inicio)
    # TODO: ejecuta query AND/OR según args.mode
    # TODO: imprime doc_ids recuperados
    raise NotImplementedError


if __name__ == "__main__":
    main()
