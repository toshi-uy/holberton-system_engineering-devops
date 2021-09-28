#!/usr/bin/python3
"""
Function that queries the Reddit API
and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    returns the number of subribers of a subreddit or 0 if fails
    """
    headers = {"User-Agent": "Mozilla/5.0"}
    req_users = requests.get('https://www.reddit.com/r/' + subreddit + '/about.json',
                             headers=headers, allow_redirects=False)
    if req_users.status_code == 200:
        users = req_users.json().get('data')
        return users.get('subscribers')
    return 0
