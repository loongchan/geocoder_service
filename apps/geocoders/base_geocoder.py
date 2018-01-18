from abc import ABC, abstractmethod
from urllib import request
from urllib.parse import quote_plus

import json

class BaseGeocoder(ABC):
    """Base class to get geocoder info from website"""

    def __init__(self, param_config, param_request: request, param_address: str) -> None:
        """init class"""
        self.config = param_config
        self.request = param_request
        self.address = param_address
        self.own_name = __name__

    @abstractmethod
    def get_own_name(self):
        pass

    def get_full_url(self, which_geocoder: str) -> str:
        """create implementation specific URL"""
        ownConf = self.config['Geocoders'][which_geocoder]
        ownURL = ownConf['url']
        apiKey = ownConf['apiKey']
        apiKeyParam = ownConf['apiParameter']
        queryParam = ownConf['queryParameter']

        return ownURL + "?" + apiKeyParam + "=" + apiKey + "&" + queryParam + "=" + quote_plus(self.address)

    @abstractmethod
    def get_lat_lng(self, param_json: json)-> tuple:
        """extract implementation specific response"""
        pass

    def get_geocoder_answer(self) -> str:
        """calls geocoder and returns json of {lat: xxx, long: xxx}"""

        # get full request url
        full_url = self.get_full_url(self.get_own_name())

        # find geocoder response
        answer = request.urlopen(full_url)

        # check if it works
        if answer.code is 200:
            try:
                # get lat/lng
                json_answer = json.loads(answer.read().decode('utf-8'))
                lat, lng = self.get_lat_lng(json_answer)

                return '{lat:' + str(lat) + ', lng:' + str(lng) + '}'

            except Exception:
                print("Whoops, something went wrong with " + __name__)
                return ""
        else:
            return ""



