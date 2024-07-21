from sqlalchemy import Column, Integer, String

from app.database.db import Base


class CitySearch(Base):
    __tablename__ = 'CitySearches'

    id = Column(Integer(), primary_key=True, nullable=False, autoincrement=True)
    city_name = Column(String(), unique=True, nullable=False)
    search_amount = Column(Integer(), nullable=False, default=1)
