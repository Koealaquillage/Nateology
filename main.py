import openai
from secret_key import OpenAI_key

def ask_for_birthdate():
    return input("When were you born (YYYY-MM-DD)? ")

def ask_for_city():
    return input("Where were you born?")


def main():
    openai_api_key = OpenAI_key

    birth_date = ask_for_birthdate()
    
    city_name = ask_for_city

    weather_fetcher = WeatherFetcher(city_name, birth_date)
    
    # Set up OpenAI
    openai.api_key = openai_api_key

    # Get weather information
    weather_info = weather_fetcher.fetch_weather(city, birth_date)
    
    # Create a completion using OpenAI to respond with the weather information
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"The weather information is ready. Here is the information:\n{weather_info}",
        max_tokens=50
    )

    print(response.choices[0].text.strip())

if __name__ == '__main__':
    main()