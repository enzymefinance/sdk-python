import json
from pathlib import Path


_cache = {}

def get(name: str) -> dict:
    if name in _cache:
        return _cache[name]

    path = Path(__file__).parent / "abis" / f"{name}.abi.json"
    with open(path, "r") as file:
        data = json.load(file)
    _cache[name] = data
    return data
