from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.blog import Blog
from app.schemas.blog import BlogCreate

def get_all_blogs(db: Session):
    return db.query(Blog).all()

def get_blog_by_id(db: Session, id: int):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')
    return blog

def create_blog(db: Session, blog: BlogCreate, user_id: int = 1):
    new_blog = Blog(title=blog.title, description=blog.description, user_id=user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def update_blog_by_id(db: Session, id: int, blog: BlogCreate):
    db_blog = db.query(Blog).filter(Blog.id == id)
    if not db_blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')
    db_blog.update(blog.model_dump())
    db.commit()
    return blog

def delete_blog_by_id(db: Session, id: int):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')
    blog.delete(synchronize_session=False)
    db.commit()
    return {'message': 'blog is deleted successfully'}
