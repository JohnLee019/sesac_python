import sqlite3
import calendar
MY_DATABASE = 'user-sample.db'

def connect_db():
    conn = sqlite3.connect(MY_DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

    # user db
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

def get_users_by_name_gender(name, gender):
    conn = connect_db()
    cursor = conn.cursor()
    if name and gender:
        cursor.execute('SELECT * FROM users WHERE Name LIKE ? AND LOWER(Gender) = LOWER(?)', ('%' + name + '%', gender))
    elif name:
        cursor.execute('SELECT * FROM users WHERE Name LIKE ?', ('%' + name + '%',))
    elif gender:
        cursor.execute('SELECT * FROM users WHERE LOWER(Gender) = LOWER(?)',(gender,))
    users = cursor.fetchall()
    conn.close()
    users = [dict(r) for r in users]
    return users

def get_user_by_id(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE Id = ?', (id,))
    users = cursor.fetchall()
    conn.close()
    users = [dict(r) for r in users]
    return users

def get_user_order_detail(id):
    conn = connect_db()
    cursor = conn.cursor()
    id = id.strip()
    cursor.execute('SELECT * FROM orders WHERE UserId = ?', (id,))
    users = cursor.fetchall()
    conn.close()
    users = [dict(r) for r in users]
    return users
    # ---------------------------------------------

    # orders db
def get_orders():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM orders')
    users = cursor.fetchall()
    conn.close()
    users = [dict(r) for r in users]
    return users

def get_orders_per_page(page, count):
    offset_pos = (page - 1) * count
    print(f"페이지:{page}, 오프셋:{offset_pos}")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders LIMIT ? OFFSET ?", (count, offset_pos))
    users = cursor.fetchall()
    conn.close()
    users = [dict(r) for r in users]
    return users

def get_order_detail(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM orders WHERE Id = ?', (id,))
    users = cursor.fetchall()
    conn.close()
    users = [dict(r) for r in users]
    return users
    #----------------------------------

    #orders items db
def get_order_items_per_page(page, count):
    offset_pos = (page - 1) * count
    print(f"페이지:{page}, 오프셋:{offset_pos}")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM order_items LIMIT ? OFFSET ?", (count, offset_pos))
    users = cursor.fetchall()
    conn.close()
    users = [dict(r) for r in users]
    return users

def get_orders_items():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM order_items')
    users = cursor.fetchall()
    conn.close()
    users = [dict(r) for r in users]
    return users

def get_orders_items_id(id):
    conn = connect_db()
    cursor = conn.cursor()
    id = id.strip()
    cursor.execute('SELECT order_items.Id, order_items.OrderId,order_items.ItemId, items.Name FROM order_items JOIN items ON order_items.ItemId = items.Id WHERE order_items.OrderId = ?', (id,))
    users = cursor.fetchall()
    conn.close()
    users = [dict(r) for r in users]
    return users
    #-----------------------------------

    #items db
def get_items():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM items')
    users = cursor.fetchall()
    conn.close()
    users = [dict(r) for r in users]
    return users

def get_items_per_page(page, count):
    offset_pos = (page - 1) * count
    print(f"페이지:{page}, 오프셋:{offset_pos}")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items LIMIT ? OFFSET ?", (count, offset_pos))
    users = cursor.fetchall()
    conn.close()
    users = [dict(r) for r in users]
    return users

def get_item_type(type):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM items WHERE LOWER(Type) = LOWER(?)',(type,))
    users = cursor.fetchall()
    conn.close()
    users = [dict(r) for r in users]
    return users

def get_item_by_id(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM items WHERE Id = ?', (id,))
    users = cursor.fetchall()
    conn.close()
    users = [dict(r) for r in users]
    return users

def get_item_monthly_count(id, unit_price):
    conn = connect_db()
    cursor = conn.cursor()
    total = []
    for num in range(1, 13):
        first_day = f"2023-{num:02d}-01 00:00:00"
        last_day_number = calendar.monthrange(2023, num)[1]
        last_day = f"2023-{num:02d}-{last_day_number} 23:59:59"

        cursor.execute("SELECT COUNT(*) FROM orders JOIN order_items ON orders.Id = order_items.OrderId JOIN items ON items.Id = order_items.ItemId WHERE orders.OrderAt BETWEEN ? AND ? AND items.Id = ?", (first_day, last_day, id))
        
        count = cursor.fetchone()[0]
        revenue = unit_price * count
        total.append([f"2023-{num:02d}", revenue, count])
    conn.close()
    return total
    #------------------------------

    #stores db
def get_stores():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM stores')
    users = cursor.fetchall()
    conn.close()
    users = [dict(r) for r in users]
    return users

def get_stores_per_page(page, count):
    offset_pos = (page - 1) * count
    print(f"페이지:{page}, 오프셋:{offset_pos}")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stores LIMIT ? OFFSET ?", (count, offset_pos))
    users = cursor.fetchall()
    conn.close()
    users = [dict(r) for r in users]
    return users

def get_store_name_area(name, area, district, full_area):
    conn = connect_db()
    cursor = conn.cursor()
    
    if name and area and district:
        cursor.execute('SELECT * FROM stores WHERE Name LIKE ? AND LOWER(Address) LIKE LOWER(?)',('%' + name + '%', full_area + '%',))
    elif name and area:
        cursor.execute('SELECT * FROM stores WHERE Name LIKE ? AND LOWER(Address) LIKE LOWER(?)',('%' + name + '%', area + '%',))
    elif name and district:
        cursor.execute('SELECT * FROM stores WHERE Name LIKE ? AND LOWER(Address) LIKE LOWER(?)',('%' + name + '%', '%' + district + '%',))
    elif area and district:
        cursor.execute('SELECT * FROM stores WHERE LOWER(Address) LIKE LOWER(?)',(full_area + '%',))
    elif area:
        cursor.execute('SELECT * FROM stores WHERE LOWER(Address) LIKE LOWER(?)',(area + '%',))
    elif district:
        cursor.execute('SELECT * FROM stores WHERE LOWER(Address) LIKE LOWER(?)',('%' + district + '%',))

    users = cursor.fetchall()
    conn.close()
    users = [dict(r) for r in users]
    return users

def get_stores_by_id(id):
    conn = connect_db()
    cursor = conn.cursor()
    id = id.strip()
    cursor.execute('SELECT * FROM stores WHERE Id = ?', (id,))
    users = cursor.fetchall()
    conn.close()
    users = [dict(r) for r in users]
    return users
    #-----------------------------