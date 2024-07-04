import requests
import datetime
from secret_key import Openweathermap_key

# Replace with your OpenWeatherMap API key
OPENWEATHERMAP_KEY = Openweathermap_key

class WeatherFetcher:
    def __init__(self, city_name, birthdate):
        self.city_name = city_name
        self.birth_date = birth_date
        self.city_coord = []
        
    def get_city_coordinates(self):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city_name}&appid={OPENWEATHERMAP_KEY}"
        response = requests.get(url)
        data = response.json()
        if 'coord' in data:
            self.city_coord = data['coord']
    
    def get_weather_on_date(self, city, date):
        timestamp = int(date.timestamp())
        url = f"http://api.openweathermap.org/data/2.5/onecall/timemachine?lat={city['lat']}&lon={city['lon']}&dt={timestamp}&appid={self.api_key}"
        response = requests.get(url)
        data = response.json()
        if 'current' in data:
            weather = data['current']['weather'][0]['description']
            temp = data['current']['temp']
            return weather, temp
        return None, None

    def fetch_weather(self):
        try:
            date = datetime.datetime.strptime(self.birth_date, '%Y-%m-%d')
        except ValueError:
            return "Invalid date format. Please use 'YYYY-MM-DD'."
        
        self.get_city_coordinates(city)
        if not self.city_coord:
            return "City not found."
        
        weather, temp = self.get_weather_on_date(self.city_coord, date)
        if weather is None:
            return "Weather data not found for the given date."
        
        temp_celsius = temp - 273.15  # Convert from Kelvin to Celsius
        return f"The weather in {self.city_name} on {self.birth_date} was {weather} with a temperature of {temp_celsius:.2f}°C."