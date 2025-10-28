from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
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
    users = db.query(models.User).all()
    return users

@router.post('', status_code=status.HTTP_201_CREATED)
def create_user(data: schemas.User, db: Session = Depends(database.get_db)):
    user = models.User(name=data.name, email=data.email, password=hashing.Hash.bcrypt(data.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def get_use_by_id(id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} not found')
    
    return user