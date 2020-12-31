import sqlite3

conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

rowid=1
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
