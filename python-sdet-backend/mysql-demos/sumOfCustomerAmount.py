from utilities.configurations import *


# Create connection object
conn = getConnection()
print(conn.is_connected())
cursor = conn.cursor()
cursor.execute('select * from customerInfo')
rows = cursor.fetchall()  # returns multiple records, means list of tuple(s) in python terminology
amount = 0
# Iterate the List
for row in rows:
    # print(row[2])
    amount = amount + row[2]
print(amount)

conn.close()



