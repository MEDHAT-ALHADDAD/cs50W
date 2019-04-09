import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

engine =create_engine("postgres://postgres:ahmed15315@localhost:5432/lec-3")
db = scoped_session(sessionmaker(bind=engine))


def main():
    flights =db.execute("SELECT * FROM flights").fetchall()
    for flight in flights:
        print(flight)






if __name__ == '__main__':
    main()
    