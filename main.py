from fastapi import FastAPI
from database import engine, Base
import models.user
import models.task

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hello World"}