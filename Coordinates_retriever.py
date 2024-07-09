from opencage.geocoder import OpenCageGeocode
from secret_key import opencagedata_key

class CityCoordinatesGetter():

    def __init__(self, city_name):
        self.city_name = city_name
        OCG = OpenCageGeocode('opencagedata_key')

    def get_city_coordinates(self):
        results = OCG.geocode(f'{self.city_name}')
        print(u'%f;%f;%s;%s' % (results[0]['geometry']['lat'],
                        results[0]['geometry']['lng'],
                        results[0]['components']['country_code'],
                        results[0]['annotations']['timezone']['name']))
        # Using regex to find the coordinates in the response
        try:
            lat = results[0]['geometry']['lat']
            lon = results[0]['geometry']['lon']
            return lat, lon
        except Exception as e:
            return {"error": "Could not parse the response correctly.", "details": str(e)}