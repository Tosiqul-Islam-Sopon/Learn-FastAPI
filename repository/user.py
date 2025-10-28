from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
import database
import hashing


def get_all_users(db: Session = Depends(database.get_db)):
    users = db.query(models.User).all()
    return users


def create_user(data: schemas.User, db: Session = Depends(database.get_db)):
    user = models.User(name=data.name, email=data.email, password=hashing.Hash.bcrypt(data.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_use_by_id(id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} not found')
    
    return user