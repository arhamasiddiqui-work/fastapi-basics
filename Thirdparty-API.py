#  API integration: third party api se data lena and return data by fastapi
# external api data: return the data we want from third party api

from fastapi import FastAPI, HTTPException
import requests  # httpRequest send krne ke liye

app = FastAPI()


#  Get all data:
@app.get("/posts")
def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    return response.json()


#  Get single data:
@app.get("/posts/{id}")
def get_post(id: int):
    url = f"https://jsonplaceholder.typicode.com/posts/{id}"
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Post not found")
    return response.json()
