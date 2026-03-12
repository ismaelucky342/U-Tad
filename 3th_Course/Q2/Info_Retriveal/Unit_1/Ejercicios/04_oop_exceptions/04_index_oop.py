from __future__ import annotations


class EmptyQueryError(ValueError):
    pass


class Tokenizer:
    def __init__(self, *, lowercase: bool = True):
        self.lowercase = lowercase

    def tokenize(self, text: str) -> list[str]:
        # TODO: normaliza + split
        raise NotImplementedError


class InvertedIndex:
    def __init__(self, tokenizer: Tokenizer | None = None):
        self.tokenizer = tokenizer or Tokenizer()
        self._index: dict[str, set[int]] = {}

    def add_document(self, doc_id: int, text: str) -> None:
        # TODO: tokeniza y añade doc_id a postings sets
        raise NotImplementedError

    def query_and(self, terms: list[str]) -> set[int]:
        if not terms:
            raise EmptyQueryError("Consulta vacía")
        # TODO: intersección
        raise NotImplementedError

    def query_or(self, terms: list[str]) -> set[int]:
        if not terms:
            raise EmptyQueryError("Consulta vacía")
        # TODO: unión
        raise NotImplementedError


if __name__ == "__main__":
    idx = InvertedIndex()
    idx.add_document(1, "Python y datos")
    idx.add_document(2, "Búsqueda de información")
    idx.add_document(3, "Python, pandas y datos")

    # TODO: prueba cuando implementes
    # print(idx.query_and(["python", "datos"]))
    # print(idx.query_or(["informacion", "pandas"]))
