#!/usr/bin/python3
"""2-export_to_JSON"""

import json
import requests
import sys

if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users/{}"
    todos_url = "https://jsonplaceholder.typicode.com/todos/?userId={}"

    user_id = int(sys.argv[1])
    user_response = requests.get(users_url.format(user_id)).json()
    todos_response = requests.get(todos_url.format(user_id)).json()

    data_list = []
    for todo in todos_response:
        if todo['userId'] == user_id:
            data_list.append({
                "task": todo['title'],
                "completed": todo['completed'],
                "username": user_response['username']
            })

    json_file_name = f"{user_id}.json"
    with open(json_file_name, 'w') as file_json:
        json.dump({str(user_id): data_list}, file_json)

    print(f"Data exported to {json_file_name}")
