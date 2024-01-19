#!/usr/bin/python3
"""
    Defines a function that quires the Reddit API
    Returns:
            the number of subscribers(not active users,
                                      total subscribers)
            for a given subreddit.
            if subreddit is invalid, return 0
"""

import requests


def number_of_subscribers(subreddit):
    """
        Queries the Reddit API
        returns the number of subscribers for a given reddit
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:97.0)"
                             "Gecko/20100101 Firefox/97.0"}

    response = requests.get(url, headers=headers,
                            allow_redirects=False)

    data = response.json()

    try:
        return data.get('data').get('subscribers')

    except Exception:
        return 0
