#!/usr/bin/python3
"""Defines a function that quires the Reddit API
    Returns:
            the number of subscribers(not active users,
                                      total subscribers)
            for a given subreddit.
            if subreddit is invalid, return 0
"""

import json
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API
       returns the number of subscribers for a given reddit
    """
    url = 'https://www.reddit.com/r/{}/about/.json'.format(subreddit)
    headers = {"user-agent": "user"}

    try:

        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            subscribers = data.get("data").get("subscribers")
            return subscribers

        return 0

    except Exception:
        return 0
