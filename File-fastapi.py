#  File upload & static file(server se frontend par file bhejna) in FastAPI:

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.staticfiles import StaticFiles
import os
import shutil   # used for file operation

app = FastAPI()

#1- Ensure uploads folder exist
UPLOAD_DIR="uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# 2- Upload file url path/ Static file
app.mount("/files",StaticFiles(directory=UPLOAD_DIR),name="files")

# 3- Upload file API
@app.post("/upload")
def uploadFile(file:UploadFile=File(...)):
    filename=file.filename
    filePath=os.path.join(UPLOAD_DIR,filename)

    if not file:
        raise HTTPException(
            status_code=400,
            detail="file not uploaded"
        )
    
    with open(filePath,"wb") as buffer: 
        shutil.copyfileobj(file.file, buffer)
        return{
            "message":"file uploaded",
            "filename":filename,
            "filepath":f"http://127.0.0.1:8000/files/{filename}"
             }

# 4- Get  File API:
@app.get("/files/{filename}")
def getFile(filename:str):
    filePath=os.path.join(UPLOAD_DIR,filename)

    if not os.path.exists(filePath):
        raise HTTPException(
            status_code=404,
            detail="File not found"
        )
    
    return{
        "FileUrl":f"http://127.0.0.1:8000/files/{filename}"
    }

@app.get("/")
def Home():
    return{
        "message":"File Upload API"
    }
