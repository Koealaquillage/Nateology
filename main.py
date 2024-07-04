import openai
import streamlit as st
from secret_key import OpenAI_key

def ask_for_birthdate():
    return input(" ")

def ask_for_city():
    return input("")


def main():

    st.title("Weather on Your Birthdate")
    openai_api_key = OpenAI_key

    city_name = st.text_input("Where were you born?")
    birth_date = st.text_input("When were you born (YYYY-MM-DD)?")

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