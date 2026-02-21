import hashlib
import json
import pathlib

from .globals import internal_path

cache_path = internal_path / "cache.json"

def get_cache() -> dict[str, str]:

    default_cache = {"check": "", "gen": "", "main": "", "slow": ""}

    if not cache_path.exists():
        with cache_path.open("w+") as file:
            json.dump(default_cache, file)

    with cache_path.open("r") as file:
        return json.load(file)

def hash_file(file_path: pathlib.Path) -> str:

    with file_path.open("rb") as file:
        return hashlib.sha256(file.read()).hexdigest()

def set_cache(cache: dict[str, str]) -> None:

    with cache_path.open("w") as file:
        json.dump(cache, file)

global_cache = get_cache()
