# Handling Error/Exception
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/users/{user_id}")        # HTTP Exception(built-in)
def getUser(user_id:int):
    if user_id !=1:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return{
        "id":1,
        "name":"Arhama"
    }


class UserNotFound(Exception):      # custom exception (we make it)
    def __init__(self,name:str):
        self.name=name
@app.get("/user/{name}")       
def getUser(name:str):
    if name != "Arhama":
        raise UserNotFound(name)
    return{
        "name":name
    }

    
class UserNotFound(Exception):   # Global error handling, used for advance error handling (code clean rahe)
    def __init__(self,name:str):
        self.name=name
@app.exception_handler(UserNotFound)
def userNotFound(request:Request,exc:UserNotFound):
    return JSONResponse(
        status_code=404,
        content={
            "status":"error",
            "message":f"User {exc.name} not found"
        }
    )
@app.get("/user/{name}")       
def getUser(name:str):
    if name != "Arhama":
        raise UserNotFound(name)
    return{
        "name":name
    } 