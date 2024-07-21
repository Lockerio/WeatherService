import traceback

import requests
from flask import Blueprint, jsonify, Response, request
from icecream import ic

from app.geocoder import Geocoder
from app.utils.data_preparer import DataPreparer

api_routes_blueprint = Blueprint('api_routes_blueprint', __name__)


@api_routes_blueprint.route('/weather', methods=['POST'])
def weather():
    location = ic(request.form.get('location'))
    if location:
        try:
            latitude, longitude = Geocoder.get_coordinates_by_city_name(location)
            if latitude and longitude:
                pass
            forecast = DataPreparer.prepare_forecast_data(latitude, longitude)
            return jsonify(forecast)
        except Exception as e:
            traceback.print_exc()
            return jsonify({'error': e})
    return jsonify({'error': 'Could not retrieve weather data'})
