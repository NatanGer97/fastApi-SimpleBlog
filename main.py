from re import A
from fastapi import FastAPI
from database import models
from database.database import engine

app = FastAPI()

@app.get("/")
def index():
    return {'msg': "Hello World"}



models.Base.metadata.create_all(engine)