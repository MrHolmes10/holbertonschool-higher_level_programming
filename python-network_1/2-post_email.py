#!/usr/bin/python3

""" network email"""

if _name__ == "__main__":
   import urllib.request
   import sys
   import urllib.parse
   url = sys.argv[1]
   email = sys.argv[2]
  
   data = urllib.parse.urlencode({"email": email}).encode("utf-8")

   with urllib.request.urlopen(url, data) as urll:
        bod = urll.read()
   
   print(body.decode("utf-8"))

