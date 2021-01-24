# Insert record in to SQLite3 Database Table
import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

rowid = 5
# Insert a record
c.execute(f"DELETE FROM Customers WHERE rowid = {rowid}")

# Query the customers table
c.execute('SELECT rowid, * FROM Customers')

customerTupleList = c.fetchall()
print(f"RowId  " + "Name        " + "\t\tEmail" )
print(f"------ " + "------------" + "\t\t-----" )
for customerTuple in customerTupleList:
    print(f"{customerTuple[0]}      {customerTuple[1]} {customerTuple[2]}            {customerTuple[3]}")

print('Commands executed successfuly')

# Commit command
conn.commit()

# Close connection
conn.close()
