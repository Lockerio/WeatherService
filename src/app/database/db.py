import sqlalchemy as db
from sqlalchemy.orm import declarative_base

from app.config import DB_URL

engine = db.create_engine(DB_URL)
Base = declarative_base()
