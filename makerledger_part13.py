# === Stage 13: Add file save support using a configurable path ===
# Project: MakerLedger
import os

class Ledger:
    def __init__(self, path="ledger.db"):
        self.path = path
        import sqlite3
        conn = sqlite3.connect(self.path)
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS materials (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, qty REAL)")
        c.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT)")
        c.execute("CREATE TABLE IF NOT EXISTS costs (id INTEGER PRIMARY KEY AUTOINCREMENT, amount REAL)")
        c.execute("CREATE TABLE IF NOT EXISTS experiments (id INTEGER PRIMARY KEY AUTOINCREMENT, note TEXT)")
        conn.commit()

    def add_material(self, name, qty):
        with sqlite3.connect(self.path) as conn:
            conn.execute("INSERT INTO materials (name, qty) VALUES (?, ?)", (name, float(qty)))

    def add_task(self, title, description=""):
        with sqlite3.connect(self.path) as conn:
            conn.execute("INSERT INTO tasks (title, description) VALUES (?, ?)", (title, description))

    def add_cost(self, amount):
        with sqlite3.connect(self.path) as conn:
            conn.execute("INSERT INTO costs (amount) VALUES (?)", (float(amount),))

    def add_experiment(self, note=""):
        with sqlite3.connect(self.path) as conn:
            conn.execute("INSERT INTO experiments (note) VALUES (?)", (note,))

    def snapshot(self):
        with sqlite3.connect(self.path) as conn:
            rows = conn.execute("SELECT name FROM materials").fetchall() + \
                   conn.execute("SELECT title FROM tasks").fetchall() + \
                   conn.execute("SELECT amount FROM costs").fetchall() + \
                   conn.execute("SELECT note FROM experiments").fetchall()
        return "ledger snapshot\n" + "\n".join(str(r) for r in rows)

    def save(self, path=None):
        if path:
            self.path = path
