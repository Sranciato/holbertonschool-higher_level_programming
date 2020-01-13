#!/usr/bin/python3
import requests
from sys import argv

if __name__ == "__main__":
    response = requests.post(argv[1], {"email": argv[2]})
    print(response.text)
