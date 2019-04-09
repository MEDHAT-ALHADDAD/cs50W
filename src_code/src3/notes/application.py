from flask import Flask, session, redirect, url_for, escape, request,render_template
from flask_session import Session

app = Flask(__name__)
app.secret_key = "medhat"

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

notes = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)
    return render_template("index.html", notes=notes, session=session)
