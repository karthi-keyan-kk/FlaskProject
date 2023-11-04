from flask import Flask, render_template, request, redirect
import pymysql as pms

app = Flask(__name__)

def sqlConnector():
    conn = pms.connect(user='root', password='@karthiKeyan1234', db='karthikeyan', host='localhost')
    c = conn.cursor()
    return conn, c

def user_details():
    conn, c = sqlConnector()
    c.execute("SELECT * FROM users")
    data = c.fetchall()
    conn.commit()
    conn.close()
    c.close()
    return data

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/user-details')
def details():
    data = user_details()
    return render_template("details.html", details=data)

@app.route('/new-user', methods=['GET','POST'])
def user():
    if request.method == 'POST':

        id = request.form.get('IdNo')
        name = request.form.get('Name')
        email = request.form.get('email')
        role = request.form.get('role')

        conn, c = sqlConnector()
        c.execute("INSERT INTO users VALUES ({}, '{}', '{}', '{}')".format(int(id), name, email, role))
        conn.commit()
        conn.close()
        c.close()

    return render_template("user.html")

@app.route('/user-details/<int:id>')
def get_user(id):
    conn, c = sqlConnector()
    c.execute("SELECT * FROM users WHERE id={}".format(int(id)))
    data = c.fetchall()
    conn.commit()
    conn.close()
    c.close()
    return render_template("details.html", details=data)

@app.route('/delete_user/<int:id>')
def delete_user(id):
    conn, c = sqlConnector()
    user = "SELECT count(*) FROM users WHERE id={}".format(int(id))
    a = c.execute(user)
    if a > 0:
        query = "DELETE FROM users WHERE id={}".format(int(id))
        c.execute(query)
        conn.commit()
        conn.close()
        c.close()
        data = user_details()
        return render_template("details.html", details=data)
    else:
        "User not found"

@app.route('/update_user/<int:id>')
def update_user(id):
    conn, c = sqlConnector()
    query = "SELECT * FROM users WHERE id={}".format(int(id))
    c.execute(query)
    data = c.fetchall()
    conn.commit()
    conn.close()
    c.close()
    return render_template("update_user.html", details=data)

@app.route('/update_user/<int:id>', methods=["GET", "POST"])
def updating(id):
    if request.method == "POST":
        id = request.form.get('IdNo')
        name = request.form.get('Name')
        email = request.form.get('email')
        role = request.form.get('role')
        query = "UPDATE users SET name='{}', email='{}', role='{}' WHERE id={}".format(name, email, role, int(id))
        conn, c = sqlConnector()
        c.execute(query)
        conn.commit()
        conn.close()
        c.close()
    data = user_details()
    return render_template("details.html", details=data)


if __name__ == "__main__":
    app.run(debug=True)