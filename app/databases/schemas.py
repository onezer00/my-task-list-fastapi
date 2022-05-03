from typing import Optional

from pydantic import BaseModel
from app.task_list import TaskList

TaskList = TaskList()

class TaskBase(BaseModel):
    task_name: str
    task_description: Optional[str] = None

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    task_name: str
    task_description: str
    class Config:
        orm_mode = True

class TaskUpdate(TaskBase):
    pass
