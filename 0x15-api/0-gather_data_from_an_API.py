#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""


if __name__ == "__main__":
    import requests
    from sys import argv


    id = argv[1]
    req_users = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(id))
    req_todo_list = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(id))
    todo_list = req_todo_list.json
    users = req_users.json
    name = users.get('name')
    print("[{}]".format(name))
