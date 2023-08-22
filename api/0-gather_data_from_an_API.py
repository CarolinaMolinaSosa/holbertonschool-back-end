#!/usr/bin/python3
"""0. Gather data from an API"""


import requests
import sys

if __name__ == "__main__":
    user_url = "https://jsonplaceholder.typicode.com/users/{}"
    todo_url = "https://jsonplaceholder.typicode.com/todos/?userId={}"

    employee_id = int(sys.argv[1])
    user_data = requests.get(user_url.format(employee_id)).json()
    tasks_data = requests.get(todo_url.format(employee_id)).json()
    completed_task_count = 0
    total_task_count = 0

    for task in tasks_data:
        if task['userId'] == employee_id:
            total_task_count += 1
        if task['userId'] == employee_id and task['completed'] is True:
            completed_task_count += 1

    print("Employee {} is done with tasks({}/{}):".format(
        user_data['name'], completed_task_count, total_task_count))

    for task in tasks_data:
        if task['userId'] == employee_id and task['completed'] is True:
            print("\t{}".format(task['title']))
