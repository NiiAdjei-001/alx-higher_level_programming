#!/usr/bin/python3
"""Script to display X-Request-Id of an http response
"""
import requests
import sys


if __name__ == "__main__":
    argv = sys.argv

    if argv.__len__() >= 2:
        try:
            res = requests.get(argv[1])
            print('{}'.format(res.headers['X-Request-Id']))
        except Exception:
            pass
