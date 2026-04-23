import sqlite3
from datetime import date
from pathlib import Path
from .models import Apartment

_DB_DIR = Path(__file__).parent.parent / "db"
_DB_FILE = _DB_DIR / "bg_scaffolding.db"

_conn = sqlite3.connect(_DB_FILE, check_same_thread=False)
_conn.row_factory = sqlite3.Row
_conn.execute("PRAGMA foreign_keys = ON")

_conn.executescript((_DB_DIR / "schema.sql").read_text())
_conn.executescript((_DB_DIR / "seed.sql").read_text())


def is_apartment_available(apartment_id: int, start_date: date, end_date: date):
    row = _conn.execute(
        "SELECT 1 FROM reservations WHERE apartment = ? AND start_date < ? AND end_date > ?",
        (apartment_id, end_date, start_date)
    ).fetchone()
    return row is None


def get_available_apartments(start_date: date, end_date: date):
    rows = _conn.execute(
        "SELECT ap.* FROM apartments ap "
        "LEFT JOIN reservations res ON res.apartment = ap.id "
        "AND res.start_date < ? AND res.end_date > ? "
        "WHERE res.id IS NULL",
        (end_date, start_date)
    ).fetchall()
    return [Apartment(id=row["id"], address=row["address"], floor=row["floor"], description=row["description"],
                      owner=row["owner"]) for row in rows]
