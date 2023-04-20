
import sqlite3
import datetime

krar_conn = sqlite3.connect('new/krar.db')
krar_cursor = krar_conn.cursor()


krar_cursor.execute('''CREATE TABLE if not exists krars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    krar_date TEXT NOT NULL,
    tag INTEGER NOT NULL DEFAULT 1)''')

def create_krar(customer_name, krar_date):
    with krar_conn:
        krar_cursor.execute("INSERT INTO krars (customer_name, krar_date) VALUES (?, ?)", (customer_name, krar_date))
        krar_id = krar_cursor.lastrowid
        return krar_id

def get_krar_by_id(krar_id):
    krar_cursor.execute("SELECT * FROM krars WHERE id = ?", (krar_id,))
    krar = krar_cursor.fetchone()
    return krar

def get_all_krars():
    krar_cursor.execute("SELECT * FROM krars")
    krars = krar_cursor.fetchall()
    return krars

def get_all_due_krars():
    krar_cursor.execute("SELECT * FROM krars where tag = 1")
    return krar_cursor.fetchall()

def get_krars_by_customer_name(customer_name):
    krar_cursor.execute("SELECT * FROM krars WHERE customer_name = ?", (customer_name,))
    krars = krar_cursor.fetchall()
    return krars

def get_due_krars_by_customer_name(customer_name):
    krar_cursor.execute("SELECT * FROM krars WHERE customer_name = ? AND tag = 1", (customer_name,))
    krars = krar_cursor.fetchall()
    return krars



def get_krars_by_date(date=None):
    if date is None:
        date = datetime.date.today().strftime('%Y-%m-%d')
    krar_cursor.execute('''SELECT * FROM krars WHERE krar_date = ? and tag = 1''', (date,))
    return krar_cursor.fetchall()

def update_krar_tag(krar_id, tag):
    with krar_conn:
        krar_cursor.execute("UPDATE krars SET tag = ? WHERE id = ?", (tag, krar_id))
        krar_conn.commit()

def update_krar_tag_by_name(krar_name, tag):
    with krar_conn:
        krar_cursor.execute("UPDATE krars SET tag = ? WHERE customer_name = ?", (tag, krar_name))
        krar_conn.commit()



def update_krar_by_id(krar_id, customer_name=None, krar_date=None, tag=None):
    
    cursor = krar_conn.cursor()
    update_query = 'UPDATE krars SET'
    update_query_params = []
    if customer_name is not None:
        update_query += ' customer_name=?,'
        update_query_params.append(customer_name)
    if krar_date is not None:
        update_query += ' krar_date=?,'
        update_query_params.append(krar_date)
    if tag is not None:
        update_query += ' tag=?,'
        update_query_params.append(tag)
    # Remove the trailing comma from the update query
    update_query = update_query.rstrip(',')
    # Add the WHERE clause to the query
    update_query += ' WHERE id=?'
    update_query_params.append(krar_id)
    cursor.execute(update_query, update_query_params)
    krar_conn.commit()

def delete_krar(krar_id):
    with krar_conn:
        krar_cursor.execute("DELETE FROM krars WHERE id = ?", (krar_id,))
        krar_conn.commit()


