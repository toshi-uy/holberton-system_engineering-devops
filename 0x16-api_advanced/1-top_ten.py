#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts listed for a given
    subreddit or None if fails
    """
    headers = {"User-Agent": "Mozilla/5.0"}
    req_hot = requests.get('https://www.reddit.com/r/' +
                             subreddit + '/hot.json?limit=10',
                             headers=headers, allow_redirects=False)
    if req_hot.status_code == 200:
        hot = req_hot.json().get('data').get('children')
        for data in hot:
            title = data.get('data').get('title')
            title.enconde('ascii')
            print(title)
    print(None)
