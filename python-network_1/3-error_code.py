#!/usr/bin/python3
"""Displays the response body, or the HTTP error code"""
import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as res:
            print(res.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
