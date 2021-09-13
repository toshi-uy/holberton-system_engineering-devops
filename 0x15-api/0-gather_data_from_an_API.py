#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
from sys import argv


if __name__ == "__main__":
    id = argv[1]
    req_users = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(id))
    req_list = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id))
    todo_list = req_list.json()
    users = req_users.json()
    name = users.get('name')
    number_of_tasks = len(todo_list)
    done = 0
    done_tasks = ""
    for task in todo_list:
        complited = task.get('completed')
        if complited:
            done += 1
            done_tasks += "\t {}\n".format(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(
        name, done, number_of_tasks))
    print(done_tasks, end="")
