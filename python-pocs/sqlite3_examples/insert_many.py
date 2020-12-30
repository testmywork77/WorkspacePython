# Insert records in to SQLite3 Database Table
import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Customers List
customerList = [
    ('fname4', 'lname4', 'name4@gmail.com'),
    ('fname5', 'lname5', 'name5@gmail.com'),
    ('fname6', 'lname6', 'name6@gmail.com'),
]

# Insert a record
c.executemany("INSERT INTO Customers VALUES (?, ?, ?)", customerList)
print('Command executed succesfully...')

# Commit command
conn.commit()

# Close connection
conn.close()

