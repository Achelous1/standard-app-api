from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from .config import Settings

settings = Settings()

db_host = settings.database_host
db_name = settings.database_name
user_name = settings.database_user
password = settings.database_password

DATABASE = 'postgresql://%s:%s@%s/%s?charset=utf8mb4' % (
    user_name, 
    password, 
    db_host,
    db_name
)

ENGINE = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=True
)

session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

Base = declarative_base()
Base.query = session.query_property()
