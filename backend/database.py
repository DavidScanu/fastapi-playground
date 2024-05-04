from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# DEFINE THE DATABASE CREDENTIALS
user = os.environ['DB_USER']
password = os.environ['DB_PASS']
host = os.environ['DB_HOST']
port = os.environ['DB_PORT']
database = os.environ['DB_NAME']

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg://{user}:{password}@{host}:{port}/{database}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()