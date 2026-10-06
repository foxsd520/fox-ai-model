import sqlite3
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any

DB_DIR = Path(__file__).resolve().parent.parent / "data"
DB_DIR.mkdir(exist_ok=True)
DB_PATH = DB_DIR / "foxsd_ai.sqlite"


class FoxSDDatabase:
    """Database layer for FoxSD AI interactions and training."""

    def __init__(self, db_path: str = str(DB_PATH)):
        self.db_path = db_path
        self._init_schema()

    def _get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_schema(self):
        conn = self._get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT NOT NULL,
                user_message TEXT NOT NULL,
                ai_response TEXT NOT NULL,
                intent TEXT DEFAULT 'general',
                tags TEXT DEFAULT '[]',
                model_version TEXT DEFAULT '1.0.0',
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(session_id, created_at)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS training_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT NOT NULL,
                content TEXT NOT NULL,
                keywords TEXT DEFAULT '[]',
                source TEXT DEFAULT 'manual',
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                role TEXT DEFAULT 'user',
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS feedback (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                conversation_id INTEGER NOT NULL,
                rating INTEGER,
                comment TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (conversation_id) REFERENCES conversations(id)
            )
        """)

        conn.commit()
        conn.close()

    def save_conversation(self, session_id: str, user_msg: str, ai_response: str, intent: str, tags: List[str]) -> int:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO conversations (session_id, user_message, ai_response, intent, tags)
            VALUES (?, ?, ?, ?, ?)
        """, (session_id, user_msg, ai_response, intent, str(tags)))
        conn.commit()
        conv_id = cursor.lastrowid
        conn.close()
        return conv_id

    def get_conversations(self, session_id: str, limit: int = 50) -> List[Dict[str, Any]]:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM conversations
            WHERE session_id = ?
            ORDER BY created_at DESC
            LIMIT ?
        """, (session_id, limit))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    def add_training_data(self, category: str, content: str, keywords: List[str]) -> int:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO training_data (category, content, keywords)
            VALUES (?, ?, ?)
        """, (category, content, str(keywords)))
        conn.commit()
        data_id = cursor.lastrowid
        conn.close()
        return data_id

    def get_training_data(self, category: str = None) -> List[Dict[str, Any]]:
        conn = self._get_connection()
        cursor = conn.cursor()
        if category:
            cursor.execute("""
                SELECT * FROM training_data
                WHERE category = ?
                ORDER BY created_at DESC
            """, (category,))
        else:
            cursor.execute("SELECT * FROM training_data ORDER BY created_at DESC")
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    def save_feedback(self, conversation_id: int, rating: int, comment: str = None):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO feedback (conversation_id, rating, comment)
            VALUES (?, ?, ?)
        """, (conversation_id, rating, comment))
        conn.commit()
        conn.close()

    def get_statistics(self) -> Dict[str, Any]:
        conn = self._get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) as total FROM conversations")
        conversations_count = cursor.fetchone()["total"]

        cursor.execute("SELECT COUNT(*) as total FROM training_data")
        training_count = cursor.fetchone()["total"]

        cursor.execute("SELECT COUNT(*) as total FROM users")
        users_count = cursor.fetchone()["total"]

        conn.close()
        return {
            "conversations": conversations_count,
            "training_data": training_count,
            "users": users_count,
        }
