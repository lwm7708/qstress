import pathlib
import shutil
import subprocess
import typing

from .cache import global_cache
from .cache import hash_file
from .cache import set_cache
from .config import global_config
from .globals import console
from .globals import internal_path

def get_path(*args: str) -> pathlib.Path:

    path = internal_path

    for x in args:
        path /= x

    return path

def compile_file(source_file: str, target: str, status: typing.Any) -> bool:

    status.update(f"Compiling [bold]{source_file}[/]")
    source_path = pathlib.Path.cwd() / source_file

    cur_hash = hash_file(source_path)

    if cur_hash == global_cache[target]:
        console.print(f"Used cached [bold]{source_file}[/]")
        return True

    process = subprocess.run(
        [shutil.which(global_config["compilerBin"])] + global_config["compileArgs"] +
        [str(source_path), "-o", str(get_path("bin", target))]
    )

    if process.returncode:
        console.print()
        console.print(f"[red]Failed to compile [bold]{source_file}[/][/]")
        return False

    console.print(f"Compiled [bold]{source_file}[/]")

    global_cache[target] = cur_hash

    set_cache(global_cache)

    return True

def run_bin(bin_file: str, **kwargs) -> subprocess.CompletedProcess:

    return subprocess.run([str(get_path("bin", bin_file))], **kwargs)
