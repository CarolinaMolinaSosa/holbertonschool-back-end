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
    task_count = 0
    task_total = 0
    formatted_tasks = []
    for task in tasks_data:
        if task['userId'] == employee_id:
            task_total += 1
        if task['userId'] == employee_id and task['completed'] is True:
            task_count += 1
            formatted_tasks.append("\t{}".format(task['title']))

    print("Employee {} is done with tasks({}/{}):".format(
        user_data['name'], task_count, task_total))

    for task_title in formatted_tasks:
        print(task_title)
