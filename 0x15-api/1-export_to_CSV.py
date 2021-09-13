#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""


if __name__ == "__main__":
    import csv
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
    user_id = req_users.get('id')

    with open('{}.csv'.format(id), mode="w") as csv_file:
        csv_file = csv.writer(csv_file, quotechar='"', quoting=csv.QUOTE_ALL)
        for task in todo_list:
            completed = task.get('completed')
            title = task.get('title')
            csv_file.writerow([user_id, name, completed, title])
