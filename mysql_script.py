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

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)
mydb.commit()