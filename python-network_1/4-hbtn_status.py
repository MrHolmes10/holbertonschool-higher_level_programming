#!/usr/bin/python3
""" 4 -task """

import requests

if __name__ == "__main__":
    faiq  = requests.get("https://intranet.hbtn.io/status")
    faiq = faiq.text

    print("Body response:")
    print("\t- type: {}".format(type(faiq)))
    print("\t- content: {}".format(faiq))
