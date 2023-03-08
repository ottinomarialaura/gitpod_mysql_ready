import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="animali"
)

mycursor = mydb.cursor()

sql = "INSERT INTO mammiferi (id, name_proprio, razza, peso, eta) VALUES (%s, %s, %s, %s, %s)"
val =[
 ("2", "gatto", "certosino", "5", "15"),
 ("3", "cane", "barboncino", "3", "11"),
 ("4", "topo", "grigio", "1", "1"),
 ("5", "giraffa", "africana", "300", "2"),
 ("1", "elefante", "indiano", "600", "4")
]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
