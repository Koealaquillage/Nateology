import re
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import OpenAI


class CityCoordinatesGetter():

    def __init__(self, city_name):
        self.city_name = city_name

        self.template =  PromptTemplate(
                             input_variables=["city"],
                             template="Please provide the latitude and longitude coordinates of {city} in the format: 'Latitude: <latitude>, Longitude: <longitude>'."
                            )

        self.llm = OpenAI(temperature=0, max_tokens=30) 

        self.chain = LLMChain(llm=self.llm, prompt=self.template)

    def get_city_coordinates(self):
        response = self.chain.run({"city": self.city_name})
        print(response)
        # Using regex to find the coordinates in the response
        try:
            parts = response_text.split(',')
            lat = float(parts[0].split(':')[1].strip())
            lon = float(parts[1].split(':')[1].strip())
            return lat, lon
        except Exception as e:
            return {"error": "Could not parse the response correctly.", "details": str(e)}

        
class GetWeatherFromJson():
    def __init__(self, weather_data):
        self.weather_data = weather_data

        # Define the prompt template for the language model
        self.template = PromptTemplate(
            input_variables=["weather"],
            template="How was the weather described by {weather}? Be very poetic."
        )

        # Initialize the language model with specified parameters
        self.llm = OpenAI(temperature=0.9, max_tokens=500)

        # Create a chain that combines the language model with the prompt
        self.chain = LLMChain(llm=self.llm, prompt=self.template)

    def weather_description(self):
        # Run the chain with the weather data and return the first response
        response = self.chain.run({"weather": self.weather_data})
        return response[0] if response else "No response generated."
