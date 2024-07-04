import requests
import datetime
import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry


class WeatherFetcher:
    def __init__(self, lat, lon, birthdate):
        self.lat = lat
        self.lon = lon
        self.birth_date = birthdate
        self.url = "https://archive-api.open-meteo.com/v1/archive"
        self.params = {"latitude": self.lat,
	                   "longitude": self.lon,
	                   "start_date": birthdate,
	                   "end_date": birthdate,
	                   "hourly": ["temperature_2m",
                                  "relative_humidity_2m",
                                  "precipitation",
                                  "surface_pressure",
                                  "cloud_cover",
                                  "wind_speed_10m"]
                       }
        # Setup the Open-Meteo API client with cache and retry on error
        cache_session = requests_cache.CachedSession('.cache', expire_after = -1)
        retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
        openmeteo = openmeteo_requests.Client(session = retry_session)

    def fetch(self):
        responses = openmeteo.weather_api(self.url, params=self.params)
        return responses[0]

