from sqlalchemy.orm import Session

from . import models, schemas

def get_task(db: Session, id: int):
    return db.query(models.Task).filter(models.Task.id == id).first()


def get_task_by_name(db: Session, task_name: str):
    return db.query(models.Task).filter(models.Task.task_name == task_name).first()


def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Task).offset(skip).limit(limit).all()


def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int):
    task = get_task(db, task_id)
    if task is not None:
        db.delete(task)
        db.commit()
        return task
    return None

def edit_task(db: Session, task_id: int, task: schemas.TaskUpdate):
    db_task = get_task(db, task_id)
    if db_task is not None:
        if task.task_name is not None:
            db_task.task_name = task.task_name
        if task.task_description is not None:
            db_task.task_description = task.task_description
        db.commit()
        return task
    return None
