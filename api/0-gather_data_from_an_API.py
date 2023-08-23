#!/usr/bin/python3
"""0. Gather data from an API"""

import requests
import sys

if __name__ == "__main__":
    users = "https://jsonplaceholder.typicode.com/users/{}"
    todos = "https://jsonplaceholder.typicode.com/todos/?userId={}"

    id = int(sys.argv[1])
    response_users = requests.get(users.format(id)).json()
    response_todos = requests.get(todos.format(id)).json()
    task_count = 0
    task_total = 0
    for task in response_todos:
        if task['userId'] == id:
            task_total += 1
        if task['userId'] == id and task['completed'] is True:
            task_count += 1
    print("Employee {} is done with tasks({}/{}):".format(
        response_users['name'], task_count, task_total))
    for lines in response_todos:
        if lines['userId'] == id and lines['completed'] is True:
            print("\t {}".format(lines['title']))
