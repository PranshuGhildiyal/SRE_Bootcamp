# This is needed as SQLAlchemy needs drivers to communicate with DB.

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.DATABASE_USERNAME}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOSTNAME}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# To connect to a DB, we make use of a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency for sqlAlchemy
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Not in use. using sqlAlchemy.

# while True:
#     try:
#         conn = psycopg2.connect(host="<hostname>",
#                                 database="<db_name>",
#                                 user="<user_name>",
#                                 password="<user_password>",
#                                 cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection successful! ")
#         break
#     except Exception as error:
#         print("Database connection failed!")
#         print("Error: ", error)
#         time.sleep(5)
