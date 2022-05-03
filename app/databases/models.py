from sqlalchemy import Column, Integer, String, DateTime

from .database import deta_key

class Task(deta_key):
    __tablename__ = "tasks_db"

    id = Column(Integer, primary_key=True, index=True)
    task_name = Column(String, index=True)
    task_description = Column(String, index=True)
    date = Column(DateTime, index=True)