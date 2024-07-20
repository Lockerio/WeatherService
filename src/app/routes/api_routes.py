import requests
from flask import Blueprint, jsonify, Response, request
from icecream import ic

from app.utils.data_preparer import DataPreparer

api_routes_blueprint = Blueprint('api_routes_blueprint', __name__)
data_preparer = DataPreparer()


@api_routes_blueprint.route('/weather', methods=['POST'])
def weather():
    location = ic(request.form.get('location'))
    if location:
        try:
            forecast = data_preparer.prepare_forecast_data(location)
            return jsonify(forecast)
        except Exception as e:
            return jsonify({'error': e})
    return jsonify({'error': 'Could not retrieve weather data'})
