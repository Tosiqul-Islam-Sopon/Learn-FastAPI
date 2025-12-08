from fastapi import FastAPI
from app.api.v1.api import api_router
from app.core.config import settings
from app.db.session import engine
from app.db.base import Base

app = FastAPI(title=settings.PROJECT_NAME)

Base.metadata.create_all(bind=engine)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI Blog"}
