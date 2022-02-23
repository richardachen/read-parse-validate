import mysql.connector

# connection string
cnx = mysql.connector.connect(user='root', 
    password='twin629DUKE', 
    host = '127.0.0.1',
    database = 'Farm',
    auth_plugin = 'mysql_native_password')

# query block
cursor = cnx.cursor()
query = ("INSERT INTO `Customers` VALUES ('bob', 'hertz', 'bob@mit.edu')")
cursor.execute(query)

# loop through data
for row in cursor.fetchall():
    print(row)

# clean up
cnx.commit()
cursor.close()
cnx.close()