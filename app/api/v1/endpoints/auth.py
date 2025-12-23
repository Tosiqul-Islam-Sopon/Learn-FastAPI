from fastapi import APIRouter, Depends, HTTPException, Body
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.security import verify_password, create_access_token, create_refresh_token, verify_refresh_token
from app.models.user import User
from app.schemas.auth import RefreshTokenRequest

router = APIRouter()

@router.post('/login')
def login(data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.username).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not verify_password(data.password, user.password):
        raise HTTPException(status_code=404, detail="Incorrect password")

    access_token = create_access_token({"sub": user.email})
    refresh_token = create_refresh_token({"sub": user.email})

    # (Optional but recommended) Store refresh token hash in DB
    # user.refresh_token = get_password_hash(refresh_token)
    db.commit()

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

@router.post("/refresh")
def refresh(payload: RefreshTokenRequest, db: Session = Depends(get_db)):
    user = verify_refresh_token(payload.refresh_token, db)

    # Create new access token
    new_access_token = create_access_token({"sub": user.email})
    # new_refresh_token = create_refresh_token({"sub": user.email})

    # rotate refresh token
    # user.refresh_token = get_password_hash(new_refresh_token)
    # db.commit()

    return {
        "access_token": new_access_token,
    }

