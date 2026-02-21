import pathlib

import rich.console

qstress_path = pathlib.Path.home() / ".qstress"
internal_path = qstress_path / "_internal"

console = rich.console.Console()

def ensure_paths() -> None:

    if not qstress_path.exists():
        qstress_path.mkdir()
        if not internal_path.exists():
            internal_path.mkdir()
            if not (internal_path / "bin").exists():
                (internal_path / "bin").mkdir()
            if not (internal_path / "io").exists():
                (internal_path / "io").mkdir()

ensure_paths()
