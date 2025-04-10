import yaml
from pathlib import Path

__all__ = [
    "faiss_database_path",
    "sqlite_database_path",
    "set_faiss_path",
    "set_sqlite_path",
]

with open(".config/config.yaml", "r") as _file:
    config = yaml.safe_load(_file)

_faiss = config.get("Databases", {}).get("Faiss", {})
faiss_database_path = str(
    Path(_faiss.get("folder", ".")).resolve()
    / _faiss.get("name", "faiss_default.index")
)

_sqlite = config.get("Databases", {}).get("Sqlite", {})
sqlite_database_path = Path(_sqlite.get("folder", ".")).resolve() / _sqlite.get(
    "name", "sqlite_default.db"
)

overwrite = False

edit = False


def set_faiss_path(path):
    global faiss_database_path
    faiss_database_path = str(Path(path).resolve())


def set_sqlite_path(path):
    global sqlite_database_path
    sqlite_database_path = str(Path(path).resolve())


def set_faiss_name(name):
    global faiss_database_path
    faiss_database_path = str(Path(_faiss.get("folder", ".")).resolve().joinpath(name))


def set_sqlite_name(name):
    global sqlite_database_path
    sqlite_database_path = str(
        Path(_sqlite.get("folder", ".")).resolve().joinpath(name)
    )


def set_faiss_dir(dir):
    global faiss_database_path
    faiss_database_path = str(
        Path(dir).resolve() / _faiss.get("name", "faiss_default.index")
    )


def set_sqlite_dir(dir):
    global sqlite_database_path
    sqlite_database_path = str(
        Path(dir).resolve() / _sqlite.get("name", "sqlite_default.db")
    )


def set_faiss_dir_name(dir, name):
    global faiss_database_path
    faiss_database_path = str(Path(dir).resolve().joinpath(name))


def set_sqlite_dir_name(dir, name):
    global sqlite_database_path
    sqlite_database_path = str(Path(dir).resolve().joinpath(name))
