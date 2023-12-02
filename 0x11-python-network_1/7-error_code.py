#!/usr/bin/python3
"""Sends a request to URL and displays body of response (utf-8)
    argv[1] - url
"""
import requests
import sys


if __name__ == "__main__":
    argv = sys.argv
    if argv.__len__() >= 2:
        url = argv[1]
        res = requests.get(url)
        if res.status_code == requests.codes.ok:
            print(res.text)
        else:
            print("Error code: {}".format(res.status_code))
