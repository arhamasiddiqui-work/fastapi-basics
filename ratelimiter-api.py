# RateLimiting: api ki limit set krne ke liye, if a user send too many request in 1 min, he will get error

from fastapi import FastAPI, Request
from slowapi import Limiter
from slowapi.util import get_remote_address #user ki ipaddress track krna
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse

app= FastAPI()

# Limiter setup:
limiter= Limiter(key_func=get_remote_address)
app.state.limiter = limiter

# Error handle:
@app.exception_handler(RateLimitExceeded)
def rateLimitExceeded(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={
            "detail": "Too many requests"
        }
    )
# Rate Limiter Api:
@app.get("/data")
@limiter.limit("5/minute")  # 5 req per min  
def getData(request: Request):
    return {
        "message": "Success"
    }
