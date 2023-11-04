#!/usr/bin/python3
"""
gathing data from an api
"""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = int(sys.argv[1])

    file = f"{user_id}.csv"

    r1 = requests.get("https://jsonplaceholder.typicode.com/users")

    users = r1.json()

    r2 = requests.get("https://jsonplaceholder.typicode.com/todos")

    todos = r2.json()

    for user in users:
        if user.get("id") == user_id:
            name = user.get("username")

    with open(file, 'a', newline='') as f:
        header = ["userId", "name", "completed", "title"]
        writer = csv.DictWriter(f, fieldnames=header, quoting=csv.QUOTE_ALL)

        for todo in todos:
            if todo.get("userId") == user_id:
                todo.update({"name": name})
                del todo["id"]
                writer.writerow(todo)
