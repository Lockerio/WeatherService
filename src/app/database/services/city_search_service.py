from app.database.dals.city_search_dal import CitySearchDAO


class CitySearchService:
    def __init__(self, dao: CitySearchDAO):
        self.dao = dao

    def get_one(self, city_id):
        return self.dao.get_one(city_id)

    def get_one_by_city_name(self, city_name):
        return self.dao.get_one_by_city_name(city_name)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        city_name = data.get("city_name")

        try:
            city = self.get_one_by_city_name(city_name)
            search_amount = data.get("search_amount")

            if search_amount:
                city.search_amount = search_amount

            return self.dao.update(city)

        except Exception:
            self.create({
                "city_name": city_name
            })

    def delete(self, city_id):
        self.dao.delete(city_id)
