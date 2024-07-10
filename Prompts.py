import openai

class GetWeatherFromJson():
    def __init__(self, api_key):
        self.client = openai.OpenAI(
                 api_key=api_key,  # this is also the default, it can be omitted
                 )

    def weather_description(self, weather_data):
        
        response = self.client.chat.completions.create( model="gpt-4",
            messages=[{"role": "system", "content": "Generate a poetic description of the weather."}, 
                      {"role": "user", "content": "It is 27 degree and the sun is shining"}],
            temperature=0.9,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        
        # Extract and return the text from the response
        return response.choices[0].message.content.strip() if response.choices else "No response generated."