
###### Initial connection to Propublica  #######
import requests

# This is the get function he set up in class

def get(url):
    headers = {"X-API-KEY": "WWSGHLJjWxC2m9tznYILCKy1xtmkvnxxdo8nEBt8"}
    url = "https://api.propublica.org/congress/v1" + url
    data = requests.get(url, headers=headers).json()
    return data['results']