from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from deta import Deta

deta = Deta()

tasks = deta.Base("task-crud")

app = FastAPI()


class User(BaseModel):
    name: str
    age: int
    hometown: str


class UserUpdate(BaseModel):
    name: str = None
    age: int = None
    hometown: str = None

@app.get("/")
def read_root():
    return {"Hello": "There"}


@app.post("/tasks", status_code=201)
def create_user(user: User):
    u = tasks.put(user.dict())
    return u

@app.get("/tasks")
def list_tasks():
    us = next(tasks.fetch())
    return us

@app.get("/tasks/{uid}")
def get_user(uid: str):
    user = tasks.get(uid)
    if user:
        return user
    return JSONResponse({"message": "user not found"}, status_code=404)


@app.patch("/tasks/{uid}")
def update_user(uid: str, uu: UserUpdate):
    updates = {k:v for k,v in uu.dict().items() if v is not None}
    try:
        tasks.update(updates, uid)
        return tasks.get(uid)
    except Exception:
        return JSONResponse({"message": "user not found"}, status_code=404)


@app.delete("/tasks/{uid}")
def delete_user(uid: str):
    tasks.delete(uid)
    return