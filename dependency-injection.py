# Dependency Injection:  design pattern, isme hum aik function ko dosre function me inject karte hain, isse code reusability barhti hai, dependency per route hota h

from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()


# user example:
def get_user():
    return {"user": "Guest"}


@app.get("/profile")
def profile(user=Depends(get_user)):  # Depends() is used to call the func
    return user


@app.get("/dashboard")
def dashboard(user=Depends(get_user)):
    return user


# auth example:(token based, we send token in Header for security, if wrong token then error)
def verify_token(token: str = Header(None)):
    if token != "mysecrettoken":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"user": "Authorized User"}


@app.get("/secure")
def secure_data(user=Depends(verify_token)):
    return {"message": "This is secure data", "user": user}
