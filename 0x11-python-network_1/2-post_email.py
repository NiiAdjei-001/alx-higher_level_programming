#!/usr/bin/python3
"""Script to display X-Request-Id of an http response
"""
from urllib import parse, request
import sys


if __name__ == "__main__":
    argv = sys.argv
    if argv.__len__() >= 3:
        url = argv[1]
        data = {
            'email': argv[2]
        }
        data_encoded = parse.urlencode(data)
        data_bytes = data_encoded.encode('utf-8')
        with request.urlopen(url, data=data_bytes) as response:
            response_data = response.read()
            response_data_str = response_data.decode('utf-8')
            print(response_data_str)
