#!/usr/bin/python3
"""who am i  """

import urllib.error
import urllib.request
import sys

if  __name__ == "__main__":
    url = sys.argv[1]

    try :
        with urllib.request.urlopen(url) as urll:
            ans = urll.read()
            ans = ans.decode()
    except urllib.error.HTTPError as E:
        print("Error code: {}".format(E.code))
