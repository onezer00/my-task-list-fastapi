from sqlalchemy import Column, Integer, String, DateTime

from .database import Base

class Task(Base):
    __tablename__ = "task_list"

    id = Column(Integer, primary_key=True, index=True)
    task_name = Column(String, index=True)
    task_description = Column(String, index=True)
    date = Column(DateTime, index=True)