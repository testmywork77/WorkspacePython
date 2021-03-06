from utilities.configurations import *


# Create connection object
conn = getConnection()
print(conn.is_connected())
cursor = conn.cursor()

# Update record in a Table -By hard coding query parameters
# query = "UPDATE customerInfo SET Location = 'UK' WHERE CourseName = 'Jmeter'"

# Update record in a Table - By dynamic query parameters/variables
query = "UPDATE customerInfo SET Location = %s WHERE CourseName = %s"
parameterData = ("US", "Jmeter")
cursor.execute(query, parameterData)
conn.commit()

# Fetch all records
cursor.execute('select * from customerInfo')
rows = cursor.fetchall()  # returns multiple records, means list of tuple(s) in python terminology
print(rows)
conn.close()
