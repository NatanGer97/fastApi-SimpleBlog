from fastapi import *
from routes.schemas import PostDAO,PostDTO
from sqlalchemy.orm import Session
from database.database import get_db
from database import postRepo

router = APIRouter(prefix='/post', tags=['post'])

@router.post('')
def cerate_Post(req: PostDAO, db: Session = Depends(get_db)):
    return postRepo.create_new_post(db, req)

@router.get('/all')
def get_all_post(db: Session = Depends(get_db)):
    return postRepo.ge_all_post(db)