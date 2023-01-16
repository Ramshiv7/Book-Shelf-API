from fastapi import FastAPI, Depends, HTTPException, status
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from .. import schemas, models, utils
from ..database import get_db
from typing import List



router = APIRouter(prefix='/users', tags=['Users'])

# Create User for DB Model - User
@router.post('/', response_model= schemas.UserReturn)
async def create_user(user_details: schemas.UserCreate,db: Session = Depends(get_db)):
    # hashed_pwd = pwd_context.hash(user_details.email)
    # Hashing the Password 
    hashed_pwd = utils.hash_pass(user_details.password)
    user_details.password = hashed_pwd  # Replace Normal Password With Hashed Password
    user_data = models.User(**user_details.dict())
    db.add(user_data)
    db.commit()
    db.refresh(user_data)
    return user_data


@router.get('/{id}', response_model= schemas.UserReturn)
async def get_user(id: int, db: Session = Depends(get_db)):
    user_data = db.query(models.User).filter(models.User.id == id).first()

    if not user_data:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f'No User Has Been Found with ID : {id}')

    return user_data