import sqlite3

# Query the database and return all the records
def get_customer_all():
    # Connect to database
    conn = sqlite3.connect("customer.db")

    # Create a cursor
    c = conn.cursor()

    # Query all customers
    c.execute("SELECT rowid,* FROM Customers")
    customers = c.fetchall()

    for customer in customers:
        print(customer)

    # Close connection
    conn.close()

def add_customer(first_name, last_name, email):
    # Connect to database
    conn = sqlite3.connect('customer.db')

    # Create a cursor
    c = conn.cursor()

    # Insert a record
    c.execute("INSERT INTO Customers VALUES (?, ?, ?)", (first_name,last_name,email))

    # Commit command
    conn.commit()
    
    # Close connection
    conn.close()

def add_customers(customerList):
    # Connect to database
    conn = sqlite3.connect('customer.db')

    # Create a cursor
    c = conn.cursor()

    # Insert a record
    c.executemany("INSERT INTO Customers VALUES (?, ?, ?)", (customerList))

    # Commit command
    conn.commit()
    
    # Close connection
    conn.close()

def delete_customer(rowid):
    # Connect to database
    conn = sqlite3.connect('customer.db')

    # Create a cursor
    c = conn.cursor()
   
    # Insert a record
    c.execute("DELETE FROM Customers WHERE rowid = (?)", rowid)
    # Commit command
    conn.commit()

    # Close connection
    conn.close()

def update_customer(rowid):
    # Connect to database
    conn = sqlite3.connect('customer.db')

    # Create a cursor
    c = conn.cursor()
    
    # Query the customer before update
    c.execute(f"SELECT rowid, * FROM Customers WHERE rowid = {rowid}")
    # Fetch record
    print(c.fetchone())

    # Update last_name for #1st reord
    c.execute(f"Update customers SET last_name = 'lname1' WHERE rowid = {rowid}")

    # Commit command
    conn.commit()

    # Query the customer after update
    c.execute(f"SELECT rowid, * FROM Customers WHERE rowid = {rowid}")
    # Fetch record
    print(c.fetchone())

    print('Commands executed successfuly')

    # Close connection
    conn.close()

def email_lookup(email):
    # Connect to database
    conn = sqlite3.connect('customer.db')

    # Create a cursor
    c = conn.cursor()
    
    # Query the customer before update
    c.execute("SELECT rowid, * FROM Customers WHERE email = (?)", (email,))
    # Fetch record
    print(c.fetchone())

    # Close connection
    conn.close()