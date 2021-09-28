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
                             subreddit + '/hot?limit=10.json',
                             headers=headers, allow_redirects=False)
    if req_hot.status_code == 200:
        hot = req_hot.json().get('data').get('children')
        for title in hot:
            print(title.get('data').get('title'))
    print(None)
