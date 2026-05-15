from pydantic import BaseModel
from models.task import TaskStatus
class TaskCreate(BaseModel):
    title: str
    description: str
    status: TaskStatus

class TaskResponse(BaseModel):
    id: int
    user_id: int
    title: str
    description: str
    status: TaskStatus
    