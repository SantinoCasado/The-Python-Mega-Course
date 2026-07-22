import hashlib
import os
import re
import sqlite3
from contextlib import contextmanager
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_FILE_NAME = os.getenv("SQLITE_DB_FILE", "users_db_app.sqlite3").strip()
DB_FILE_PATH = BASE_DIR / DB_FILE_NAME

DEFAULT_USERS = [
    ("admin", "Admin123"),
    ("demo", "Demo123"),
]


def validate_password_strength(password):
    if len(password) < 6 or len(password) > 12:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    return True


def get_db_settings_masked():
    return {
        "engine": "sqlite",
        "database": str(DB_FILE_PATH),
        "host": "local_file",
        "port": "-",
        "user": "-",
        "password_set": False,
    }


def _hash_password(password):
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


@contextmanager
def get_connection():
    BASE_DIR.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(DB_FILE_PATH)
    try:
        yield connection
    finally:
        connection.close()


def test_connection():
    try:
        with get_connection() as connection:
            with connection:
                connection.execute("SELECT 1")
        return True, "ok"
    except sqlite3.Error:
        return False, "sqlite_error"
    except Exception:
        return False, "unknown_error"


def init_database():
    with get_connection() as connection:
        with connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """
            )
            cursor = connection.cursor()
            cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name='health_logs'"
            )
            has_health_logs = cursor.fetchone() is not None

            if not has_health_logs:
                connection.execute(
                    """
                    CREATE TABLE health_logs (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER NOT NULL,
                        log_date TEXT NOT NULL,
                        weight REAL,
                        meals TEXT,
                        notes TEXT,
                        mood TEXT,
                        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        UNIQUE(user_id, log_date),
                        FOREIGN KEY(user_id) REFERENCES users(id)
                    )
                    """
                )
            else:
                cursor.execute("PRAGMA table_info(health_logs)")
                columns = [row[1] for row in cursor.fetchall()]
                if "user_id" not in columns:
                    connection.execute("ALTER TABLE health_logs RENAME TO health_logs_legacy")
                    connection.execute(
                        """
                        CREATE TABLE health_logs (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER NOT NULL,
                            log_date TEXT NOT NULL,
                            weight REAL,
                            meals TEXT,
                            notes TEXT,
                            mood TEXT,
                            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            UNIQUE(user_id, log_date),
                            FOREIGN KEY(user_id) REFERENCES users(id)
                        )
                        """
                    )
                    connection.execute("DROP TABLE health_logs_legacy")


def seed_default_users():
    with get_connection() as connection:
        with connection:
            for username, password in DEFAULT_USERS:
                password_hash = _hash_password(password)
                connection.execute(
                    """
                    INSERT INTO users (username, password_hash)
                    VALUES (?, ?)
                    ON CONFLICT(username) DO NOTHING
                    """,
                    (username, password_hash),
                )


def create_user(username, password):
    if not validate_password_strength(password):
        raise ValueError("Invalid password format")

    password_hash = _hash_password(password)
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT 1 FROM users WHERE username = ?", (username,))
        if cursor.fetchone():
            return False

        try:
            cursor.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                (username, password_hash),
            )
            connection.commit()
            return True
        except sqlite3.IntegrityError:
            connection.rollback()
            return False


def validate_user(username, password):
    password_hash = _hash_password(password)
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT id FROM users WHERE username = ? AND password_hash = ?",
            (username, password_hash),
        )
        user = cursor.fetchone()
        return user is not None


def authenticate_user(username, password):
    password_hash = _hash_password(password)
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT id, username FROM users WHERE username = ? AND password_hash = ?",
            (username, password_hash),
        )
        user = cursor.fetchone()
        if not user:
            return None
        return {"id": user[0], "username": user[1]}


def upsert_health_log(user_id, log_date, weight, meals, notes, mood):
    with get_connection() as connection:
        with connection:
            connection.execute(
                """
                INSERT INTO health_logs (user_id, log_date, weight, meals, notes, mood, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
                ON CONFLICT(user_id, log_date) DO UPDATE SET
                    weight = excluded.weight,
                    meals = excluded.meals,
                    notes = excluded.notes,
                    mood = excluded.mood,
                    updated_at = CURRENT_TIMESTAMP
                """,
                (user_id, log_date, weight, meals, notes, mood),
            )


def get_health_log_by_date(user_id, log_date):
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT weight, meals, notes, mood
            FROM health_logs
            WHERE user_id = ? AND log_date = ?
            """,
            (user_id, log_date),
        )
        row = cursor.fetchone()
        if not row:
            return None

        return {
            "weight": row[0],
            "meals": row[1] or "",
            "notes": row[2] or "",
            "mood": row[3] or "",
        }


def list_health_logs(user_id, limit=30):
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT log_date, weight, meals, notes, mood
            FROM health_logs
            WHERE user_id = ?
            ORDER BY log_date DESC
            LIMIT ?
            """,
            (user_id, limit),
        )
        rows = cursor.fetchall()

    logs = []
    for row in rows:
        logs.append(
            {
                "log_date": row[0],
                "weight": row[1],
                "meals": row[2] or "",
                "notes": row[3] or "",
                "mood": row[4] or "",
            }
        )
    return logs
