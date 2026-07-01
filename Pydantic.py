# Pydantic: schema structure, define what data format should be,validation

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str  # schema
    age: int
    email: str


@app.post("/create-user")
def create_User(user: User):
    return {"message": "User created", "data": user}


# Nested data:
class Address(BaseModel):
    city: str
    pincode: int


class Citizen(BaseModel):
    name: str
    age: int
    address: Address


@app.post("/create-citizen")
def create_Citizen(citizen: Citizen):
    return {"message": "Citizen created", "data": citizen}
