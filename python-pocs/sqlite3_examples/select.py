import sqlite3

conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Query the customers table
c.execute('SELECT * FROM Customers')

# Fetch 1st record
# print('Fetch 1st reord:')
# print(c.fetchone())

# # Fetch first n records
# print('Fetch first n records:')
# print(c.fetchmany(3))

# Fetch all records
print('Fetch all reords:')
print(c.fetchall())

print('Commands executed successfuly')

# Commit command
conn.commit()

# Close connection
conn.close()
