#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles
of the first 10 hot posts for a given subreddit
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot
    posts for a given subreddit

    :param subreddit: The name of the subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:97.0)"
                             "Gecko/20100101 Firefox/97.0"}
    params = {
        "limit": 10
    }

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        data = response.json()

        if 'data' in data and 'children' in data['data']:
            posts = data.get('data').get('children')
            for post in posts:
                title = post.get('data').get('title')
                print(title)
        else:
            print("None")

        # print(data)

    except Exception:
        print("None")
