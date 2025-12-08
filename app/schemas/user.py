from pydantic import BaseModel
from typing import List

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    pass

class ShowUser(BaseModel):
    name: str
    email: str
    
    class Config:
        from_attributes = True
