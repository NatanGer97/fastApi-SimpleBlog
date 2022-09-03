
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1997@localhost:5432/fast_api"
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:root@localhost:3306/blog_api"
# SQLALCHEMY_DATABASE_URL = "mysql://root:root@localhost:3306/fastapi_practice"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
 
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()