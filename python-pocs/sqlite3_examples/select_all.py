# Query(Select) all the SQLLite3 Database Table
import sqlite3

conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Query the customers table
c.execute('SELECT * FROM Customers')

customerTupleList = c.fetchall()
print(f"Name      " + "\t\tEmail" )
print(f"----------" + "\t\t-----" )
for customerTuple in customerTupleList:
    print(f"{customerTuple[0]} {customerTuple[1]}     {customerTuple[2]}")

print('Commands executed successfuly')

# Commit command
conn.commit()

# Close connection
conn.close()