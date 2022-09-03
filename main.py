from re import A
from fastapi import FastAPI
from database import models
from database.database import engine
from routes import postRoute

app = FastAPI()
app.include_router(postRoute.router)




models.Base.metadata.create_all(engine)