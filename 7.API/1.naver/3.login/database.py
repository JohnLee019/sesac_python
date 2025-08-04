import sqlite3
import bcrypt

DB_FILENAME = 'users.db'

conn = sqlite3.connect(DB_FILENAME)
cur = conn.cursor()

# 테이블 생성
cur.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT,
    name TEXT
)
''')

def check_user(username):
    conn = sqlite3.connect(DB_FILENAME)
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cur.fetchone()
    conn.close()
    return user


def create_user(username, name):
    conn = sqlite3.connect(DB_FILENAME)
    cur = conn.cursor()
    cur.execute("INSERT INTO users (username, password, name) VALUES (?, ?, ?)",
                (username, None, name))
    conn.commit()
    conn.close()

def update_user(username, password, name):
    conn = sqlite3.connect(DB_FILENAME)
    cur = conn.cursor()
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    cur.execute(
        "UPDATE users SET password=?, name=? WHERE username=?",
        (hashed, name, username)
    )
    conn.commit()
    changed = cur.rowcount
    conn.close()
    return changed