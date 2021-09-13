#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    if type(argv[1]) is int:
        users = requests.get('https://jsonplaceholder.typicode.com/users')
        todo_list = requests.get('https://jsonplaceholder.typicode.com/todos')
        print("\t- users:", todo_list.text)
        print("\t- users:", users.text)
