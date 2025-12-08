from pydantic import BaseModel

class BlogBase(BaseModel):
    title: str
    description: str

class BlogCreate(BlogBase):
    pass

class Blog(BlogBase):
    class Config:
        from_attributes = True

class ShowBlogUser(BaseModel):
    name: str
    email: str
    
    class Config:
        from_attributes = True

class ShowBlog(BlogBase):
    id: int
    creator: ShowBlogUser
    
    class Config:
        from_attributes = True
