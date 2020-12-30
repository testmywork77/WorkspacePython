# Insert record in to SQLite3 Database Table
import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Insert a record
c.execute("INSERT INTO Customers VALUES ('fname3', 'lname3', 'name3@gmail.com')")

# Commit command
conn.commit()

# Close connection
conn.close()
