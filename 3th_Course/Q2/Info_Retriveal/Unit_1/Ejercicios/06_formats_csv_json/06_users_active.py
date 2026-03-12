from __future__ import annotations

import json
from pathlib import Path


DATA = Path(__file__).resolve().parents[2] / "datasets" / "users.json"


def main() -> None:
    with open(DATA, encoding="utf-8") as f:
        payload = json.load(f)

    users = payload.get("users", [])

    active = [u for u in users if u.get("active") is True]
    for u in active:
        print(f"{u.get('name')} ({u.get('city')})")


if __name__ == "__main__":
    main()
