#!/usr/bin/python3
"""
Python script that Takes in a URL, sends a request to the URL and
displays the body of the
response (decoded in utf-8). If the HTTP status code is greater than or
equal to 400, print: Error code: followed by the value of the HTTP status
"""
import requests
import sys


if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
