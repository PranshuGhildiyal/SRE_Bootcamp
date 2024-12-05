# Every model represents a table in the DB.
# Limitation here is that sqlAlchemy does not modify tables once created.
from .database import Base
from sqlalchemy import Column, String, Date, Integer, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class Students(Base):
    __tablename__ = "students"

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    joining_date = Column(Date, server_default=func.now(), nullable=False)
    owner_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )

    owner = relationship(
        "Users"
    )  # will create a property for students and define relationship with user.


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), server_default=func.now(), nullable=False
    )
