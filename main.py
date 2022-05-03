from fastapi import FastAPI
from pydantic import BaseModel
from deta import Deta

from datetime import datetime

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
    "SQLALCHEMY_DATABASE_URI": "postgresql://sql10489830:mfpJPYJ71Y@sql10489830:3306/task_app",
}

db = Deta()

tasks = db.Base('tasks_db')

app = FastAPI(**configuration)

class Task(BaseModel):
    task_name: str
    task_description: str
    task_creation: str

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

@app.post('tasks')
def create_task(task: Task):
    task.put(task.dict())
    return next(task.fetch())