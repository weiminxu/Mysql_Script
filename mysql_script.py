import mysql.connector  #python -m pip install mysql-connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="123456",
    database="mysql_script")

#auth_plugin="mysql_native_password"

print(mydb)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE mysql_script")

#mycursor.execute("CREATE TABLE customers(name VARCHAR(255), address VARCHAR(255))")

#sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
#val = ("John", "Highway 21")
#mycursor.execute(sql, val)

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#     ("Peter", "Low street 4"),
#     ("Amy", "Apple street 652"),
#     ("Hannah", "Mountain 21"),
#     ("Michael", "Valley 345"),
#     ("Sandy", "Ocean blvd 2"),
#     ("Betty", "Green Grass 1"),
#     ("Richard", "Sky st 331"),
#     ('Susan', 'One way 98'),
#     ('Vicky', 'Yellow Garden 2'),
#     ('Ben', 'Park Lane 38'),
#     ('William', 'Central st 954'),
#     ('Chuck', 'Main Road 989'),
#     ('Viola', 'Sideway 1633')
# ]
# mycursor.executemany(sql, val)
# mydb.commit()

# mycursor.execute("SELECT * FROM customers")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# sql = "SELECT * FROM customers WHERE address = 'Park Lane 38'"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# sql = "SELECT * FROM customers ORDER BY name"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
mycursor.execute(sql)
mydb.commit()