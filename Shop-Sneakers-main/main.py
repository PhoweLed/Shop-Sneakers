from flask import Flask, flash, redirect,render_template, request, session, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = "iy6w8egiudk"

@app.route("/")
def index():
    if "user" in session:
        return render_template('main.html')
    else:
        flash("ти не увійшов")
        return redirect(url_for("login"))

@app.route("/login")
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?",(username,password))
        user_data = cursor.fetchone()
        print(user_data)
        conn.close()
        if user_data:
            session["user"] = username
            flash("Вхід успішний","success")
            return redirect("/")
        else:
            flash("неправильний логін або пароль","error")
            return redirect('/login')
        
    return render_template("login.html")

@app.route("/register")
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username,password) VALUE (?,?)", (username,password))
            conn.commit()
            conn.close()
            flash("реєстрація успішна ","success")
            return redirect("/login")
        except sqlite3.IntegrityError:
            flash("Користувач із таким іменем вже існує","error")
            return redirect("/regiter")

    return render_template('register.html')


@app.route('/add', methods=['post','get'])

def add():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        conn = sqlite3.connect('sneakers.db')
        cursor = conn.cursor()
        try:
            cursor.execute
        ("INSERT INTO sneakers (name, price) VALUES (?,?)", (name, price))
        conn.commit()
        conn.close()

        
        except KeyError as e:
            flash(f"Помилка: Відсутнє поле {e}", "error")
        except sqlite3.Error as e:
            flash(f"Помилка бази даних: {e}", "error")
        except Exception as e:
            flash(f"Сталася помилка: {e}", "error")

app.run()