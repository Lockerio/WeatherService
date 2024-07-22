import traceback

import requests
from flask import Blueprint, jsonify, Response, request, make_response
from icecream import ic

from app.database.container import city_search_service
from app.geocoder import Geocoder
from app.utils.data_preparer import DataPreparer

api_routes_blueprint = Blueprint('api_routes_blueprint', __name__)


@api_routes_blueprint.route('/cities_searches', methods=['GET'])
def cities_searches():
    cities = city_search_service.get_all()
    cities_json = [
        {
            "city_name": city.city_name,
            "search_amount": city.search_amount
        }
        for city in cities
    ]
    return jsonify({"cities_list": cities_json})


@api_routes_blueprint.route('/get_cities', methods=['GET'])
def get_cities():
    cities = request.cookies.get('cities', '')
    cities_list = cities.split(',') if cities else []
    return jsonify({'cities': cities_list})


@api_routes_blueprint.route('/weather', methods=['POST'])
def weather():
    location = request.form.get('location')
    if location:
        try:
            # Если кончились запросы к геокодеру, можно указать здесь геоточки для проверки сервиса
            # latitude, longitude = Geocoder.get_coordinates_by_city_name(location)
            latitude, longitude = 50, 70

            if latitude and longitude:
                city_search_service.update({"city_name": location})

                response = make_response()
                response = update_cities_cookie(response, location)

                forecast = DataPreparer.prepare_forecast_data(latitude, longitude)
                response.data = jsonify(forecast).data
                return response

            forecast = DataPreparer.prepare_forecast_data(latitude, longitude)
            return jsonify(forecast)
        except Exception as e:
            traceback.print_exc()
            return jsonify({'error': e})
    return jsonify({'error': 'Could not retrieve weather data'})


def update_cities_cookie(response, city_name):
    cities = request.cookies.get('cities', '')
    cities_list = cities.split(',') if cities else []

    if city_name in cities_list:
        cities_list.remove(city_name)
    cities_list.insert(0, city_name)

    if len(cities_list) > 5:
        cities_list = cities_list[:5]

    cities_str = ','.join(cities_list)
    response.set_cookie('cities', cities_str, max_age=60*60*24*30)
    return response
