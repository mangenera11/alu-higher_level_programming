#!/usr/bin/python3
"""POSTs an email to a URL and displays the response body"""
import requests
import sys

if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    print(r.text)
