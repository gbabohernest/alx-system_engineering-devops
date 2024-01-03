#!/usr/bin/python3
"""This module defines a function that uses REST API
gather data about employees and export data in JSON format
"""

import json
import requests
# from sys import argv


def get_all_employees_todo():
    """Uses REST API to fetch data from resources, export
    employee data fetched from an endpoint into a JSON format
    """

    # endpoint
    user_endpoint = f'https://jsonplaceholder.typicode.com/users'

    with requests.get(user_endpoint) as user_response:
        employees_data = user_response.json()

        all_employees_data = {}

        for employee in employees_data:
            usr_id = employee.get('id')
            usr_name = employee.get('username')

            todos = (f'https://jsonplaceholder.typicode.com/'
                     f'users/{usr_id}/todos')

            with requests.get(todos) as todos_response:
                todos_data = todos_response.json()

            employee_todos = [
                {
                    "username": usr_name,
                    "task": todo.get('title'),
                    "completed": todo.get('completed'),

                }
                for todo in todos_data
            ]
            all_employees_data[str(usr_id)] = employee_todos

    json_file_name = 'todo_all_employees.json'
    with open(json_file_name, 'w') as fd:
        json.dump(all_employees_data, fd)


if __name__ == "__main__":
    get_all_employees_todo()
