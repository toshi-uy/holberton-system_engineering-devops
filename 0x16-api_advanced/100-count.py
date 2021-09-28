#!/usr/bin/python3
"""
recursive function that queries the Reddit API parses the title of all hot
articles, and prints a sorted count of given keywords (case-insensitive,
delimited by spaces. Javascript should count as javascript, but java
should not).
"""
import requests


def count_words(subreddit, word_list, pagination="", results={}):
    """
    queries the Reddit API parses the title of all hot
    articles, and prints a sorted count of given keywords
    """
    headers = {"User-Agent": "Mozilla/5.0"}
    url = 'https://www.reddit.com/r/' + subreddit +\
          '/hot.json?after={}'.format(pagination)
    req_hot = requests.get(url, headers=headers, allow_redirects=False)
    if req_hot.status_code != 200:
        return
    else:
        response = req_hot.json()
        hot = response.get('data').get('children')
        for data in hot:
            title = data.get('data').get('title').encode()
            for i in word_list:
                for j in title.split():
                    print(j)
                    if i in title.split(' '):
                        if results[i]:
                            results[i] += 1
                        else:
                            results[i] = 1
        pagination = response.get('data').get('after')
        if pagination is not None:
            count_words(subreddit, word_list, pagination, results)
        print(results)
