from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from .. import models
from ..database import get_db
from .. import schemas
from .. import utils

router = APIRouter(tags=['Authentication'])

@router.post('/login')
async def login(user_data: schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_data.email).first()

    if not user: 
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f'Invalid Credentials')

    
    if not utils.verify_pwd(user_data.password, user.password): 
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f'Invalid Credentials')

    
    # Create Token 

    # Return Token 