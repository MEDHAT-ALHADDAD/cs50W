import datetime
from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)


app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/", methods=["GET", "POST"])
def index():
    if session.get("notes") is None:
        session["notes"] = []
    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)

    return render_template("index.html", notes=session["notes"])

###################################################################

# @app.route('/')
# def index():
#     return render_template("index.html")


# @app.route('/hello', methods=["post", "get"])
# def hello():
#     name = request.form.get("name")
#     return render_template("hello.html", name=name)


##################################################################

# @app.route("/")
# def index():
#     return render_template("index.html")


# @app.route("/more")
# def more():
#     return render_template("more.html")


##############################################################

# @app.route('/')
# def index():
#     names = ["alice", "bob", "charlie", "medhat"]
#     return render_template("index.html", names=names)

###################################################################

# @app.route('/')
# def index():
#     now = datetime.datetime.now()
#     new_year = now.month == 1 and now.day == 1
#     return render_template("index.html", new_year=new_year)

###############################################################

# @app.route("/")
# def index():
#     headline = "hello!"
#     return render_template("index.html", headlines=headline)


# @app.route('/bye')
# def bye():
#     headline = "good bye"
#     return render_template("index.html", headlines=headline)

################################################################

# @app.route("/")
# def method_name():
#     return 'hello, flask!!!'


# @app.route("/david")
# def david():
#     return "hello, david!"


# @app.route("/<string:name>")
# def hello(name):
#     name = name.capitalize()
#     return f"<h1>Hello, {name}!</h1>"
