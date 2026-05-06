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