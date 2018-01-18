#!/usr/bin/env python3

import os, sys

package_directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(package_directory, 'apps'))


from http.server import HTTPServer
from apps.utils.get_request_handler import GetRequestHandler


# initialize and start up server
httpServer = HTTPServer(('', 8000), GetRequestHandler)

while True:
    httpServer.handle_request()