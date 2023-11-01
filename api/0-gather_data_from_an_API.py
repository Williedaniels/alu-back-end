#!/usr/bin/python3
import sys
import requests

# Define the base URL for the API
BASE_URL = 'https://jsonplaceholder.typicode.com'

# Accept the employee ID as a command-line argument
employee_id = int(sys.argv[1])

# Send a GET request to the API to retrieve the employee's TODO list
response = requests.get(f'{BASE_URL}/todos?userId={employee_id}')

# Parse the JSON response to extract the relevant information
todos = response.json()

# Calculate the number of completed tasks and the total number of tasks
num_completed_tasks = sum(1 for todo in todos if todo['completed'])
total_tasks = len(todos)

# Display the progress information in the specified format
employee_name = requests.get(f'{BASE_URL}/users/{employee_id}').json()['name']
print(f'Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):')
for todo in todos:
    if todo['completed']:
        print(f'\t{todo["title"]}')
