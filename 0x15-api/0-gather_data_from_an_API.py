#!/usr/bin/python3
"""This module defines a function that REST API
to gather information about an employee to-do list
using the given employee ID.

return: Information about his/her TODO list progress
"""

import requests
from sys import argv


def get_employee_todo_progress(emp_id):
    """Uses REST API to fetch data form a resource
    for an employee to-do list
    """
    # endpoints
    user_endpoint = f'https://jsonplaceholder.typicode.com/users/{emp_id}'
    todos = f'https://jsonplaceholder.typicode.com/users/{emp_id}/todos'

    # fetch data
    with requests.get(user_endpoint) as user_response, requests.get(
            todos) as todos_response:
        employee_data = user_response.json()
        todos_data = todos_response.json()

    employee_name = employee_data.get('name')
    completed_tasks = []
    total_tasks = len(todos_data)

    for tasks in todos_data:
        if tasks.get('completed') is True:
            completed_tasks.append(tasks.get('title'))

    print(f'Employee {employee_name} is done with tasks('
          f'{len(completed_tasks)}/{total_tasks}):')

    # Print the completed tasks
    for task_title in completed_tasks:
        print(f'\t\t{task_title}')


if __name__ == "__main__":
    if len(argv) != 2:
        exit(1)
    employee_id = int(argv[1])
    get_employee_todo_progress(employee_id)
