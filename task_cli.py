import sys
import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

# ---------------------------
# Helpers for file I/O
# ---------------------------
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def now():
    return datetime.now().isoformat()

# ---------------------------
# Core Features
# ---------------------------
def add_task(description):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    task = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "createdAt": now(),
        "updatedAt": now()
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task_id})")

def list_tasks(filter_status=None):
    tasks = load_tasks()
    if filter_status:
        tasks = [t for t in tasks if t["status"] == filter_status]
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print(f"{task['id']}. {task['description']} [{task['status']}]")

def migrate_tasks():
    tasks = load_tasks()
    updated = False

    for task in tasks:
        if "id" not in task:
            task["id"] = len(tasks) + 1
            updated = True
        if "description" not in task:
            task["description"] = ""
            updated = True
        if "status" not in task:
            task["status"] = "todo"
            updated = True
        if "createdAt" not in task:
            task["createdAt"] = now()
            updated = True
        if "updatedAt" not in task:
            task["updatedAt"] = now()
            updated = True

    if updated:
        save_tasks(tasks)
        print("Migration complete: tasks.json updated.")
    else:
        print("No migration needed.")

def mark_done(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            task["updatedAt"] = now()
            save_tasks(tasks)
            print(f"Task {task_id} marked as done!")
            return
    print(f"No task found with ID {task_id}")

# ---------------------------
# Help / Usage
# ---------------------------
def print_help():
    print("""
Task Tracker CLI - Commands

Usage:
  python task_cli.py <command> [arguments]

Commands:
  add <description>          Add a new task
  list                       List all tasks
  list todo                  List only tasks with status 'todo'
  list in-progress           List only tasks with status 'in-progress'
  list done                  List only tasks with status 'done'
  mark-done <task_id>        Mark a task as done
  migrate                    Fix old tasks.json to ensure required properties
  help                       Show this help message
""")

# ---------------------------
# CLI Entry Point
# ---------------------------
def main():
    if len(sys.argv) < 2:
        print_help()
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: python task_cli.py add <description>")
            return
        description = " ".join(sys.argv[2:])
        add_task(description)

    elif command == "list":
        status = sys.argv[2] if len(sys.argv) > 2 else None
        list_tasks(status)

    elif command == "migrate":
        migrate_tasks()

    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Usage: python task_cli.py mark-done <task_id>")
            return
        try:
            task_id = int(sys.argv[2])
            mark_done(task_id)
        except ValueError:
            print("Task ID must be a number.")

    elif command == "help":
        print_help()

    else:
        print(f"Unknown command: {command}")
        print("Use: python task_cli.py help")

if __name__ == "__main__":
    main()
