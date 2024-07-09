import requests

class WeatherFetcher:
    def __init__(self):
        self.base_url = "https://archive-api.open-meteo.com/v1/era5?"
        self.params = ["temperature_2m", "relative_humidity_2m", "precipitation",
                       "surface_pressure", "cloud_cover", "wind_speed_10m"]
        self.url = ""  # Initialize an empty URL that will be built later

    def build_url(self, lat, lon, date):
        # Construct the URL with the provided parameters and date
        params_str = ",".join(self.params)
        self.url = f"{self.base_url}latitude={lat}&longitude={lon}"
        self.url += f"&hourly={params_str}&start_date={date}&end_date={date}"

    def fetch(self, lat, lon, date):
        # Build the URL for the given latitude, longitude, and date
        self.build_url(lat, lon, date)

        # Send a GET request to the API
        response = requests.get(self.url)
    
        # Check if the request was successful
        if response.status_code == 200:
            # Return the JSON response
            return response.json()
        else:
            # Return an error message if something went wrong
            return {"error": "Failed to fetch data", "status_code": response.status_code}


