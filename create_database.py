import mysql.connector  #python -m pip install mysql-connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="123456")

#auth_plugin="mysql_native_password"

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE MySQLScript")

