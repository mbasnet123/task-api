from sqlalchemy.orm import Session
from models.user import User
from models.task import Task
from schemas.task import TaskCreate

def get_tasks(db: Session, id: int):
    return db.query(Task).filter(Task.user_id == id).all()

def get_task_by_id(db: Session, user_id: int, task_id: int):
    return db.query(Task).filter(Task.user_id == user_id, Task.id == task_id).first()

def create_task(db: Session, task: TaskCreate, user_id: int):
    db_task = Task(title=task.title, description=task.description, status=task.status, user_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task: TaskCreate, task_id: int, user_id: int):
    task_data = db.query(Task).filter(Task.user_id == user_id, Task.id == task_id).first()
    task_data.title=task.title
    task_data.description=task.description
    task_data.status=task.status
    db.commit()
    db.refresh(task_data)
    return task_data

def delete_task(db: Session, user_id: int, task_id: int):
    # print(f"Deleting task with user_id: {user_id}, task_id: {task_id}")
    task = db.query(Task).filter(Task.user_id == user_id, Task.id == task_id).first()
    # print(f"Found task: {task}")
    db.delete(task)
    db.commit()


