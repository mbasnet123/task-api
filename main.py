from fastapi import FastAPI
from database import engine, Base
import models.user
import models.task
from routers import auth, tasks

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(tasks.router, tags=["tasks"])

@app.get("/")
async def root():
    return {"message": "Hello World"}