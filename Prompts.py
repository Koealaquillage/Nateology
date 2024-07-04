import re
from langchain import LLMChain, PromptTemplate
from langchain.llms import OpenAI


class CityCoordinatesGetter():

    def __init__(self, city_name):
        self.city_name = city_name
        self.lat = None
        self.lon = None

        self.template =  PromptTemplate(
                             input_variables=["city"],
                             template="What are the latitude and longitude coordinates of {city}?"
                            )

        self.llm = OpenAI(temperature=0, max_tokens=30) 

        self.chain = LLMChain(llm=self.llm, prompt=self.template)

    def get_city_coordinates(self):
        response = self.chain.run({"city": self.city_name})
    
        # Using regex to find the coordinates in the response
        match = re.search(r"(-?\d+\.\d+)[^\d,]+(-?\d+\.\d+)", response)
        if match:
            self.lat = float(match.group(1))
            self.lon = float(match.group(2))
            return [lat, lon]
        else:
            return "Coordinates not found in the response."
        
class GetWeatherFromjson():

    def __init__(self, weather_data):
        self.weather_data = weather_data

        self.template =  PromptTemplate(
                             input_variables=["weather"],
                             template="How was the weather described by {weather}? Be very poetic"
                            )

        self.llm = OpenAI(temperature=0.9, max_tokens=500) 

        self.chain = LLMChain(llm=self.llm, prompt=self.template)

    def weather_description(self):
        response = self.chain.run({"weather": self.weather_data})
    
        return response[0]