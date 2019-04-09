import csv
import os

from flask import Flask, session, render_template, request
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

# Set up database
engine = create_engine("postgres://kzspkcgxwfgggz:212c3e5a75ca861906aa77eaa081aa9f9a753365ff1db2a6d284631e6e012668@ec2-54-227-240-7.compute-1.amazonaws.com:5432/detdsknm9rtht6")
db = scoped_session(sessionmaker(bind=engine))


def main():
    name = "%"+"Krondor"+"%"
    books = db.execute("SELECT * FROM books WHERE (isbn LIKE :name  OR title LIKE :name OR author LIKE :name) ", {"name": name}).fetchall()
    for book in books:
        print(book)


if __name__ == '__main__':
    main()
