#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""


if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    id = argv[1]
    req_users = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(id))
    req_list = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id))
    todo_list = req_list.json()
    users = req_users.json()
    name = users.get('username')
    user_id = users.get('id')
    tasks = []
    jaison = {}

    for task in todo_list:
        dic = {}
        dic['task'] = task.get('title')
        dic['completed'] = task.get('completed')
        dic['username'] = name
        tasks(dic)
    jaison[id] = tasks

    with open("{}.json".format(id), "w")as f:
        json.dump(jaison, f)
