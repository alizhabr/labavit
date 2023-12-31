import psycopg2
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
conn = psycopg2.connect(database="service_db",
user="postgres",
password="356qwedf",
host="localhost",
port="5432")


cursor = conn.cursor()
@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')

@app.route('/login/', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        if request.form.get("login"):
            username=request.form.get("username")
            password=request.form.get("password")
            if username=="" or password=="":
                return render_template("login.html",alert="no login or password")
            cursor.execute("SELECT * FROM service.users WHERE login=%s", (str(username),))
            records = list(cursor.fetchall())
            if len(records)==0:
                return render_template("login.html",alert="no user")
            cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username), str(password)))
            records = list(cursor.fetchall())
            if len(records)==0:
                return render_template("login.html", alert="wrong password")
            return render_template('account.html', full_name=records[0][1],login=username,password=password)
        elif request.form.get("registration"):
            return redirect("/registration/")
    return render_template("login.html")
@app.route('/registration/', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        name = request.form.get('name')
        login = request.form.get('login')
        password = request.form.get('password')
        if len(name) > 0 and len(password) > 0 and len(login) > 0:
            cursor.execute("SELECT * FROM service.users WHERE login=%s", (str(login),))
            if len(cursor.fetchall()) == 0:
                cursor.execute('INSERT INTO service.users (full_name, login, password) VALUES(%s, %s, %s);',
                               (str(name), str(login), str(password)))
                conn.commit()
                return redirect('/login/')
            else:
                return render_template('registration.html', alert="This user exists")
        else:
            return render_template('registration.html', alert="Enter name,login and password")
    return render_template('registration.html')
