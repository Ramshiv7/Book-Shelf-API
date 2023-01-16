# DataBase Models 
from .database import Base 
from sqlalchemy import Integer, Text, Boolean, TIMESTAMP, Column, text


""" 
title : str 
content : str 
published : bool 
    
"""

class DB(Base):
    __tablename__ = 'PostDetails'

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(Text, nullable=False)
    content = Column(Text, nullable=False)
    published = Column(Boolean, nullable=False, server_default="True")
    created_at = Column(TIMESTAMP, nullable=False, server_default=text('now()'))



class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(Text, nullable=False, unique=True)
    password = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text('now()'))
