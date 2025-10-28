from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from repository import user
from typing import List
import models
import schemas
import database
import hashing

router = APIRouter(
    prefix='/users',
    tags=['Users']
)

@router.get('', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowUser])
def get_all_users(db: Session = Depends(database.get_db)):
    return user.get_all_users(db)

@router.post('', status_code=status.HTTP_201_CREATED)
def create_user(data: schemas.User, db: Session = Depends(database.get_db)):
    return user.create_user(data, db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def get_use_by_id(id: int, db: Session = Depends(database.get_db)):
    return user.get_use_by_id(id, db)