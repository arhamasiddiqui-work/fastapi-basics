#  Testing API: if our api has some bug,issues we can test api via Pytest + fastapi

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def Home():
    return {"message": "Testing API"}


@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}
