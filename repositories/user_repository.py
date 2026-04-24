from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate

def get_user_by_email(db: Session, email: str):
    # SELECT * FROM users WHERE email = user.email
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    # INSERT into User
    db_user = User(name=user.name, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user