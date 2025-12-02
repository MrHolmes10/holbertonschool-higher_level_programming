#!/usr/bin/python3
""" task 7"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    
    data = {"email": email}
    fako = requests.post(url, data=data)
    print(faiq.text)
