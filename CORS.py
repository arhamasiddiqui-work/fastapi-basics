#  CORS (Cross-Origin Resource Sharing) is a security mechanism that controls whether a web page can access resources from a different domain (origin), connecting frontend and backend

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#  Allow origin (FRONT-END URL)
origin = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,  # allowed FE
    allow_credentials=True,
    allow_methods=["*"],  # allowed get,post,put,delete
    allow_headers=["*"],
)


@app.get("/")
def Home():
    return {"message": "CORS enable API"}
