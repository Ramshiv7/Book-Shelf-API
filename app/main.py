from fastapi import FastAPI, Depends, HTTPException, status
from . import database, models
from .database import get_db
from sqlalchemy.orm import Session
from . import schemas, utils
from typing import List
from .routers import post, user, auth
# from passlib.context import CryptContext


# pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")
app = FastAPI()

# Main Engine Module 
models.Base.metadata.create_all(bind=database.engine)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)