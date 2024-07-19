import openai
from chatbot_instructions import chatbot_instructions

class GetWeatherFromJson():
    def __init__(self, api_key):
        self.client = openai.OpenAI(
                 api_key=api_key,  # this is also the default, it can be omitted
                 )

    def weather_description(self, weather_data):
        
        response = self.client.chat.completions.create( model="gpt-4",
            messages=[{"role": "system", "content": chatbot_instructions}, 
                      {"role": "user", "content": f"The weather was {weather_data}"}],
            temperature=0.9,
            max_tokens=600,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        
        # Extract and return the text from the response
        return response.choices[0].message.content.strip() if response.choices else "No response generated."
    
    def text_to_speech(self, input_text):
        response = self.client.audio.speech.create(
            model="tts-1",
            voice="nova",
            input=input_text
        )
        webm_file_path = "temp_audio_play.mp3"
        with open(webm_file_path, "wb") as f:
            response.stream_to_file(webm_file_path)
        return webm_file_path