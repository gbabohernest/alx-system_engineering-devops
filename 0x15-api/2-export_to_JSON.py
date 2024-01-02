#!/usr/bin/python3
"""This module defines a function that uses REST API
gather data about employee and export data in JSON format
"""

import json
import requests
from sys import argv


def export_to_json(emp_id):
    """Uses REST API to fetch data from resources, export
    employee data fetched from an endpoint into a JSON format
    """

    # endpoints
    user_endpoint = f'https://jsonplaceholder.typicode.com/users/{emp_id}'
    todos = f'https://jsonplaceholder.typicode.com/users/{emp_id}/todos'

    with requests.get(user_endpoint) as user_response, requests.get(
            todos) as todos_response:
        employee_data = user_response.json()
        todos_data = todos_response.json()

    username = employee_data.get('username')
    user_id = employee_data.get('id')

    json_file_name = f'{user_id}.json'

    employee_todos = [
        {
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": username
        }
        for todo in todos_data
    ]
    employee_data_json = {str(user_id): employee_todos}

    with open(json_file_name, 'w') as fd:
        json.dump(employee_data_json, fd)


if __name__ == "__main__":
    if len(argv) != 2:
        exit(1)
    employee_id = int(argv[1])
    export_to_json(employee_id)
