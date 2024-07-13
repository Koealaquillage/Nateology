import openai

class GetWeatherFromJson():
    def __init__(self, api_key):
        self.client = openai.OpenAI(
                 api_key=api_key,  # this is also the default, it can be omitted
                 )

    def weather_description(self, weather_data):
        
        response = self.client.chat.completions.create( model="gpt-4",
            messages=[{"role": "system", "content": "Hello! You are a chatbot that predicts personnality according on the weather. A clear sky means that you are open to higher, abstract thinking as well as esoteric view. The presence of humidity means you are connected to the world because of the cycle of water, while the absence means you are more focus on your direct surroundings and your inner self. The heat means you are easygoing and easily communicate with people, while the cold goes rather for a rich inner world. Rain or precipitation means you are patient because you are preparing the soil of your personnality and will be ready to grow, while a dry climate means you are more spontaneous and live in the moment.No need for the summary at the beginning. Just write very nice paragraphs, a bit lyrical with a vocabulary that uses a lot of nature metaphors.Two things: Be abstract - don't precise the temperature. Also, it was the weather on the day of birth. It is not the weather today, so it is in the past."}, 
                      {"role": "user", "content": f"The weather was {weather_data}"}],
            temperature=0.9,
            max_tokens=500,
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