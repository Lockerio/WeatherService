from app.openmeteo_parser import OpenmeteoParser
from app.utils.time_helper import TimeHelper


class DataPreparer:
    def __init__(self, period: int = 12):
        self.period = period

    def prepare_forecast_data(self, location: str):
        data = OpenmeteoParser.get_weather_json(54.2667, 101.8333)
        local_time = TimeHelper.get_local_time(data["timezone_abbreviation"])
        current_time_index = data["hourly"]["time"].index(local_time)

        current_values = {
            "relative_humidity": data["hourly"]["relative_humidity_2m"][current_time_index],
            "apparent_temperature": data["hourly"]["apparent_temperature"][current_time_index],
            "precipitation_probability": data["hourly"]["precipitation_probability"][current_time_index],
            "precipitation": data["hourly"]["precipitation"][current_time_index],
            "surface_pressure": data["hourly"]["surface_pressure"][current_time_index],
            "cloud_cover": data["hourly"]["cloud_cover"][current_time_index],
            "visibility": data["hourly"]["visibility"][current_time_index],
            "wind_speed": data["hourly"]["wind_speed_10m"][current_time_index],
            "wind_direction": data["hourly"]["wind_direction_10m"][current_time_index]
        }

        temperature_by_hours = [
            {
                'date': time,
                'temperature': temperature
            }
            for time, temperature in zip(
                data["hourly"]["time"][current_time_index:current_time_index + self.period],
                data["hourly"]["temperature_2m"][current_time_index:current_time_index + self.period]
            )
        ]

        forecast = {
            "current_values": current_values,
            "temperature_by_hours": temperature_by_hours
        }

        return forecast
