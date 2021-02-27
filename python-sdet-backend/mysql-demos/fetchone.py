import mysql.connector
# host, database, user, password
conn = mysql.connector.connect(host='localhost', database='PythonAutomation', user='root', password='root')
print(conn.is_connected())
cursor = conn.cursor()
cursor.execute('select * from customerInfo')
row = cursor.fetchone()  # returns single record, means tuple in python terminology
print(type(row))  # tuple i.e. <class 'tuple'>
print(row)
print(row[3])  # tuple use index to retrieve data
