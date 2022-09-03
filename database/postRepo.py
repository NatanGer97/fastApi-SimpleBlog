from routes.schemas import PostDAO
from sqlalchemy.orm.session import Session
import datetime
from database.models import DbPost

def create_new_post(db: Session, request: PostDAO):
    new_post = DbPost(
        image_url = request.image_url,
        title = request.title,
        content = request.content,
        creator = request.creator,
        timestamp = datetime.datetime.now()
    )
    
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return {'created_post': new_post} 

def ge_all_post(db: Session):
    return db.query(DbPost).all()