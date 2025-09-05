import sys
import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

# Ensure JSON file exists
if not os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, "w") as f:
        json.dump([], f)

def load_tasks():
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(description):
    tasks = load_tasks()

    # Generate new id (1 higher than last id, or 1 if list empty)
    new_id = tasks[-1]["id"] + 1 if tasks else 1

    now = datetime.now().isoformat(timespec="seconds")

    new_task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }

    tasks.append(new_task)
    save_tasks(tasks)

    print(f'Task added successfully (ID: {new_id})')

def main():
    if len(sys.argv) < 2:
        print("Usage: python task_cli.py <command> [arguments]")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Error: Missing task description.")
        else:
            description = " ".join(sys.argv[2:])
            add_task(description)

    elif command == "list":
        tasks = load_tasks()
        if not tasks:
            print("No tasks found.")
        else:
            for task in tasks:
                print(f"[{task['id']}] {task['description']} - {task['status']}")

    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
