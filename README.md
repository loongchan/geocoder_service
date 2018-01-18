# Geocoder Service

This is a simple service which creates a localhost server that can handle RESTful HTTP Interface for Geocoding services.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Requires that the user has:
* Python3.6
* [Google Maps](developer.google.com/maps/documentation/geocoding/start) API Key
* [Here](developer.here.com/documentation/geocoder/topics/quick-start.html) App_ID and App_Code

### Installing

To startup the service:

1. Install Python 3.6
2. Get the codebase
```
git clone git@github.com:loongchan/geocoder_service.git
```
3. Copy the geocoder_config.json.example to geocoder_config.json
```
cp geocoder_config.json.example geocoder_config.json
```
4. Edit geocoder_config.json to add in your own keys for Google and Here api service

5. TADA!  That should be it!

## Deployment

### Starting the Server
```
python startup.py
```
**NOTE:**
* The startup script optionally takes one argument, which specifies the port to use.  Default port is 8000.

###Stopping the Server
Just press CTRL + c on the terminal running where the startup.py script is running.

## Using the service
This current version only runs on localhost.  To use the service, assuming you used the default port of 8000 and setup and deployed properly.  It takes only one GET argument "address", which is what is processed by the geocoder.

eg.
```
http://localhost:8888/?address=425+Market+Street,+425+Market+St,+San+Francisco,+CA
```

## Authors

* **Loong Chan**