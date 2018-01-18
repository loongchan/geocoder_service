from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from apps.geocoders import Geocoder


class GetRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        # parse the get url
        uri = urlparse(self.path)
        query = parse_qs(uri.query)

        # only care about get requests that has the "address" parameter
        if query.get("address") is None:
            return None

        # try to get
        geocoder = Geocoder()
        answer = geocoder.get_geocode(query.get("address")[0])

        if answer == "":
            self.send_response(503)
            self.end_headers()
            self.wfile.write("Whoops, something went wonky with the geocoders.  Please try again later.".encode('utf-8'))
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(answer.encode('utf-8'))

        return None