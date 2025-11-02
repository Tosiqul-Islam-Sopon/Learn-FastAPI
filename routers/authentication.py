from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
import schemas
import database
import models
import hashing
import jwtToken

router = APIRouter(
    tags=["Authentication"]
)



@router.post('/login', status_code=status.HTTP_200_OK)
def login(data: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == data.email).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with this email not exist')
    if not hashing.Hash.verify(user.password, data.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Incorrect password')
    

    access_token = jwtToken.create_access_token( data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

    