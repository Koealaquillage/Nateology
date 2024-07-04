import openai
import streamlit as st
import re
from secret_key import OpenAI_key

def get_city_coordinates(city_name):
    
    prompt = f"What are the latitude and longitude coordinates of {city_name}?"
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    
    response_text = response.choices[0].text.strip()
    
    # Using regex to find the coordinates in the response
    match = re.search(r"(-?\d+\.\d+)[^\d,]+(-?\d+\.\d+)", response_text)
    if match:
        lat = float(match.group(1))
        lon = float(match.group(2))
        return [lat, lon]
    else:
        return "Coordinates not found in the response."


def main():

    st.title("Weather on Your Birthdate")
    openai_api_key = OpenAI_key

    city_name = st.text_input("Where were you born?")
    birth_date = st.text_input("When were you born (YYYY-MM-DD)?")

    lat_city, lon_city = get_city_coordinates(city_name)

    if st.button("Let's tell you who you are"):
        if city_name and birth_date:
            weather_info = weather_fetcher.fetch_weather(city_name, birth_date)
            
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"The weather information is ready. Here is the information:\n{weather_info}",
                max_tokens=50
            )

            st.write(response.choices[0].text.strip())
        else:
            st.error("Please enter both the city and birthdate.")


if __name__ == '__main__':
    main()