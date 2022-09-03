from ast import In
from email.mime import image
from typing import Collection
from .database import Base
from sqlalchemy import *

class DbPost(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(Text)
    title = Column(Text)
    content = Column(Text)
    creator = Column(Text)
    timestamp = Column(DateTime)