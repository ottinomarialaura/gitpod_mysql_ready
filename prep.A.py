import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE animali")
mycursor.execute("CREATE TABLE customers (ID INT(50), name_proprio VARCHAR(255), razza VARCHAR(255), peso INT(10), eta INT(5))")
