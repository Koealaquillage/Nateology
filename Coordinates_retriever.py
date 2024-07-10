import requests

class CityCoordinatesGetter():

    def __init__(self, apikey):
        self.base_url = "https://forward-reverse-geocoding.p.rapidapi.com/v1/forward"
        self.querystring =  {"format":"json","city":"city",
                             "accept-language":"en","namedetails":"0","limit":"1","bounded":"0",
                             "polygon_text":"0","polygon_kml":"0","polygon_svg":"0","polygon_geojson":"0",
                             "polygon_threshold":"0.0"}
        self.apikey = apikey
        self.headers = {
	        "x-rapidapi-key": self.apikey,
	        "x-rapidapi-host": "forward-reverse-geocoding.p.rapidapi.com"
            }
    
    def _edit_query_string(self, city_name):
        self.querystring["city"] =  f"{city_name}"
    
    def get_city_coordinates(self, city_name):

        self._edit_query_string(city_name)
        response = requests.get(self.base_url, headers=self.headers, params=self.querystring)
        try:
            data = response.json()
            lat = data[0]['lat']
            lon = data[0]['lon']
            return lat, lon
        except IndexError:  # Handle empty response data
            return {"error": "No results found for the specified city."}
        except KeyError:  # Handle unexpected JSON structure
            return {"error": "Unexpected data format from API response."}
        except Exception as e:  # Handle other exceptions such as connection errors
            return {"error": "Could not retrieve the coordinates.", "details": str(e)}
