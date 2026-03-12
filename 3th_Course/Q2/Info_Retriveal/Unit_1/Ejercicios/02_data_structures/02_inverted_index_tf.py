from __future__ import annotations

from collections.abc import Iterable


def build_index_tf(documents: dict[int, list[str]]) -> dict[str, dict[int, int]]:
    """Índice invertido token -> {doc_id: tf}.

    Input: documents ya tokenizados.

    TODO:
    - Construye el dict anidado
    - Usa `dict.get` para simplificar
    """
    # TODO: implement
    raise NotImplementedError


def postings(index: dict[str, dict[int, int]], term: str) -> dict[int, int]:
    """Devuelve posting list con TF (doc_id -> tf) para el término."""
    return index.get(term, {})


def query_and_tf(index: dict[str, dict[int, int]], terms: Iterable[str]) -> set[int]:
    """AND booleano usando las claves doc_id de cada posting list."""
    # TODO: implement
    raise NotImplementedError


if __name__ == "__main__":
    tokenized = {
        1: ["python", "datos", "datos"],
        2: ["busqueda", "informacion"],
        3: ["python", "pandas", "datos"],
    }

    # TODO: cuando implementes
    # idx = build_index_tf(tokenized)
    # print(postings(idx, "datos"))
    # print(query_and_tf(idx, ["python", "datos"]))
