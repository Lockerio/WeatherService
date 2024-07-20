import json

import requests


class OpenmeteoParser:
    @staticmethod
    def get_weather_json(latitude: float, longitude: float):
        url = (f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
               ",relative_humidity_2m,apparent_temperature,precipitation_probability,precipitation,surface_pressure,"
               "cloud_cover,visibility,wind_speed_10m,wind_direction_10m&timezone=auto")

        result = requests.get(url)
        data = result.json()
        return data


if __name__ == "__main__":
    res = OpenmeteoParser.get_weather_json(54.2667, 101.8333)

    print(res["hourly"]["time"])
    print(len(res["hourly"]["time"]))
