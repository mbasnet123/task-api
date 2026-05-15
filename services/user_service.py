from passlib.context import CryptContext
from sqlalchemy.orm import Session
from schemas.user import UserCreate
import repositories.user_repository as user_repo
from jose import jwt
import os
from datetime import datetime, timedelta

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def register_user(db:Session, user:UserCreate):
    existing_user = user_repo.get_user_by_email(db, user.email)
    if existing_user:
        raise ValueError("Email already registered")
    hashed_password = pwd_context.hash(user.password)
    new_user = UserCreate(name=user.name, email=user.email, password=hashed_password)
    return user_repo.create_user(db, new_user)

def login_user(db: Session, email:str, password: str):
    existing_user = user_repo.get_user_by_email(db, email)
    if not existing_user:
        raise ValueError("Email not registered")
    password_verified = pwd_context.verify(password, existing_user.password)
    if not password_verified:
        raise ValueError("password not verified")
    token = jwt.encode({"sub": existing_user.email, "exp": datetime.utcnow() + timedelta(minutes=30)}, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM"))
    return token