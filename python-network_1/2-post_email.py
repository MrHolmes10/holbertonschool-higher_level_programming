#!/usr/bin/python3
""" network email"""

import urllib.request
import sys
import urllib.parse

if __name__ == "__main__":
   url = sys.argv[1]
   email = sys.argv[2]
   
   # post  
   data = urllib.parse.urlencode({"email": email}).encode("utf-8")
   
   # post req
   with urllib.request.urlopen(url, data) as urll:
        bod = urll.read()
   # decode
   print(bod.decode("utf-8"))

