from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import models
from ..database import get_db
from .. import schemas
from .. import utils
from .. import oauth2

router = APIRouter(tags=['Authentication'])

@router.post('/login', response_model= schemas.Token)
async def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not user: 
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail=f'Invalid Credentials')

    
    if not utils.verify_pwd(user_credentials.password, user.password): 
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail=f'Invalid Credentials')

    
    # Create Token 
    access_token = oauth2.create_access_token(data={"user_id": user.id })

    return {"access token": access_token, "token_type": "bearer"}

    # Return Token 


