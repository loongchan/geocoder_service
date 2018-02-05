from apps.geocoders.base_geocoder import BaseGeocoder
import json

class Here(BaseGeocoder):
    """Here's flavour of geocoder"""

    def get_full_url(self) -> str:
        base_url = super().get_full_url()

        extra_params = self.config['Geocoders'][__name__]['extras']

        return base_url + "&" + extra_params

    def get_lat_lng(self, param_json: json)-> tuple:
        """extract response lat long"""

        lat = param_json['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Latitude']
        lng = param_json['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Longitude']

        return lat, lng
