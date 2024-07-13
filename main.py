import streamlit as st
from Coordinates_retriever import CityCoordinatesGetter
from Prompts import  GetWeatherFromJson
from WeatherRetrieval import WeatherFetcher, get_parameter_value_for_hour
import os
import base64
from secret_key import openai_key, geocoding_key

def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode("utf-8")
    md = f"""
    <audio autoplay>
    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """
    st.markdown(md, unsafe_allow_html=True)

parameters = ["temperature_2m", "relative_humidity_2m", "precipitation",
                       "surface_pressure", "cloud_cover", "wind_speed_10m"]

weather_at_given_hour = {}

def main():

    weather_fetcher = WeatherFetcher()

    st.title("Nateology")

    city_name = st.text_input("Where were you born?")
    birth_date = st.text_input("When were you born (YYYY-MM-DD)?")
    hour_birth = st.text_input("At what hour (00-23)")

    if st.button("Let's tell you who you are"):
        if city_name and birth_date:
            citycoordinatesgetter = CityCoordinatesGetter(geocoding_key)
            lat_city, lon_city = citycoordinatesgetter.get_city_coordinates(city_name)

            weather_info = weather_fetcher.fetch(lat_city, lon_city, birth_date)
            print(weather_info)
            for param in parameters:
                weather_at_given_hour[param] = get_parameter_value_for_hour(weather_info, param, birth_date, hour_birth)
            
            print(weather_at_given_hour)
            
            
            WeatherDescriptor = GetWeatherFromJson(openai_key)

            weather_description = WeatherDescriptor.weather_description(weather_at_given_hour)

            st.write(weather_description)

            audio_file = WeatherDescriptor.text_to_speech(weather_description)

            autoplay_audio(audio_file)

            os.remove(audio_file)
        else:
            st.error("Please enter both the city and birthdate.")


if __name__ == '__main__':
    main()