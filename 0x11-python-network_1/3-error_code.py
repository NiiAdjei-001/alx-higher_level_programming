#!/usr/bin/python3
"""Sends a request to URL and displays body of response (utf-8)
    argv[1] - url
"""
from urllib import error, request
import sys


if __name__ == "__main__":
    argv = sys.argv
    if argv.__len__() >= 2:
        url = argv[1]
        try:
            with request.urlopen(url) as response:
                response_data = response.read()
                response_data_str = response_data.decode('utf-8')
                print(response_data_str)
        except error.HTTPError as err:
            print("Error code: {}".format(err.code))
