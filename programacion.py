#!/usr/bin/python3
import requests

def getJSON(api_endpoint):
    response = requests.get(url=api_endpoint)
    return response.json()

if __name__ == "__main__":
    url="https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"
    data = getJSON(url)
    