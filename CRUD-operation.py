# CRUD operations: seeing using swagger
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

tasks = []


class Task(BaseModel):
    id: int
    title: str
    completed: bool


# create task
@app.post("/tasks")
def createTask(task: Task):
    tasks.append(task)
    return {"message": "Task added", "data": tasks}


# read task
@app.get("/tasks")
def readTask():
    return tasks


# read single task
@app.get("/tasks/{task_id}")
def getSingleTask(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    return {"error": "Task not found"}


# update task
@app.put("/tasks/{task_id}")
def updatedTask(task_id: int, updatedTask: Task):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks[index] = updatedTask
            return {"message": "Task updated", "data": updatedTask}
    return {"error": "Task not found"}


# delete task
@app.delete("/tasks/{task_id}")
def deleteTask(task_id: int):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(index)
            return {"message:": "Data Deleted"}
    return {"error": "Task not found"}
