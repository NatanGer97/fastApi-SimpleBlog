from email.mime import image
from pydantic import *
from datetime import *

class  PostDAO(BaseModel):
    image_url: str
    title: str
    content: str
    creator: str


class PostDTO(BaseModel):
    image_url: str
    title: str
    content: str
    creator: str
    class Config():
        orm_mode = True
