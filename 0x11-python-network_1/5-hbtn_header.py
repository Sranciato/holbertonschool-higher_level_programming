#!/usr/bin/python3
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    response = requests.get(url)
    print(response.headers['X-Request-Id'])
