#!/usr/bin/python3
""" task 5"""

import requests 
import sys

if __name__ == "__main__":
   url = sys.argv[1]
   faiq = requests.get(url)
   print(faiq.headers.get("X-Request-Id"))
