#!/usr/bin/python3
"""3-dictionary_of_list_of_dictionaries"""

import json
import requests

if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users_response = requests.get(users_url).json()
    todos_response = requests.get(todos_url).json()

    data_dict = {}
    for user in users_response:
        user_id = user['id']
        username = user['username']
        tasks = []

        for todo in todos_response:
            if todo['userId'] == user_id:
                tasks.append({
                    "username": username,
                    "task": todo['title'],
                    "completed": todo['completed']
                })

        data_dict[str(user_id)] = tasks

    json_file_name = "todo_all_employees.json"
    with open(json_file_name, 'w') as file_json:
        json.dump(data_dict, file_json)
