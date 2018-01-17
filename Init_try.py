#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs, quote_plus
from urllib import request
import json


# handles get requests from HTTPServer
class RequestHandler(BaseHTTPRequestHandler):
    # deals with GET request
    def do_GET(self):
        # process get URL to get the address attribute from GET path
        uri = urlparse(self.path)
        query = parse_qs(uri.query)

        # create url that works with google geocoder
        apiKey = '<put google api key>'
        full_uri = 'https://maps.googleapis.com/maps/api/geocode/json?key=' + apiKey + '&address=' + quote_plus(
            query.get('address')[0])

        # get response from geocoder
        answer = request.urlopen(full_uri)
        answer_json = answer.read().decode('utf-8')

        # pull lat / long from
        ja = json.loads(answer_json)
        lat = ja['results'][0]['geometry']['location']['lat']
        lng = ja['results'][0]['geometry']['location']['lng']

        # create response and return
        response_txt = '{lat:' + str(lat) + ', lng:' + str(lng)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(response_txt.encode('utf-8'))


# start up HTTP Server to take requests
from http.server import HTTPServer

httpServer = HTTPServer(('', 8000), RequestHandler)

while True:
    httpServer.handle_request()
