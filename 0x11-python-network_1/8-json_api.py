#!/usr/bin/python3
import requests
from sys import argv

if __name__ == "__main__":

    if len(argv) < 2:
        q = ""
    else:
        q = argv[1]

    try:
        response = requests.post(
            "http://0.0.0.0:5000/search_user",
            data={'q': q}
        ).json()
    except ValueError:
        print("Not a valid JSON")
    if response == {}:
        print("No result")
    else:
        print("[{}] {}".format(response['id'], response['name']))
