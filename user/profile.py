import sqlite3

def update_profile(conn, user_id, key, value):
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS profiles (
        user_id INTEGER,
        key TEXT,
        value TEXT
    )
    """)

    cursor.execute("""
    INSERT INTO profiles (user_id, key, value)
    VALUES (?, ?, ?)
    """, (user_id, key, value))

    conn.commit()

def get_profile(conn, user_id):
    cursor = conn.cursor()

    cursor.execute(
        "SELECT key, value FROM profiles WHERE user_id=?",
        (user_id,)
    )

    rows = cursor.fetchall()
    return {k: v for k, v in rows}