from sqlalchemy import create_engine

# from sqlalchemy.orm.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base

# We can put the uri in plain text here. In the future we need to make it read
# from the environment
SQLALCHEMY_DATABASE_URL = "sqlite:///mayat_api.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
