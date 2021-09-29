#!/usr/bin/python3
"""
recursive function that queries the Reddit API parses the title of all hot
articles, and prints a sorted count of given keywords (case-insensitive,
delimited by spaces. Javascript should count as javascript, but java
should not).
"""
import requests


def count_words(subreddit, word_list, pagination="", results={}, count=0):
    """
    queries the Reddit API parses the title of all hot
    articles, and prints a sorted count of given keywords
    """
    headers = {"User-Agent": "Mozilla/5.0"}
    url = 'https://www.reddit.com/r/' + subreddit +\
          '/hot.json?after={}'.format(pagination)
    req_hot = requests.get(url, headers=headers, 
                           allow_redirects=False, count=count, limit=100)
    if req_hot.status_code != 200:
        return
    else:
        response = req_hot.json()
        count += results.get('data').get('dist')
        hot = response.get('data').get('children')
        for data in hot:
            title = data.get('data').get('title')
            for word in word_list:
                if word in title.split():
                    times = len([t for t in title.split() if t == word.lower()])
                    if results.get(word) is None:
                        results[word] = times
                    else:
                        results[word] += times
        pagination = response.get('data').get('after')
        if pagination is not None:
            count_words(subreddit, word_list, pagination, results, count)
        else:
            for key, value in sorted(results.items()):
                print("{}: {}".format(key, value))
