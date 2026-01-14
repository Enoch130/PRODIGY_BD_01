from pydantic import BaseModel,EmailStr
from uuid import UUID
from datetime import datetime


class CreateUser(BaseModel):
    name: str
    email: EmailStr
    age: int

