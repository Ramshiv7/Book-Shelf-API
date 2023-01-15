from . import models
from pydantic import BaseModel


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

    