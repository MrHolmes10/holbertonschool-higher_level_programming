#!/usr/bin/python3
"""qaqa bu kimdi """
if  __name__ == "__main__":
    import urllib.request
    import sys
    url = sys.argv[1]
    with urllib.request.urlopen(url) as urll:
         headers = response.info()
         print(headers.get("X-Request-Id"))
