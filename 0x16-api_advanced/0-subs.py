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
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    req_users = requests.get('https://www.reddit.com/r/' + subreddit + '/about.json', headers=headers, allow_redirects=False)
    if req_users.status_code == 404:
        print("error")
        return 0
    users = req_users.get('data')
    print(users)
    return 20
