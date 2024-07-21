from sqlalchemy.orm import Session

from app.database.dals.city_search_dal import CitySearchDAO
from app.database.db import engine
from app.database.services.city_search_service import CitySearchService

session = Session(bind=engine)


city_search_dao = CitySearchDAO(session)
city_search_service = CitySearchService(city_search_dao)
