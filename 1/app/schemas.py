from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class StudentData(BaseModel):  # Schema -> pydantic
    name: str
    age: int


class CreateStudent(StudentData):
    pass

    class Config:  # Ensures no extra value or data with wrong key is added.
        extra = "forbid"


class ResponseUser(BaseModel):  # Output schema for User.
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class ResponseData(StudentData):  # Output schema for Student.
    id: int
    owner_id: int
    owner: ResponseUser  # This comes from defining the relationship in models.py
    # joining_date: datetime

    class Config:
        orm_mode = True


class CreateUser(BaseModel):
    email: EmailStr
    password: str

    class Config:  # Ensures no extra value or data with wrong key is added.
        extra = "forbid"


class UserLogin(CreateUser):
    pass


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None
