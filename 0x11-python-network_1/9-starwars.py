#!/usr/bin/python3
import requests
from sys import argv

if __name__ == "__main__":
    json = requests.get(
        "https://swapi.co/api/people/?search={}".format(argv[1])
    ).json()
    print("Number of results: {}".format(json['count']))
    for results in json['results']:
        print(results['name'])
