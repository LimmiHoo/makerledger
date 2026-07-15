# === Stage 22: Add favorite records and quick favorite listing ===
# Project: MakerLedger
import sqlite3

def add_favorites(conn):
    """Add a favorites table and helper functions for quick favorite access."""
    conn.execute("""
        CREATE TABLE IF NOT EXISTS favorites (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            category TEXT DEFAULT 'general',
            added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )""")

    def add_favorite(name: str, category: str = "general") -> int:
        """Add a new favorite and return its ID."""
        conn.execute(
            "INSERT INTO favorites (name, category) VALUES (?, ?)",
            (name, category),
        )
        return conn.commit()

    def get_favorites(category_filter=None):
        """Return all favorites, optionally filtered by category."""
        if category_filter:
            cur = conn.execute(
                "SELECT id, name, category, added_at FROM favorites WHERE category = ? ORDER BY added_at",
                (category_filter,),
            )
        else:
            cur = conn.execute("SELECT id, name, category, added_at FROM favorites ORDER BY added_at")
        return [dict(row) for row in cur.fetchall()]

    def remove_favorite(fav_id: int):
        """Remove a favorite by its ID."""
        conn.execute("DELETE FROM favorites WHERE id = ?", (fav_id,))
        conn.commit()
