#!/usr/bin/python3
"""who am i  """

import requests
import csv

def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print("Status Code: {}").format(response.status_code)

    if response.status_code == 200 :
        data = response.json()
        for pos in data:
            print(pos["title"])


def fetch_and_save_posts():
    """ some code"""
    url = "https://jsonplaceholder.typicode.com/posts"
    res = requests.get(url)

    if res.status_code == 200:
        data = res.json()

        posts_list = [ {
            "id": post["id"],
             "title": post["title"],
                "body": post["body"],
            }
            for post in data
        ]

        # Write to CSV
        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts_list)

