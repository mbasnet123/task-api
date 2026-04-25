from passlib.context import CryptContext
from sqlalchemy.orm import Session
from schemas.user import UserCreate
import repositories.user_repository as user_repo

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def register_user(db:Session, user:UserCreate):
    existing_user = user_repo.get_user_by_email(db, user.email)
    if existing_user:
        raise ValueError("Email already registered")
    hashed_password = pwd_context.hash(user.password)
    new_user = UserCreate(name=user.name, email=user.email, password=hashed_password)
    return user_repo.create_user(db, new_user)

