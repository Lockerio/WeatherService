from app.parsers.openmeteo_parser import OpenmeteoParser
from app.utils.time_helper import TimeHelper


class DataPreparer:
    @staticmethod
    def prepare_forecast_data(latitude: float, longitude: float, period: int = 12):
        data = OpenmeteoParser.get_weather_json(latitude, longitude)
        local_time = TimeHelper.get_local_time(data["utc_offset_seconds"])
        current_time_index = data["hourly"]["time"].index(local_time)

        current_values = {
            "relative_humidity": data["hourly"]["relative_humidity_2m"][current_time_index],
            "apparent_temperature": data["hourly"]["apparent_temperature"][current_time_index],
            "current_temperature": data["hourly"]["temperature_2m"][current_time_index],
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
                data["hourly"]["time"][current_time_index:current_time_index + period],
                data["hourly"]["temperature_2m"][current_time_index:current_time_index + period]
            )
        ]

        forecast = {
            "current_values": current_values,
            "temperature_by_hours": temperature_by_hours
        }

        return forecast
