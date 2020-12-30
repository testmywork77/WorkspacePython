import sqlite3

conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Query the customers table
c.execute('SELECT rowid, * FROM Customers')

# Fetch all records
print('Fetch all reords:')
print(c.fetchall())

print('Commands executed successfuly')

# Commit command
conn.commit()

# Close connection
conn.close()
