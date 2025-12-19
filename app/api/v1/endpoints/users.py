from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.schemas.user import ShowUser, UserCreate
from app.crud import user as crud_user

router = APIRouter()

@router.get('', status_code=status.HTTP_200_OK, response_model=List[ShowUser])
def get_all_users(db: Session = Depends(get_db)):
    return crud_user.get_all_users(db)

@router.post('', status_code=status.HTTP_201_CREATED)
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    return crud_user.create_user(db, data)

@router.get('/email/{email}', status_code=status.HTTP_200_OK, response_model=ShowUser)
def get_user_by_email(email: str, db: Session = Depends(get_db)):
    return crud_user.get_user_by_email(db, email)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ShowUser)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    return crud_user.get_user_by_id(db, id)
