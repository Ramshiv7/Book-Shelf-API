from . import models
from datetime import datetime
from pydantic import BaseModel, EmailStr



class PostBase(BaseModel):
    title : str 
    content : str 
    published : bool 

    class Config:
        orm_mode = True


class CreatePost(PostBase):
    pass

class UpdatePost(PostBase):
    pass
    

class ReturnPostModel(PostBase):
    title : str 
    content : str 
    published : bool 

    

class UserCreate(BaseModel):
    email : EmailStr
    password : str 


class UserReturn(BaseModel):
    id : int
    email: EmailStr
    created_at : datetime

    class Config:
        orm_mode = True