from flask import Flask, render_template, request, session, redirect, url_for
from idlelib.query import Query
from select import select

import pymysql
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='Shakthi@2004',
    database='flasdb',
    port=3306
)
cursor = connection.cursor()

app = Flask(__name__)
app.secret_key = "secret key"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/home')
def home():
    return  render_template('home.html',username = session['username'])


@app.route('/login', methods=['GET', 'POST'])
def login():
    msg=' '
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        cursor.execute('SELECT * FROM user WHERE username=%s AND password=%s',(username,password))
        record = cursor.fetchone()
    if record:
        if record:
            session['loggedin'] = True
            session['username'] = record[1]
            return redirect(url_for('home'))
        else:
            msg = ('Incorrect username/password. Try again!')
    return render_template('index.html',msg=msg)

@app.route('/Webdeveloper')
def wb():
    cursor.execute("select * from e_detail where ROLL = 'Webdeveloper' ")
    Data = cursor.fetchall()
    return render_template("personal_details.html",data = Data,name = "Webdeveloper" )

if __name__ == '__main__':
    app.run(debug=True)
