#!/usr/bin/python3
""" git hub """

if __name__ == "__main__":
    import sys
    import requests
    username = sys.argv[1]
    passwd = sys.argv[2]

    url = "https://api.github.com/user"

    ans = requests.get(url, auth=(username, passwd))

    try:
        data = ans.json()
        print(data.get("id"))
    except ValueError:
        print("None")
