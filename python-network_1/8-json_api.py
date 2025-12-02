#!/usr/bin/python3
""" tasks json"""

import requests
import sys
if __name__ == "__main__":
    if len( sys.argv[1])>0:
       q = sys.argv[1]
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": q}
    
    
   try:
       faiq = requests.post(url, data=data)
       faiqjson = faiq.json()
       
       if faiqjson :
           print("[{}] {}".format(faiqjson.get("id"), faiqjson.get("name")))
       else:
           print("No result")
   except ValueError:
       print("Not a valid JSON")
