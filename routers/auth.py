from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas.user import UserCreate, UserResponse, UserLogin, TokenResponse
import services.user_service as user_service 

router = APIRouter()

@router.post("/register", response_model=UserResponse)
async def register(user: UserCreate, db: Session = Depends(get_db)):
    new_user = user_service.register_user(db, user)
    return new_user

@router.post("/login", response_model=TokenResponse)
async def login(user: UserLogin, db: Session = Depends(get_db)):
    login_user = user_service.login_user(db, user.email, user.password)
    return {"access_token": login_user, "token_type": "bearer"}