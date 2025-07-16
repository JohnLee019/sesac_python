import sqlite3


MY_DATABASE = 'user-sample.db'

def connect_db():
    conn = sqlite3.connect(MY_DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def get_user_count():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    user_count = cursor.fetchone()[0]
    conn.close()
    return user_count
    
def get_users():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    users = [dict(r) for r in users]
    return users

def get_users_per_page(page, count):
    offset_pos = (page - 1) * count
    print(f"페이지:{page}, 오프셋:{offset_pos}")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users LIMIT ? OFFSET ?", (count, offset_pos))
    users = cursor.fetchall()
    conn.close()
    users = [dict(r) for r in users]
    return users

def get_users_by_name(name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE Name Like ?", ('%' + name + '%',))
    users = cursor.fetchall()
    conn.close()
    users = [dict(r) for r in users]
    return users
