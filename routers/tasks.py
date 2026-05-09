from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas.task import TaskCreate, TaskResponse
import services.task_service as task_service
from routers.dependencies import get_current_user

router = APIRouter()

@router.get("/tasks", response_model=list[TaskResponse])
async def get_tasks(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    tasks= task_service.get_tasks(db, current_user.id)
    return tasks

@router.get("/tasks/{task_id}", response_model=TaskResponse)
async def get_task_by_id(task_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    task = task_service.get_task_by_id(db, current_user.id, task_id)
    return task

@router.post("/tasks", response_model = TaskResponse)
async def create_task(task: TaskCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    task = task_service.create_task(db, task, current_user.id)
    return task

@router.put("/tasks/{task_id}", response_model = TaskResponse)
async def update_task(task: TaskCreate, task_id: int,  db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    task = task_service.update_task(db, task, task_id, current_user.id)
    return task

@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    task_service.delete_task(db, current_user.id, task_id)