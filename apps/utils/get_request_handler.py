from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs, quote_plus
from apps.utils.config import Config
import json

from urllib import request

class GetRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        uri = urlparse(self.path)
        query = parse_qs(uri.query)

        if query.get("address") is None:
            return None

        apiKey = Config().configs['Geocoders'][0]['Google']['apiKey']
        full_uri = 'https://maps.googleapis.com/maps/api/geocode/json?key=' + apiKey + '&address=' + quote_plus(query.get('address')[0])
        answer = request.urlopen(full_uri)
        answer_json = answer.read().decode('utf-8')

        try:
            ja = json.loads(answer_json)
            lat = ja['results'][0]['geometry']['location']['lat']
            lng = ja['results'][0]['geometry']['location']['lng']

            response_txt = '{lat:' + str(lat) + ', long:' + str(lng) + '}'
            self.send_response(200)
            self.end_headers()
            self.wfile.write(response_txt.encode('utf-8'))

            return None
        except:
            print("exitttttt")
            return None

        return None