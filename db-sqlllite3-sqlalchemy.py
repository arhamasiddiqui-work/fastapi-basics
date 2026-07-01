# Database Integration : working with databases, connecting to database, saves data in fileformat

# SQLite =used for small application, built-in library,sqlite3 uses query makes code messy, if we want to write our own sql use sqllite3
import sqlite3
from fastapi import FastAPI

app = FastAPI()

connect = sqlite3.connect("test.db", check_same_thread=False)

cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    title TEXT,
    completed TEXT
    )
""")

connect.commit()


@app.get("/")
def Home():
    return {"message": "SQLITE connected fine"}


# SQLALCHEMY =large applications, ORM (Object Relational Model,python to handle database), sqlalchemy, sqllite3 ka hi ORM hai and uses python code to make code clean and make easy query, install library, if we want python to handle our database use sqlachemy

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from fastapi import FastAPI, Depends

app = FastAPI()

# Database URL
DATABASE_URL = "sqlite:///./test.db"

# create_engine:method to connect to database,
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# sessionmaker:method to create a database operation
sessionLocal = sessionmaker(bind=engine)

# declarative_base:method to create a base for our models
Base = declarative_base()


class Task(Base):  # creating model/table
    __tablename__ = "tasks"  # table name

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    completed = Column(String)


# create_all:method to create tables in database
Base.metadata.create_all(bind=engine)


def get_db():
    db = sessionLocal()  # create a new session
    try:
        yield db
    finally:
        db.close()  # close the session


@app.get("/")
def Home(db: Session = Depends(get_db)):
    return {"message": "DB Connected Fine"}
