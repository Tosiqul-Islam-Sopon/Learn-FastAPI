from fastapi import APIRouter
from app.api.v1.endpoints import users, auth, blogs

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(blogs.router, prefix="/blogs", tags=["Blogs"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
