import sqlite3
from pathlib import Path
from .models import Item

_DB_DIR = Path(__file__).parent.parent / "db"
_DB_FILE = _DB_DIR / "bg_scaffolding.db"

_conn = sqlite3.connect(_DB_FILE, check_same_thread=False)
_conn.row_factory = sqlite3.Row
_conn.execute("PRAGMA foreign_keys = ON")

_conn.executescript((_DB_DIR / "schema.sql").read_text())
_conn.executescript((_DB_DIR / "seed.sql").read_text())


def get_all() -> list[Item]:
    rows = _conn.execute("SELECT id, name FROM items").fetchall()
    return [Item(id=row["id"], name=row["name"]) for row in rows]


def get_by_id(item_id: int) -> Item | None:
    row = _conn.execute(
        "SELECT id, name FROM items WHERE id = ?", (item_id,)
    ).fetchone()
    return Item(id=row["id"], name=row["name"]) if row else None


def reset() -> None:
    _conn.execute("DELETE FROM items")
    _conn.commit()
