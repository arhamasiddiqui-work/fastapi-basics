#  Authentication:  user ko verify krna, less secured
#  JWP(json web token): user login, server verify user, if valid-> server send token, user save token, user send token with every request, server verify token, valid -> send data,invalid -> 401 Unauthorized

from fastapi import FastAPI, HTTPException, Depends, Header
from jose import jwt  # json data ko encrypt/secret code me krta hai
from datetime import datetime, timedelta, timezone

app = FastAPI()

# make a secure key for token:
SECRET_KEY = "mytoken"

# encryption algorithm
ALGORITHM = "HS256"


# create token
def createToken(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=30
    )  # token expire in 30 min
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return token


# Login API (Token Generate)
@app.post("/login")
def login(username: str, password: str):
    if username != "Admin" or password != "1234":
        raise HTTPException(status_code=401, detail="Invalid Username and Passowrd")
    token = createToken({"user": username})
    return {"access_token": token}


# Verify Token
def verifyToken(token: str = Header(None)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(status_code=401, detail="Invalid or expired Token")


# Protected API(after verification access to api)
@app.get("/secure")
def secureData(user=Depends(verifyToken)):
    return {"message": "Secure Data Accessed", "user": user}
