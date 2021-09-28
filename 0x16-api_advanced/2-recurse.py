#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], pagination=""):
    """
    queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit or None
    """
    headers = {"User-Agent": "Mozilla/5.0"}
    url = 'https://www.reddit.com/r/' + subreddit +\
          '/hot.json??after={}'.format(pagination)
    req_hot = requests.get(url, headers=headers, allow_redirects=False)
    if req_hot.status_code != 200:
        return None
    response = req_hot.json()
    hot = response.get('data').get('children')
    for data in hot:
        hot_list.append(data.get('data').get('title'))
        pagination = response.get('data').get('after')
        if pagination is not None:
            recurse(subreddit, hot_list, pagination)
    return hot_list
