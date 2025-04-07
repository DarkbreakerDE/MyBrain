import yaml
from pathlib import Path

__all__ = ["faiss_database", "sqlite_database"]
relative_path = Path("some/folder/file.txt")
absolute_path = relative_path.resolve()

with open(".config/config.yaml", "r") as file:
    config = yaml.safe_load(file)

_faiss = config.get("Databases", {}).get("Faiss", {})
faiss_database_name = str(
    Path(_faiss.get("folder", ".")).resolve()
    / _faiss.get("name", "faiss_default.index")
)

_sqlite = config.get("Databases", {}).get("Sqlite", {})
sqlite_database_name = Path(_sqlite.get("folder", ".")).resolve() / _sqlite.get(
    "name", "sqlite_default.db"
)
