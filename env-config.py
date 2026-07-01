#  Environment Variable(.env file): A saved URL that CORS allows, if we make a secretkey we don't want everyone to access it thats why we use environment variable(.env->don't send data on github OR config file->large application)


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import settings


app= FastAPI()

# Allow origin (FRONT-END URL)
origins=settings.origins      # using Settings from config

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # allowed FE
    allow_credentials=True,
    allow_methods=["*"],        # allowed get,post,put,delete
    allow_headers=["*"]         
    )

@app.get("/")
def Home():
    return{
        "message":"CORS enable API"
    }