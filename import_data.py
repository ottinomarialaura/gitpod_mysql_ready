import mysql.connector
import pandas as pd

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
mycursor = mydb.cursor()

#Create the DB (if not already exists)
mycursor.execute("CREATE DATABASE IF NOT EXISTS VOLLEYBALL")

#Create the table for the csv data (if not exists)
mycursor.execute("""
  CREATE TABLE IF NOT EXISTS VOLLEYBALL.volleyball (
    circuit VARCHAR(30) NOT NULL,
    tournament VARCHAR (30),
    country VARCHAR(30),
    year INT(30),
    date VARCHAR(30),
    gender VARCHAR(30),
    w_player1 VARCHAR(30),
    w_p1_birthdate VARCHAR(30),
    w_p1_age VARCHAR(30),
    w_player2 VARCHAR(30),
    w_p2_birthdate VARCHAR(30),
    w_p2_age VARCHAR(30)
  );""")

#Delete data from the table Clsh_Unit
mycursor.execute("DELETE FROM VOLLEYBALL.volleyball")
mydb.commit()

#Read data from a csv file
clash_data = pd.read_csv('./foglio_dati.csv', index_col=False, delimiter = ',')
clash_data = clash_data.fillna('Null')
print(clash_data.head(20))

#Fill the table
for i,row in clash_data.iterrows():
    cursor = mydb.cursor()
    #here %S means string values 
    sql = "INSERT INTO VOLLEYBALL.volleyball VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    #print("Record inserted")
    # the connection is not auto committed by default, so we must commit to save our changes
    mydb.commit()

#Check if the table has been filled
mycursor.execute("SELECT * FROM VOLLEYBALL.volleyball")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)