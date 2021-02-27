import mysql.connector
# host, database, user, password
conn = mysql.connector.connect(host='localhost', database='PythonAutomation', user='root', password='root')
print(conn.is_connected())
cursor = conn.cursor()
cursor.execute('select * from customerInfo')
rows = cursor.fetchall()  # returns multiple records, means list of tuple(s) in python terminology
print(rows)
print(type(rows))  # list of tuples i.e. <class 'list'>
