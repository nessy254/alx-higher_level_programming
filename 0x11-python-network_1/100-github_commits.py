#!/usr/bin/python3
"""
Python script that lists 10 most recent commits from a given GitHub repository
"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    acc_owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(acc_owner, repo)
    req = requests.get(url)
    commits = req.json()
    for commit in commits[:10]:
        print("{}: {}".format(commit.get('sha'),
                              commit.get('commit').get('author').get('name')))
