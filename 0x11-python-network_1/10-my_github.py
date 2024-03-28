#!/usr/bin/python3
"""
A Python script that uses the Github API to display the ID of the user
"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    req = requests.get('https://api.github.com/user',
                       auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    print(req.json().get('id'))
