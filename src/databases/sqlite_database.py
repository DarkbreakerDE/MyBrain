import sqlite3
import atexit
import Config
import os
from typing import Optional


conn: Optional[sqlite3.Connection] = None
cursor: Optional[sqlite3.Cursor] = None


def init():
    global conn, cursor

    if Config.overwrite and os.path.exists(Config.sqlite_database_path):
        os.remove(Config.sqlite_database_path)

    conn = sqlite3.connect(Config.sqlite_database_path)
    cursor = conn.cursor()

    # Foreign keys aktivieren
    cursor.execute("PRAGMA foreign_keys = ON")

    # Tabellen erstellen
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            fingerprint TEXT NOT NULL UNIQUE
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS passages (
            id INTEGER PRIMARY KEY,
            text TEXT,
            file_id INTEGER NOT NULL,
            FOREIGN KEY (file_id) REFERENCES files(id) ON DELETE CASCADE
        )
        """
    )

    atexit.register(conn.close)


def next_id():
    assert cursor is not None
    cursor.execute("SELECT MAX(id) FROM passages")
    result = cursor.fetchone()
    current_max_id = result[0] if result[0] is not None else -1
    return current_max_id + 1


def insert_passages(passages, file_id):
    assert cursor is not None
    assert conn is not None
    base_id = next_id()
    for idx, passage in enumerate(passages):
        cursor.execute(
            "INSERT INTO passages (id, text, file_id) VALUES (?, ?, ?)",
            (base_id + idx, passage, file_id),
        )
    conn.commit()


def get_passage(passage_id):
    assert cursor is not None
    cursor.execute("SELECT text FROM passages WHERE id = ?", (passage_id,))
    row = cursor.fetchone()
    return row[0] if row else None


def get_passage_context(passage_id: int, before: int = 1, after: int = 1):
    assert cursor is not None
    # Zentrale Passage abrufen (inkl. file_id)
    cursor.execute("SELECT text, file_id FROM passages WHERE id = ?", (passage_id,))
    row = cursor.fetchone()

    if not row:
        return None

    text, file_id = row

    # Vorherige Passagen (absteigend sortiert, später umdrehen)
    cursor.execute(
        """
        SELECT text FROM passages
        WHERE id < ? AND file_id = ?
        ORDER BY id DESC
        LIMIT ?
    """,
        (passage_id, file_id, before),
    )
    prev = [r[0] for r in cursor.fetchall()][::-1]  # Reihenfolge umdrehen

    # Nachfolgende Passagen
    cursor.execute(
        """
        SELECT text FROM passages
        WHERE id > ? AND file_id = ?
        ORDER BY id ASC
        LIMIT ?
    """,
        (passage_id, file_id, after),
    )
    nxt = [r[0] for r in cursor.fetchall()]

    return {"previous": prev, "current": text, "next": nxt}


def insert_file_or_none(filename: str, fingerprint: str):
    assert cursor is not None
    # Versuche zuerst, ob der Fingerprint schon existiert
    cursor.execute("SELECT id FROM files WHERE fingerprint = ?", (fingerprint,))
    row = cursor.fetchone()
    if row:
        return None  # bestehende ID zurückgeben

    # Einfügen und neue ID zurückgeben
    cursor.execute(
        "INSERT INTO files (name, fingerprint) VALUES (?, ?)", (filename, fingerprint)
    )
    return cursor.lastrowid
