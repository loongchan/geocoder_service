from apps.utils.config import Config
from apps.geocoders.google import Google
from apps.geocoders.here import Here
from urllib import request
import json


class Geocoder:
    def __init__(self):
        self.config = Config().configs
        self.request = request

    def get_geocode(self, param_address: str) -> json:
        """gets geocode and has failover"""

        # get geocoders
        google_geocoder = Google(self.config, self.request, param_address)
        here_geocoder = Here(self.config, self.request, param_address)

        # try Google geocoder
        answer = google_geocoder.get_geocoder_answer()

        # if google fails, try Here
        if answer == "":
            answer = here_geocoder.get_geocoder_answer()

        return answer