import sqlite3

# Create a connection to the accounts database
accounts_conn = sqlite3.connect('new/accounts.db')
accounts_cursor = accounts_conn.cursor()


# Create a table to store information about all customers
accounts_cursor.execute('''CREATE TABLE IF NOT EXISTS customers
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                other_details TEXT)''')

# Function to add a new customer to the database
def add_new_customer(name, other_details):
    accounts_cursor.execute("""
        INSERT INTO customers (name, other_details)
        VALUES (?, ?)
    """, (name, other_details))
    id = accounts_cursor.lastrowid
    # Create a new table for the customer with their ID
    accounts_cursor.execute(f'''CREATE TABLE IF NOT EXISTS customer_{id}
                       (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       date TEXT,
                       description TEXT,
                       amount REAL,
                       type TEXT,
                       tags TEXT)''')
    # Insert the new customer into the main customers table
    accounts_conn.commit()

    return id


# Function to get a list of all customer IDs
def get_customer_ids():
    accounts_cursor.execute("SELECT id FROM customers")
    return [row[0] for row in accounts_cursor.fetchall()]

# Function to get customer details by ID
def get_customer_details(customer_id):
    accounts_cursor.execute(f"SELECT * FROM customers WHERE id = {customer_id}")
    return accounts_cursor.fetchone()

def get_all_customers():
    accounts_cursor.execute(f"select * from customers")
    return accounts_cursor.fetchall()

# Function to get all transactions for a specific customer
def get_customer_transactions(customer_id):
    table_name = f'customer_{customer_id}'
    accounts_cursor.execute(f"SELECT * FROM {table_name}")
    return accounts_cursor.fetchall()

def get_transaction_by_id(table_name, transaction_id):
    # table_name = "customer_" + str(item_id)
    accounts_cursor.execute(f"SELECT * FROM {table_name} WHERE id = ?", (transaction_id,))
    transaction = accounts_cursor.fetchone()
    return transaction

# Function to add a new transaction for a specific customer
def add_customer_transaction(customer_id, date, description, amount, transaction_type, tags=''):
    table_name = f'customer_{customer_id}'
    accounts_cursor.execute(f'''INSERT INTO {table_name}
                                 (date, description, amount, type, tags)
                                 VALUES (?, ?, ?, ?, ?)''',
                            (date, description, amount, transaction_type, tags))
    accounts_conn.commit()



def update_customer_details(customer_id, name=None, other_details=None):
    query = "UPDATE customers SET "
    updates = []
    if name:
        updates.append("name = '{}'".format(name))
    if other_details:
        updates.append("email = '{}'".format(other_details))
    if not updates:
        return False
    query += ", ".join(updates)
    query += " WHERE id = {}".format(customer_id)
    accounts_cursor.execute(query)
    accounts_conn.commit()
    return True

def delete_customer(customer_id):
    query = "DROP TABLE IF EXISTS customer_{}".format(customer_id)
    accounts_cursor.execute(query)
    query = "DELETE FROM customers WHERE id = {}".format(customer_id)
    accounts_cursor.execute(query)
    accounts_conn.commit()
    return True


def update_customer_transaction(table_name, transaction_id, date, description, amount, transaction_type, tags):
    """
    Update an existing transaction for a customer in the accounts database.
    """
    query = "UPDATE {} SET date=?, description=?, amount=?, type=?, tags=? WHERE id=?".format(table_name)
    values = (date, description, amount, transaction_type, tags, transaction_id)
    accounts_cursor.execute(query, values)
    accounts_conn.commit()

def delete_customer_transaction(customer_id, transaction_id):
    """
    Delete a transaction for a customer from the accounts database.
    """
    query = "DELETE FROM customer_{} WHERE id=?".format(customer_id)
    values = (transaction_id,)
    accounts_cursor.execute(query, values)
    accounts_conn.commit()
    

def get_table(table_name):
    accounts_cursor.execute(f"select * from {table_name}")
    return accounts_cursor.fetchall()