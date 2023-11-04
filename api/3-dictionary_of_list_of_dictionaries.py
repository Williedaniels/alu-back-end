#!/usr/bin/python3
"""
gathing data from an api
i"""

import json
import requests
import sys

if __name__ == "__main__":
    file = "todo_all_employees.json"

    r1 = requests.get("https://jsonplaceholder.typicode.com/users")

    users = r1.json()

    r2 = requests.get("https://jsonplaceholder.typicode.com/todos")

    todos = r2.json()

    my_dict = {}
    for user in users:
        value = []
        name = user.get("username")
        user_id = user.get("id")
        for todo in todos:
            if todo.get("userId") == user_id:
                todo.update({"task": todo.get("title")})
                todo.update({"username": name})
                for _ in ["title", "id", "userId"]:
                    del todo[_]
                value.append(todo)
        my_dict[user_id] = value

    with open(file, 'w') as f:
        json.dump(my_dict, f)
