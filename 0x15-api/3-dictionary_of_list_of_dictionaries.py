#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""


if __name__ == "__main__":
    import json
    import requests

    req_users = requests.get(
        'https://jsonplaceholder.typicode.com/users/')
    users = req_users.json()
    all_dict = {}

    for user in users:
        user_dict = {}
        tasks_list = []
        req_list = requests.\
            get('https://jsonplaceholder.typicode.com/user/{}/todos'.
                format(user.get('id')))
        todo_list = req_list.json()
        for task in todo_list:
            new_dict = {}
            new_dict["username"] = user.get('username')
            new_dict["task"] = task.get('title')
            new_dict["completed"] = task.get('completed')
            tasks_list.append(new_dict)
        all_dict[user.get('id')] = tasks_list

    with open('todo_all_employees.json', mode='w') as json_file:
        json.dump(all_dict, json_file)
