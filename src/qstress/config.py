import json
import typing

from .globals import qstress_path

default_config = {
    "compilerBin": "g++", "compileArgs": ["-O2", "-std=c++17"], "tests": 200, "find": 1,
    "folder": "test_cases"
}

def get_config() -> dict[str, typing.Any]:

    config_path = qstress_path / "config.json"

    if not config_path.exists():
        with config_path.open("w+") as file:
            json.dump(default_config, file, indent=4)

    with config_path.open("r") as file:
        return json.load(file)

global_config = default_config | get_config()
