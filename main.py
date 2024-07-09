import streamlit as st
import re
from Prompts import CityCoordinatesGetter, GetWeatherFromJson
from WeatherRetrieval import WeatherFetcher,get_parameter_value_for_hour
import os
from secret_key import openai_key

os.environ['OPENAI_API_KEY'] = openai_key

parameters = ["temperature_2m", "relative_humidity_2m", "precipitation",
                       "surface_pressure", "cloud_cover", "wind_speed_10m"]

weather_at_noon = {}

def main():

    weather_fetcher = WeatherFetcher()

    st.title("Weather on Your Birthdate")

    city_name = st.text_input("Where were you born?")
    birth_date = st.text_input("When were you born (YYYY-MM-DD)?")

    if st.button("Let's tell you who you are"):
        if city_name and birth_date:
            print(city_name)
            citycoordinatesgetter = CityCoordinatesGetter(city_name)
            lat_city, lon_city = citycoordinatesgetter.get_city_coordinates()

            weather_info = weather_fetcher.fetch(lat_city, lon_city, birth_date)

            for param in parameters:
                weather_at_noon[param] = get_parameter_value_for_hour(weather_info, param)
            
            WeatherDescriptor = GetWeatherFromJson(weather_at_noon)

            weather_description = WeatherDescriptor.weather_description()

            st.write(weather_description)
        else:
            st.error("Please enter both the city and birthdate.")


if __name__ == '__main__':
    main()