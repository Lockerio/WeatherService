import traceback

import requests
from flask import Blueprint, jsonify, Response, request
from icecream import ic

from app.database.container import city_search_service
from app.geocoder import Geocoder
from app.utils.data_preparer import DataPreparer

api_routes_blueprint = Blueprint('api_routes_blueprint', __name__)


@api_routes_blueprint.route('/weather', methods=['POST'])
def weather():
    location = ic(request.form.get('location'))
    if location:
        try:
            # Если кончились запросы к геокодеру, можно указать здесь геоточки для проверки сервиса
            # latitude, longitude = Geocoder.get_coordinates_by_city_name(location)
            latitude, longitude = 50, 70

            if latitude and longitude:
                city_search_service.update({"city_name": location})
            forecast = DataPreparer.prepare_forecast_data(latitude, longitude)
            return jsonify(forecast)
        except Exception as e:
            traceback.print_exc()
            return jsonify({'error': e})
    return jsonify({'error': 'Could not retrieve weather data'})
