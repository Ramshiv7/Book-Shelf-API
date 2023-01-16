from fastapi import FastAPI, Depends, HTTPException, status
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from .. import schemas, models, utils
from ..database import get_db
from typing import List
from .. import oauth2


router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)

@router.get('/', response_model = List[schemas.PostBase])
async def get_all_post(db: Session = Depends(get_db)):
    return_data = db.query(models.DB).all()
    #return_data = db.query(models.PupHub).all()
    return return_data


@router.get('/{id}')
async def get_post_by_id(id: int,db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    books_by_id = db.query(models.DB).filter(models.DB.id == id).all()
    return  books_by_id


@router.post('/')
# async def create_post(new_data: schemas.CreatePost, db : Session = Depends(get_db)):
async def create_post(new_data: schemas.CreatePost, db : Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    data_insert = models.DB(**new_data.dict())
    db.add(data_insert)
    db.commit()
    db.refresh(data_insert)
    return data_insert


@router.put('/{id}')
async def update_post(id: int,upd_data: schemas.UpdatePost, db: Session = Depends(get_db),user_id: int = Depends(oauth2.get_current_user)):
    print(id, upd_data.dict())
    update_q = db.query(models.DB).filter(models.DB.id == id)
    update_query = update_q.first()
    update_q.update(upd_data.dict(), synchronize_session=False)
    db.commit()
    return update_q.first()

@router.delete('/{id}')
async def delete_post(id: int, db: Session = Depends(get_db),user_id: int = Depends(oauth2.get_current_user)):
    del_data = db.query(models.DB).filter(models.DB.id == id)

    del_data.delete(synchronize_session=False)
    db.commit()
    return "deleted the post ID "