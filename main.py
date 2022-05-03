from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from deta import Deta

from os import getenv
import datetime

deta = Deta()
task_db = deta.Base("task-crud")

configuration = {
    "title":"Python Task List",
    "version":getenv("VERSION", "FALILED TO LOAD VERSION"),
    "author":"Oner",
    "description":'A simple task list with fastapi',
    "python_requires":">:3.5",
    "last_updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
}

app = FastAPI(**configuration)

class Task(BaseModel):
    task_name: str
    task_description: str
    task_created: Optional[str] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
class TaskUpdate(BaseModel):
    task_name: str = None
    task_description: str = None
    task_updated: Optional[str] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@app.get("/")
async def read_root():
    '''
    Description:
    -------
    Async function to describe the name and version of the application

    Returns
    -------
    dict
        Returns a dict with the App Name and version
    '''    
    return {"AppName": "FAST LIST WITH PYTHON", "AppVersion": app.version}


@app.get("/version")
async def read_item():
    '''
    Description:
    -------
    Async function to describe the last update of the application

    Returns
    -------
    dict
        Returns a dict with the app version and last update
    '''    
    return {"AppVersion": app.version, "LastUpdated": app.extra["last_updated"]}

@app.get("/")
def read_root():
    return {"Hello": "There!"}

@app.post("/tasks")
def create_task(task: Task):
    task_db.put(task.dict())
    return task_db.fetch()

@app.get("/tasks")
def list_users(limit: int = 100):
    tasks = task_db.fetch(limit=limit)
    return tasks.items

@app.get("/tasks/{uid}")
def get_user(uid: str):
    task = task_db.get(uid)
    if task:
        return task
    return JSONResponse({"message": "Task not found"}, status_code=404)


@app.patch("/tasks/{uid}")
def update_user(uid: str, uu: TaskUpdate):
    updates = {k:v for k,v in uu.dict().items() if v is not None}
    try:
        task_db.update(updates, uid)
        return task_db.get(uid)
    except Exception:
        return JSONResponse({"message": "user not found"}, status_code=404)


@app.delete("/tasks/{uid}")
def delete_user(uid: str):
    task_db.delete(uid)
    return