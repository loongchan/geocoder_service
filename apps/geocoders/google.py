from apps.geocoders.base_geocoder import BaseGeocoder
import json

class Google(BaseGeocoder):
    """Google's flavour of geocoder"""

    def get_lat_lng(self, param_json: json)-> tuple:
        """extract response lat long"""

        lat = param_json['results'][0]['geometry']['location']['lat']
        lng = param_json['results'][0]['geometry']['location']['lng']

        return lat, lng
