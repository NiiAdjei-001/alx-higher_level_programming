#!/usr/bin/python3
"""Script to post an email
    argv[1] - url
    argv[2] - email
"""
import requests
import sys


if __name__ == "__main__":
    argv = sys.argv
    if argv.__len__() >= 3:
        url = argv[1]
        data = {
            'email': argv[2]
        }
        res = requests.post(url, data=data)
        print(res.text)
