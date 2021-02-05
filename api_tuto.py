'''
Tutorial : Getting started with APIs
dataquest.io/blog/python-api-Tutorial

Querying a simple API to retrieve data about the International Space Station
'''

import requests

'''Use Get Request to retrieve data'''

'''
response = requests.get('http://api.open-notify.org/this-api-doesnot-exist')
print(response.status_code) # 404
'''

'''
200: Everything is ok
301: redirecting to a different endpoint. (Somethings has been changed)
400: Bad requests
401: not authenticated
403: forbidden
404: Not found
503: not ready to handle the request
'''

'''
We had better consult the API documentation
Here, we use Open Nofity API
'''

import json

'''
json.dump(): Takes in a Python object, and converts it to a string
json.load(): Tkaes a JSON string and converts it to a Python object
'''

def json_print(obj):
    # create a formatted string of the python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

response = requests.get('http://api.open-notify.org/astros.json')
print(response.status_code) # 200 : successful

print(response.json())

json_print(response.json())

'''
Using an API with Query Parameters
Commonly, API requires us to specify parameters
'''

parameters = {
    'lat': 40.71,
    'lon': -74
}

'''International Space Station Pass Time'''
response = requests.get('http://api.open-notify.org/iss-pass.json'
                            ,params = parameters)
json_print(response.json())

pass_time = response.json()['response']
json_print(pass_time)

'''extract just the five resetime values'''
risetimes = []

for dict in pass_time:
    time = dict['risetime']
    risetimes.append(time)

print(risetimes)

'''To convert time format easier to understand'''
from datetime import datetime

times = []

for rt in risetimes:

    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(time)
