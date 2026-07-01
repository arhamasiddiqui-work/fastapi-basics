# Response Model: what to show to client and what to hide
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):  # will hide this
    name: str
    age: int
    password: int


class UserResponse(BaseModel):  # will show this only
    name: str
    age: int


@app.get("/users", response_model=UserResponse)
def getUser():
    return {"name": "John", "age": 20, "password": "1234"}


# Status Code & Response Model:


@app.post("/create-users", status_code=status.HTTP_201_CREATED)
def createUser():
    return {"message": "User created"}


@app.get("/users")  # custom response
def getUsers():
    return {
        "status": "success",
        "message": "User fetched",
        "data": {
            "name": "John",
        },
    }


@app.get("/users/{user_id}")  # Error Handling
def getUser(user_id: int):
    if user_id != 1:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": 1, "name": "John"}
