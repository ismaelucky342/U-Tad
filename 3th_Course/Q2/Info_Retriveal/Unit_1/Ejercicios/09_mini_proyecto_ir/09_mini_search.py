from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


DATA = Path(__file__).resolve().parents[2] / "datasets" / "docs.jsonl"


@dataclass(frozen=True)
class Doc:
    doc_id: int
    title: str
    text: str


def load_docs(path: Path) -> list[Doc]:
    """Carga documentos desde JSONL."""
    docs: list[Doc] = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            docs.append(Doc(int(obj["doc_id"]), obj.get("title", ""), obj.get("text", "")))
    return docs


def normalize(text: str) -> str:
    # TODO: normalización (minúsculas, puntuación, espacios)
    raise NotImplementedError


def tokenize(text: str) -> list[str]:
    # TODO: tokenización
    raise NotImplementedError


def build_index(docs: list[Doc]) -> dict[str, set[int]]:
    """Índice invertido token -> set(doc_id)."""
    # TODO: implement
    raise NotImplementedError


def query_and(index: dict[str, set[int]], terms: list[str]) -> set[int]:
    # TODO: implement
    raise NotImplementedError


def query_or(index: dict[str, set[int]], terms: list[str]) -> set[int]:
    # TODO: implement
    raise NotImplementedError


def main() -> None:
    docs = load_docs(DATA)
    index = build_index(docs)

    # TODO: prueba manual
    # print(query_and(index, ["python", "datos"]))
    # print(query_or(index, ["pandas", "indice"]))


if __name__ == "__main__":
    main()
