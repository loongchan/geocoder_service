#!/usr/bin/env python3

import os
import sys

package_directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(package_directory, 'apps'))


from http.server import HTTPServer
from apps.utils.get_request_handler import GetRequestHandler


# main entry point to start up Geocoding service
if __name__ == "__main__":

    #default port is 8000, but you can specify port by passing in integer as first argument to calling startup.py
    port = 8000
    if len(sys.argv) == 2:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("First argument must be an integer that specifies the port number.")
            exit(1)

    # initialize and start up server
    httpServer = HTTPServer(('', port), GetRequestHandler)

    while True:
        httpServer.handle_request()