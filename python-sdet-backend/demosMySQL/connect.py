from utilities.configurations import *


# Create connection object
conn = getConnection()
# Check connection status
print(conn.is_connected())
