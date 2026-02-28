import sqlite3


class UserStore:
    def __init__(self, db_path):
        self.db_path = db_path
        self.init_db()

    # ----------------------------
    # Initialize Database
    # ----------------------------
    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """)

        conn.commit()
        conn.close()

    # ----------------------------
    # Load All Users
    # ----------------------------
    def load(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT id, name, email FROM users")
        rows = cursor.fetchall()

        conn.close()

        return [
            {"id": row[0], "name": row[1], "email": row[2]}
            for row in rows
        ]

    # ----------------------------
    # Create User
    # ----------------------------
    def save(self, user_data):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (user_data["name"], user_data["email"])
        )

        conn.commit()
        new_id = cursor.lastrowid
        conn.close()

        return {
            "id": new_id,
            "name": user_data["name"],
            "email": user_data["email"]
        }

    # ----------------------------
    # Find User by ID
    # ----------------------------
    def find_by_id(self, user_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, name, email FROM users WHERE id = ?",
            (user_id,)
        )

        row = cursor.fetchone()
        conn.close()

        if row:
            return {"id": row[0], "name": row[1], "email": row[2]}

        return None

    # ----------------------------
    # Update User
    # ----------------------------
    def update_user(self, user_id, updated_data):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE users SET name = ?, email = ? WHERE id = ?",
            (updated_data["name"], updated_data["email"], user_id)
        )

        conn.commit()
        updated = cursor.rowcount
        conn.close()

        return updated > 0

    # ----------------------------
    # Delete User
    # ----------------------------
    def delete_user(self, user_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM users WHERE id = ?",
            (user_id,)
        )

        conn.commit()
        deleted = cursor.rowcount
        conn.close()

        return deleted > 0