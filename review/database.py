import sqlite3

DATABASE = 'user-db-example'

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.row
    return conn

def get_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    stores = cursor.fetchall()
    conn.close()
    return stores

def get_users_per_page(page, count):
    conn = get_connection
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stores WHERE Name LIKE ?", ('%' + name + '%'))
    
