from __future__ import annotations

import json
from pathlib import Path


DATA = Path(__file__).resolve().parents[2] / "datasets" / "docs.jsonl"


def main() -> None:
    docs: dict[int, str] = {}

    with open(DATA, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            docs[int(obj["doc_id"])] = obj["text"]

    print("docs:", len(docs))
    print("sample:", docs.get(1))


if __name__ == "__main__":
    main()
