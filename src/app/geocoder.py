from geopy.geocoders import Nominatim


class Geocoder:
    @staticmethod
    def get_coordinates_by_city_name(city_name: str):
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city_name)

        if location:
            return location.latitude, location.longitude
        else:
            raise Exception(f"Не удалось получить координаты для города {city_name}")
