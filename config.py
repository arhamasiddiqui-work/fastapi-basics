import os
from dotenv import load_dotenv

load_dotenv()    # reading .env file by this function

class Settings:
    origins=os.getenv("ORIGINS") 
    SECRET_KEY=os.getenv("SECRET_KEY")
    DB_URL=os.getenv("DB_URL")

settings=Settings()    