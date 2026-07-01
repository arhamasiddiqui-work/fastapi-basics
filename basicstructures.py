from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#   GET request: fetching data, work on browser


@app.get("/")  # send our data so user can read/get it
def home():
    return {"message": "Welcome to fast-api basics"}


# Path parameter : /users/1, e.g:specific id
@app.get("/users/{user_id}")
def get_users(user_id: int):
    return {"user_id": user_id}


# Query parameter   /users?name=John, e.g: searching,filtering price,etc
@app.get("/users")
def get_users(name: str = None):  # null value
    return {"Name": name}


@app.get("/products")
def get_products(limit: int = 10):  # default value
    return {"limit": limit}


@app.get("/items")
def get_items(items: str = None, price: int = 0):  # default & null value
    return {"items": items, "price": price}


# POST request: creating data, work on swagger


class User(BaseModel):  # pydantic->validation, dict->no validation
    name: str
    age: int


@app.post("/create-user")
def createUser(user: User):
    return {"message": "User created", "data": user}  # pass value
