from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

notes = []

@app.route("/<string:name>", methods=["GET", "POST"])
def index(name):
    # if request.method == "POST":
    #     note = request.form.get("note")
    #     notes.append(note)
    # elif request.method == "GET":
    notes=name
    return render_template("index.html", notes=notes)
