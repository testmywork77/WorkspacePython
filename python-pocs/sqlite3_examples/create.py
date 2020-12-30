import sqlite3

# conn = sqlite3.connect(':memory:')

# Connect to database
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Data Types -NULL, INTEGER, REAL, TEXT,BLOB
# Create a Table
c.execute("""
        CREATE TABLE Customers (            
            first_name text,
            last_name text,
            email text
        )
        """)

# Commit command
conn.commit()

# Close connection
conn.close()

