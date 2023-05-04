from flask import render_template
from flask import Flask
import mysql.connector

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="VOLLEYBALL"
)
mycursor = mydb.cursor()
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('hello.html', name='Maria Laura')


@app.route('/units')
def unitList():
    mycursor.execute("SELECT * FROM volleyball")
    myresult=mycursor.fetchall()
    return render_template('volleyball.html',units=myresult)
