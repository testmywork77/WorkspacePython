from utilities.configurations import *


# Create connection object
conn = getConnection()
print(conn.is_connected())
cursor = conn.cursor()
cursor.execute('select * from customerInfo')
rows = cursor.fetchall()  # returns multiple records, means list of tuple(s) in python terminology
print(rows)
print(type(rows))  # list of tuples i.e. <class 'list'>
