import re
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI


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
