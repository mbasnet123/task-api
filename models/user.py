from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer
from database import Base

class User(Base):
    __tablename__ = "users"
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)