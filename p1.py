from fastapi import FastAPI
from routers import blog, user
import models
import database

app = FastAPI()

models.Base.metadata.create_all(database.engine)

app.include_router(blog.router)
app.include_router(user.router)