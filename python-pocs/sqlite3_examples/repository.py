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

def delete_customer(id):
    # Connect to database
    conn = sqlite3.connect('customer.db')

    # Create a cursor
    c = conn.cursor()
   
    # Insert a record
    c.execute("DELETE FROM Customers WHERE rowid = (?)", id)
    # Commit command
    conn.commit()

    # Close connection
    conn.close()

