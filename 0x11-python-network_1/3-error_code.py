#!/usr/bin/python3
"""
A python script that takes in a URL, sends a request
to the URL and displays the body of the
response (decoded in utf-8).
"""
import urllib.request
import sys
import urllib.error


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
