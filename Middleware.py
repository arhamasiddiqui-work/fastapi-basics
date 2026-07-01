# Middleware: request aur response ke beech me rehta h, global level pe request aur response ko modify kar sakta h, jaise logging, authentication, etc.


from fastapi import FastAPI, Request, HTTPException
import time


app = FastAPI()


@app.middleware("http")
async def my_midware(
    request: Request, call_next
):  # call_next is a function jo request ko agle middleware ya route handler tak bhejta h and response ko wapas laata h
    print("Thinking ")

    if request.url.path == "/protect":
        # somechecks get false value
        raise HTTPException(status_code=418, detail="Access Denied")

    response = await call_next(request)
    print("response send")
    return response


@app.middleware("http")
async def my_midware(
    request: Request, call_next
):  # call_next is a function jo request ko agle middleware ya route handler tak bhejta h and response ko wapas laata h
    print("Request received")

    response = await call_next(request)
    print("response send")
    return response


# e.g, logging middleware:
@app.middleware("http")
async def log_middleware(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time
    print(f"Path:{request.url.path} | Time:{process_time}")
    return response


@app.get("/")
def someWath():
    return {"message": "Hello World"}


@app.get("/protect")
def someWath():
    return {"message": "Protect World"}
