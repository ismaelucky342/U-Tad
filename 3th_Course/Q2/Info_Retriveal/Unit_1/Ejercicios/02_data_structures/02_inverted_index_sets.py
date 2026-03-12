from __future__ import annotations

from collections.abc import Iterable


def build_index(documents: dict[int, str]) -> dict[str, set[int]]:
    """Construye un índice invertido token -> set(doc_ids).

    TODO:
    - Normaliza/tokeniza (puedes reusar tu tokenize de ejercicios 01)
    - Rellena el índice con sets
    """
    # TODO: implement
    raise NotImplementedError


def query_and(index: dict[str, set[int]], terms: Iterable[str]) -> set[int]:
    """Consulta booleana AND: intersección de postings."""
    # TODO: implement
    raise NotImplementedError


def query_or(index: dict[str, set[int]], terms: Iterable[str]) -> set[int]:
    """Consulta booleana OR: unión de postings."""
    # TODO: implement
    raise NotImplementedError


if __name__ == "__main__":
    docs = {
        1: "Python es usado en datos",
        2: "Búsqueda de información con índice invertido",
        3: "Datos y pandas con python",
    }

    # TODO: cuando implementes
    # idx = build_index(docs)
    # print("AND(python, datos):", query_and(idx, ["python", "datos"]))
    # print("OR(python, indice):", query_or(idx, ["python", "indice"]))
