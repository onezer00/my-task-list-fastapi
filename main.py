from fastapi import FastAPI
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
