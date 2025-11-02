from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from typing import List
from repository import blog
import schemas
import database
import oauth2

router = APIRouter(
    prefix='/blogs',
    tags=['Blogs']
)


@router.get('', status_code=status.HTTP_200_OK, response_model= List[schemas.ShowBlog])
def get_all_blogs(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all_blogs(db)


@router.post('', status_code=status.HTTP_201_CREATED)
def create_blog(data: schemas.Blog, db: Session = Depends(database.get_db), user_id: int = 1):
    return blog.create_blog(data, db, user_id)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def get_blog_by_id(id: int, db: Session = Depends(database.get_db)):
    return blog.get_blog_by_id(id, db)


@router.delete('/{id}', status_code=status.HTTP_200_OK)
def delete_blog_by_id(id: int, db: Session = Depends(database.get_db)):
    return blog.delete_blog_by_id(id, db)


@router.put('/{id}',  status_code=status.HTTP_202_ACCEPTED)
def update_blog_by_id(id: int, data: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.update_blog_by_id(id, data, db)