#!/usr/bin/python3
"""This module defines a function that uses REST API
gather data about employee and export to CSV file
"""

import csv
import requests
from sys import argv


def export_to_csv(emp_id):
    """Uses REST API to fetch data from resources, export
    employee data fetched from an endpoint into a csv file
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

    csv_file_name = f'{user_id}.csv'

    with open(csv_file_name, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        # write todos data
        for task in todos_data:
            task_completed_status = task.get('completed')
            task_title = task.get('title')

            csv_writer.writerow([user_id, username,
                                 task_completed_status, task_title])


if __name__ == "__main__":
    if len(argv) != 2:
        exit(1)
    employee_id = int(argv[1])
    export_to_csv(employee_id)
