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
    header = {'User-Agent': 'android:com.example.myredditapp:v1.2.3 (by /u/kemitche)'}
    req_users = requests.get('https://www.reddit.com/r/' + subreddit + '/mine/subscribers.json', allow_redirects=False)
    if req_users.status_code == 404:
        print("404")
        return 0
    users = req_users.json()
    return users.get('count')
