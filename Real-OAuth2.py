# OAUTH2 + JWT: authorization framework, real authentication, fully secured api, token based authorization 

from fastapi import FastAPI, HTTPException, Depends
from jose import jwt    # json data ko encrypt/secret code me krta hai
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext

app = FastAPI()

# jwt config:
SECRET_KEY="mytoken"
ALGORITHM="HS256"   
ACCESS_TOKEN_EXPIRE_MINUTE= 30    

# password hashing:
pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

# OAuth setup:
oauth2_schema= OAuth2PasswordBearer(tokenUrl="/login")
 
# Dummy user DB
fake_user_db={
    "admin":{
        "username":"admin",
        "hashed_password":pwd_context.hash("1234")
    }
}
# Hash password
def hash_password(password:str):
    return pwd_context.hash(password)

# Verify password
def verify_password(normal_password,hashed_password):
    return pwd_context.verify(normal_password,hashed_password)


# create token
def createToken(data:dict):
    to_encode=data.copy()
    expire= datetime.now(timezone.utc) + timedelta(minutes=30)  # token expire in 30 min
    to_encode.update({
            "exp": expire
        })
    token=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return token

# Login API (OAuth2 form + Token Generate)
@app.post("/login")
def login(form_data:OAuth2PasswordRequestForm=Depends()):
    user= fake_user_db.get(form_data.username)
    if not user or not verify_password(form_data.password,user["hashed_password"]):
        raise HTTPException(
            status_code=400,
            detail="Invalid username or password"
        )
    access_token=createToken({
        "user":form_data.username
    })
    return{
        "access_token":access_token,
        "token_type":"bearer"   # req header m extract krenge(bearer)
    }

# Verify Token
def VerifyToken(token:str=Depends(oauth2_schema)):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired Token"
        )

# Protected Route   
@app.get("/protected")
def protected(username:str=Depends(VerifyToken)):
    return{
        "message":"Protected Route",
        "user":username
    }