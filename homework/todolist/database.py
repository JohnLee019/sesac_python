import sqlite3

MY_DATABASE = 'todolist.db'

def connect_db():
    conn = sqlite3.connect(MY_DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute('''
                CREATE TABLE IF NOT EXISTS todolist
                (id INTEGER PRIMARY KEY NOT NULL, 
                todolist TEXT, 
                status TEXT,
                complete_date_time DATETIME)
                ''')

    conn.commit()
    conn.close()

def insert_todo(todolist, status, date_time):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute('INSERT INTO todolist (todolist, status, completed_date_time) VALUES (?, ?, ?)', (todolist, status, date_time))

    conn.commit()
    conn.close()

def get_todolist():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute('SELECT * FROM todolist')
    rows = cur.fetchall()

    conn.commit()
    conn.close()

    return rows

def update_status(todolist, status):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute('UPDATE todolist SET status=? WHERE todolist=?', (status, todolist))

    conn.commit()
    conn.close()

def delete_todolist(todolist):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute('DELETE FROM todolist WHERE todolist=?', (todolist))

