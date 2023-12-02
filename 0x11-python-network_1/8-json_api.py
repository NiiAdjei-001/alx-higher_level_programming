#!/usr/bin/python3
"""Script to query a server by name
    argv[1] - q
"""
import requests
import sys


if __name__ == "__main__":
    q = sys.argv[1] if sys.argv.__len__() >= 2 else ""
    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': f"{q}"}
    res = requests.post(url, params=payload)
    # print(res.url)
    # print (res.status_code)
    if res.status_code == requests.codes.ok:
        try:
            dic = res.json()
            # print(dic)
            # print(dic.__len__())
            if (dic.__len__() == 0):
                print("No result")
            else:
                print("[{}] {}".format(dic['id'], dic['name']))
        except Exception:
            print("Not a valid JSON")
    res.close()
