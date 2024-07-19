import streamlit as st
from Coordinates_retriever import CityCoordinatesGetter
from Prompts import  GetWeatherFromJson
from WeatherRetrieval import WeatherFetcher, get_parameter_value_for_hour
from audio import autoplay_audio
from front_end import texts
import os


openai_key = st.secrets["openai_key"]
geocoding_key = st.secrets["geocoding_key"]

parameters = ["temperature_2m", "relative_humidity_2m", "precipitation",
                       "surface_pressure", "cloud_cover", "wind_speed_10m"]

weather_at_given_hour = {}

def main():

    weather_fetcher = WeatherFetcher()

    st.title("Nateology")

    # Language selection
    language = st.selectbox("Select Language / Sélectionnez la langue / Seleccione el idioma", ("English", "Français", "Español"))

    selected_texts = texts[language]

    city_name = st.text_input(selected_texts["city_input"])
    birth_date = st.text_input(selected_texts["date_input"])
    hour_birth = st.text_input(selected_texts["hour_input"])

    if st.button(selected_texts["button"]):
        if city_name and birth_date:
             with st.spinner(selected_texts["interrogating"]):
                 citycoordinatesgetter = CityCoordinatesGetter(geocoding_key)
                 lat_city, lon_city = citycoordinatesgetter.get_city_coordinates(city_name)

                 weather_info = weather_fetcher.fetch(lat_city, lon_city, birth_date)
                 for param in parameters:
                     weather_at_given_hour[param] = get_parameter_value_for_hour(weather_info, param, birth_date, hour_birth)
            
            
                 WeatherDescriptor = GetWeatherFromJson(openai_key, language)

                 weather_description = WeatherDescriptor.weather_description(weather_at_given_hour)

             st.write(weather_description)
             with st.spinner(selected_texts["preparing_voice"]):
                 audio_file = WeatherDescriptor.text_to_speech(weather_description)

             autoplay_audio(audio_file)

             os.remove(audio_file)
        else:
            st.error("Please enter both the city and birthdate.")


if __name__ == '__main__':
    main()