#!/usr/bin/python3
import requests
import sys

def get_employee_todo_progress(employee_id):
    """
    Retrieve and display an employee's TODO list progress.

    Args:
    employee_id (int): The ID of the employee.

    Returns:
    None: This function prints the progress information.
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    try:
        # Retrieve user information
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user_data = user_response.json()

        # Retrieve TODO list for the user
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        total_tasks = len(todos_data)
        completed_tasks = [task for task in todos_data if task['completed']]

        # Print the progress information
        print(f'Employee {user_data["name"]} is done with tasks ({len(completed_tasks)}/{total_tasks}):')

        for task in completed_tasks:
            print(f'\t{task["title"]}')
    
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python todo_progress.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)

