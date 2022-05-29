import json

import requests

def get_colour_list():
    url = 'http://colormind.io/list/'
    response = requests.get(url)
    return response.json()

def random_colour_scheme(model="default"):
    url = 'http://colormind.io/api/'
    response = requests.post(url, data=json.dumps({"model":model}).encode())
    colours = response.json()['result']
    #convert to rgb to hex
    return ["#" + ''.join([hex(element)[2:] for element in colour]) for colour in colours]

print(get_colour_list())