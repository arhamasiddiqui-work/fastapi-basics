# Async programming: multiple tasks can run in parallel.

import time  # time a function to use sleep() method
import asyncio  # asyncio a function to use async/await syntax.
from fastapi import FastAPI

app = FastAPI()

# #SYNC WAY: not preferred
# def task1():
#     time.sleep(3)
#     return "Task 1 completed"


# ASYNC WAY: mostly preferred
@app.get("/")
async def home():
    await asyncio.sleep(3)  # reload in 3 seconds
    return {"message": "Async API"}
