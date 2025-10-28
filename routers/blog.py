from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
import database

router = APIRouter(
    prefix='/blogs',
    tags=['Blogs']
)


@router.get('', status_code=status.HTTP_200_OK, response_model= List[schemas.ShowBlog])
def get_all_blogs(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@router.post('', status_code=status.HTTP_201_CREATED)
def create_blog(blog: schemas.Blog, db: Session = Depends(database.get_db), user_id: int = 1):
    new_blog = models.Blog(title=blog.title, description=blog.description, user_id=user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def get_blog_by_id(id: int, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')
    
    return blog

@router.delete('/{id}', status_code=status.HTTP_200_OK)
def delete_blog_by_id(id: int, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')

    blog.delete(synchronize_session=False)
    db.commit()
    return {'message': 'blog is deleted successfully'}

@router.put('/{id}',  status_code=status.HTTP_202_ACCEPTED)
def update_blog_by_id(id: int, blog: schemas.Blog, db: Session = Depends(database.get_db)):
    new_blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not new_blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')

    new_blog.update(blog.model_dump())
    db.commit()
    return blog