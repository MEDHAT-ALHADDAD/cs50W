import csv
import os
import requests

from flask import Flask, session, render_template, request, redirect, url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
# if not os.getenv("postgres://kzspkcgxwfgggz:212c3e5a75ca861906aa77eaa081aa9f9a753365ff1db2a6d284631e6e012668@ec2-54-227-240-7.compute-1.amazonaws.com:5432/detdsknm9rtht6"):
#     raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# Set up database
engine = create_engine("postgres://kzspkcgxwfgggz:212c3e5a75ca861906aa77eaa081aa9f9a753365ff1db2a6d284631e6e012668@ec2-54-227-240-7.compute-1.amazonaws.com:5432/detdsknm9rtht6")
db = scoped_session(sessionmaker(bind=engine))


@app.route('/')
def index():
    if 'username' in session:
        return render_template("/index.html")
    return render_template("/login.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route('/search', methods=['GET', 'POST'])
def search():
    bookslist = []
    name = request.form.get("note")
    name = "%" + name + "%"
    books = db.execute("SELECT * FROM books WHERE (isbn LIKE :name  OR title LIKE :name OR author LIKE :name) ", {"name": name}).fetchall()
    bookslist.append(books)
    return render_template("/search.html", books=bookslist)


@app.route('/<string:id>')
def name(id):
    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "xtJTyQRefMPz4Wf5iCKqQ", "isbns": id})
    res1=res.json()
    return render_template("name.html", name=res1, username=session.get('username'))


@app.route('/signup_success', methods=['POST'])
def signup_success():
    username=request.form.get("username")
    email=request.form.get("email")
    password=request.form.get("password")
    emailcount= db.execute("SELECT * FROM users WHERE email = :email",{"email": email}).fetchone()
    db.commit()
    if emailcount is None:
        # user={"username":username,"email":email,"password":password}
        db.execute("INSERT INTO users (username, email, password) VALUES (:username, :email, :password)",
            {"username": username, "email": email, "password": password})
        db.commit()
    else:
        return render_template("/signup_success.html",massage="already exist")
    return render_template("/signup_success.html",massage="success")


@app.route('/name/<string:book_id>/<int:user_id>/<string:username>', methods=['POST'])
def review(book_id,user_id,username):
    # username=request.form.get("username")
    rating=request.form.get("rating")
    comment=request.form.get("comment")
    db.execute("INSERT INTO reviews (username, rating, comment, book_id, user_id) VALUES (:username, :rating, :comment, :book_id, :user_id)",
            {"username": username, "rating": rating, "comment": comment, "book_id": book_id, "user_id": user_id})
    db.commit()
    return redirect(url_for('name',id=book_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        emailcount= db.execute("SELECT * FROM users WHERE username = :username AND password = :password",{"username": username, "password": password}).fetchone()
        db.commit()
        if emailcount is None:
            return redirect(url_for('login'))
        session['username'] = {"id": emailcount.id , "username": emailcount.username}
        return redirect(url_for('index'))
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))
