#!/usr/bin/python3
"""
Recursive function to query the Reddit API, parse the titles
of all hot articles and print a sorted count of given keywords.
"""

import requests


def count_words(subreddit, word_list, after=None, word_counts=None):
    """
    Recursively queries the Reddit API, parses titles of host articles,
    and prints sorted count of given keywords

    :param subreddit: Name of the subreddit.
    :param word_list: List of keywords to count
    :param after: Param for pagination
    :param word_counts: Dict to store keyword counts
    :return: None
    """
    if word_counts is None:
        word_counts = {}

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
                title = post.get('data').get('title').lower()
                for word in word_list:
                    count = title.count(word.lower())
                    if count > 0:
                        if word in word_counts:
                            word_counts[word] += count
                        else:
                            word_counts[word] = count

            after = data.get('after')
            if after is not None:
                count_words(subreddit, word_list, after, word_counts)
            else:
                print_results(word_counts)

        else:
            pass

    except Exception:
        pass


def print_results(word_counts):
    """
    Prints the results in descending order by count
    & alphabetically for tied counts.

    :param word_counts: Dictionary containing keyword counts
    :return: None
    """
    sorted_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print(f"{word}: {count}")
