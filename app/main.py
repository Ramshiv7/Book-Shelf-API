from fastapi import FastAPI, Depends
from . import database, models
from .database import get_db
from sqlalchemy.orm import Session
from . import schemas
from typing import List
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


app = FastAPI()

# Main Engine Module 
models.Base.metadata.create_all(bind=database.engine)


@app.get('/post', response_model = List[schemas.PostBase])
async def get_all_post(db: Session = Depends(get_db)):
    return_data = db.query(models.DB).all()
    #return_data = db.query(models.PupHub).all()
    return return_data


@app.get('/post/{id}')
async def get_post_by_id(id: int,db: Session = Depends(get_db)):
    books_by_id = db.query(models.DB).filter(models.DB.id == id).all()
    return  books_by_id


@app.post('/post')
async def create_post(new_data: schemas.CreatePost, db : Session = Depends(get_db)):
    data_insert = models.DB(**new_data.dict())
    db.add(data_insert)
    db.commit()
    db.refresh(data_insert)
    return data_insert


@app.put('/post/{id}')
async def update_post(id: int,upd_data: schemas.UpdatePost, db: Session = Depends(get_db)):
    print(id, upd_data.dict())
    update_q = db.query(models.DB).filter(models.DB.id == id)
    update_query = update_q.first()
    update_q.update(upd_data.dict(), synchronize_session=False)
    db.commit()
    return update_q.first()

@app.delete('/post/{id}')
async def delete_post(id: int, db: Session = Depends(get_db)):
    del_data = db.query(models.DB).filter(models.DB.id == id)

    del_data.delete(synchronize_session=False)
    db.commit()
    return "deleted the post ID "


# Create User for DB Model - User
@app.post('/user', response_model= schemas.UserReturn)
async def create_user(user_details: schemas.UserCreate,db: Session = Depends(get_db)):
    hashed_pwd = pwd_context.hash(user_details.email) # Hashing the Password 
    user_details.password = hashed_pwd  # Replace Normal Password With Hashed Password
    user_data = models.User(**user_details.dict())
    db.add(user_data)
    db.commit()
    db.refresh(user_data)
    return user_data