#!/usr/bin/python3
from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    data = parse.urlencode({"email": argv[2]}).encode()
    with request.urlopen(argv[1], data) as f:
        print(f.read().decode('utf-8'))
