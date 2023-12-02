#!/usr/bin/python3
"""Script to display X-Request-Id of an http response
"""
import urllib.request
import sys


if __name__ == "__main__":
    argv = sys.argv
    
    if argv.__len__() >= 2:
        with urllib.request.urlopen(argv[1]) as response:
            print('{}'.format(response.headers['X-Request-Id']))
