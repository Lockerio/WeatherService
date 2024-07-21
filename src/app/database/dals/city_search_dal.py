from app.database.model import CitySearch


class CitySearchDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, city_id):
        return self.session.query(CitySearch).get(city_id)

    def get_one_by_city_name(self, city_name):
        return self.session.query(CitySearch).filter_by(city_name=city_name).first()

    def get_all(self):
        return self.session.query(CitySearch).all()

    def create(self, data):
        city = CitySearch(**data)
        self.session.add(city)
        self.session.commit()
        return city

    def update(self, city):
        self.session.add(city)
        self.session.commit()
        return city

    def delete(self, city_id):
        city = self.get_one(city_id)
        self.session.delete(city)
        self.session.commit()
