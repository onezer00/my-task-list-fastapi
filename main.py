from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app.databases import models, schemas, crud
from app.databases.database import SessionLocal, engine

from app.task_list import TaskList

import datetime
import load_envs
"""
It is responsible for the configuration

...

Methods
-------
get_current_config()
    Gets current config
"""

from os import getenv

load_envs.load()

configuration = {
    "title":"Python Task List",
    "version":getenv("VERSION", "FALILED TO LOAD VERSION"),
    "author":"Oner",
    "description":'A simple task list with fastapi',
    "python_requires":">:3.5",
    "last_updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
}

app = FastAPI(**configuration)
TaskList = TaskList()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

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

@app.get("/tasks", response_model=list[schemas.Task])
async def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db, skip=skip, limit=limit)
    return tasks

@app.post('/tasks', response_model=schemas.Task)
async def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db=db, task=task)

@app.delete('/tasks/{task_id}')
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    return crud.delete_task(db=db, task_id=task_id)

@app.put('/tasks/{task_id}', response_model=schemas.TaskUpdate)
async def edit_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    return crud.edit_task(db=db, task_id=task_id, task=task)