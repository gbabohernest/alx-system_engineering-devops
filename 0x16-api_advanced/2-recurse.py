#!/usr/bin/python3
"""
Recursive function to query the Reddit API
Return a list of titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries the Reddit API and appends
    titles of hot articles to the hot_list.

    :param subreddit: Name of the subreddit
    :param hot_list: List to store titles
    :param after: pagination param
    :return: List containing title of hot articles or None
    """

    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json?".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:97.0)'
                             'Gecko/20100101 Firefox/97.0'}

    params = {
       "limit": 100,
       "after": after
    }

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        data = response.json().get("data")

        if data and 'children' in data:
            posts = data.get('children')
            for post in posts:
                title = post.get('data').get('title')
                hot_list.append(title)

            after = data.get('after')
            if after is not None:
                recurse(subreddit, hot_list, after)
            return hot_list

        else:
            return None

    except Exception:
        return None
