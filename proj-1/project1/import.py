import csv
import os

from flask import Flask, session
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
    # db.execute("CREATE TABLE books1(isbn VARCHAR ,title VARCHAR ,author VARCHAR ,year  INTEGER )")
    # db.commit()
    # ########################################################################
    # file = open("books.csv")
    # books = csv.reader(file)
    # for isbn, title, auther, year in books:
    #     db.execute("INSERT INTO books(isbn, title, author, year) VALUES(:isbn, :title, :author, :year)",
    #     {"isbn": isbn, "title": title, "author": auther, "year": year})
    # db.commit()
    #########################################################################################################
    db.execute("CREATE TABLE users(id SERIAL PRIMARY KEY,username VARCHAR NOT NULL,email VARCHAR NOT NULL,password  VARCHAR NOT NULL)")
    #######################################################################################################################
    db.execute("CREATE TABLE reviews(username VARCHAR NOT NULL, rating INTEGER NOT NULL, comment VARCHAR NOT NULL, book_id VARCHAR REFERENCES books, user_id INTEGER REFERENCES users)")
    db.commit()

if __name__ == '__main__':
    main()
