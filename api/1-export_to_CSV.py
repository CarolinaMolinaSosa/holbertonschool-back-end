#!/usr/bin/python3
"""1-export_to_CSV"""

import requests
import sys

if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users/{}"
    todos_url = "https://jsonplaceholder.typicode.com/todos/?userId={}"

    user_id = int(sys.argv[1])
    user_response = requests.get(users_url.format(user_id)).json()
    todos_response = requests.get(todos_url.format(user_id)).json()

    with open('{}.csv'.format(user_id), 'w') as file_csv:
        for todo in todos_response:
            if todo['userId'] == user_id:
                file_csv.write('"{}","{}","{}","{}"\n'.format(
                    user_id, user_response['username'],
                    todo['completed'], todo['title']))
