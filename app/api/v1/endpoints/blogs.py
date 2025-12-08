from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.schemas.blog import ShowBlog, BlogCreate
from app.schemas.user import User
from app.crud import blog as crud_blog
from app.dependencies import get_current_user

router = APIRouter()

@router.get('', status_code=status.HTTP_200_OK, response_model=List[ShowBlog])
def get_all_blogs(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud_blog.get_all_blogs(db)

@router.post('', status_code=status.HTTP_201_CREATED)
def create_blog(data: BlogCreate, db: Session = Depends(get_db), user_id: int = 1):
    return crud_blog.create_blog(db, data, user_id)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ShowBlog)
def get_blog_by_id(id: int, db: Session = Depends(get_db)):
    return crud_blog.get_blog_by_id(db, id)

@router.delete('/{id}', status_code=status.HTTP_200_OK)
def delete_blog_by_id(id: int, db: Session = Depends(get_db)):
    return crud_blog.delete_blog_by_id(db, id)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog_by_id(id: int, data: BlogCreate, db: Session = Depends(get_db)):
    return crud_blog.update_blog_by_id(db, id, data)
