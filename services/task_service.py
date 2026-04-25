from sqlalchemy.orm import Session
from schemas.task import TaskCreate
import repositories.task_repository as task_repo

def get_tasks(db: Session, id: int):
    return task_repo.get_tasks(db, id)

def get_task_by_id(db: Session, user_id: int, task_id: int):
    single_task = task_repo.get_task_by_id(db, user_id, task_id)
    if not single_task:
        raise ValueError("No tasks found for the given id")
    return single_task

def create_task(db: Session, task: TaskCreate, user_id: int):
    return task_repo.create_task(db, task, user_id)

def update_task(db: Session, task: TaskCreate, task_id: int, user_id: int):
    given_task = task_repo.get_task_by_id(db, user_id, task_id)
    if not given_task:
        raise ValueError("task with given id doesn't exist")
    return task_repo.update_task(db, task, task_id, user_id)

def delete_task(db: Session, task_id: int, user_id: int):
    given_task = task_repo.get_task_by_id(db, user_id, task_id)
    if not given_task:
        raise ValueError("task with given id doesn't exist")
    task_repo.delete_task(db, user_id, task_id)