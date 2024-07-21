from geopy.geocoders import Nominatim


class Geocoder:
    @staticmethod
    def get_coordinates_by_city_name(city_name: str):
        try:
            geolocator = Nominatim(user_agent="geoapiExercises")
            location = geolocator.geocode(city_name)
        except Exception as e:
            raise Exception(f"Кончились запросы к геокодеру\n{e}")

        if location:
            return location.latitude, location.longitude
        else:
            raise Exception(f"Не удалось получить координаты для города {city_name}")


if __name__ == "__main__":
    res = Geocoder.get_coordinates_by_city_name("Москва")
    print(res)
