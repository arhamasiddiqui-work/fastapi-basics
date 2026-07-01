# CRUD with DATABASE: using SQLAlChemy

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from fastapi import FastAPI,Depends,HTTPException

app=FastAPI()

# Database URL 
DATABASE_URL="sqlite:///./test.db"

# Engine: create(DB connection)
engine= create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False})  

# Session: create(DB operation)
sessionLocal= sessionmaker(bind=engine) 

#  Base: create model/table
Base=declarative_base()    

# Model/Table
class Task(Base):      
    __tablename__="tasks"  

    id= Column(Integer,primary_key=True, index=True)  
    title= Column(String)
    completed=Column(String)

# Create tables
Base.metadata.create_all(bind=engine) 

# Dependency (DB session provide karega)
def get_db():
    db=sessionLocal()  
    try:
        yield db
    finally:
        db.close()  

#1- CREATE API:
@app.post("/tasks")
def createTask(title:str, db:Session=Depends(get_db)):
    task= Task(title=title,completed="False")  #create object of model
    db.add(task)          #data mai add 
    db.commit()          #data mai commit
    db.refresh(task)      #data mai refresh(latest data display)
    return {
        "message":"Task created successfully",
        "data":task
    }


#2- READ API:
# read all data:
@app.get("/tasks")
def getTasks(db:Session=Depends(get_db)):
    tasks=db.query(Task).all()  #read all data
    return {
        "Total":len(tasks),
        "data":tasks
    }
# read single data based on id:
@app.get("/tasks/{id}")
def getTask(id=int, db:Session=Depends(get_db)):
    task=db.query(Task).filter(Task.id==id).first()  #read single data
    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    return task


#3- UPDATE API:
@app.put("/tasks/{id}")
def updateTask(id:int,title:str, db:Session = Depends(get_db)):
    task= db.query(Task).filter(Task.id==id).first()
    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    
    task.title=title
    db.commit()
    db.refresh(task)

    return{
        "message":"Task Updated",
        "data":task
    }

#4- DELETE API:
@app.delete("/tasks/{id}")
def deleteTask(id:int,db:Session=Depends(get_db)):
    task=db.query(Task).filter(Task.id==id).first()
    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    
    db.delete(task)
    db.commit()

    return {
        "message":"Task deleted successfully"
    }