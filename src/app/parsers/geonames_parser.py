import requests

from app.config import GEONAMES_USERNAME


class GeonamesParser:
    @staticmethod
    def get_cities_names_json(request):
        term = request.args.get('term', '')
        url = "http://api.geonames.org/searchJSON"

        response = requests.get(url, params={
            'q': term,
            'maxRows': 10,
            'username': GEONAMES_USERNAME
        })
        data = response.json()
        return data
