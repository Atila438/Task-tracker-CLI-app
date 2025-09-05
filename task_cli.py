import sys
import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"


# ----------------------------
# Helpers
# ----------------------------
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
        json.dump(tasks, f, indent=4)


# ----------------------------
# Commands
# ----------------------------
def add_task(description):
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "description": description,
        "done": False,  # new field
        "status": "todo",  # new field
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {description}")


def list_tasks(filter_status=None):
    tasks = load_tasks()

    if filter_status:
        tasks = [t for t in tasks if t.get("status", "todo") == filter_status]

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        status = "✓" if task.get("done", False) else "X"
        print(f"{task['id']}. [{status}] {task['description']} ({task.get('status', 'todo')})")


def migrate_tasks():
    """One-time migration to add 'done' and 'status' to old tasks"""
    tasks = load_tasks()
    updated = False

    for task in tasks:
        if "done" not in task:
            task["done"] = False
            updated = True
        if "status" not in task:
            task["status"] = "todo"
            updated = True

    if updated:
        save_tasks(tasks)
        print("Migration complete: tasks.json updated.")
    else:
        print("No migration needed.")


# ----------------------------
# Main CLI entry
# ----------------------------
def main():
    if len(sys.argv) < 2:
        print("Usage: python task_cli.py [add|list|migrate] <args>")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: python task_cli.py add <task description>")
            return
        description = " ".join(sys.argv[2:])
        add_task(description)

    elif command == "list":
        if len(sys.argv) == 2:
            list_tasks()
        else:
            filter_status = sys.argv[2]
            list_tasks(filter_status)

    elif command == "migrate":
        migrate_tasks()

    else:
        print("Unknown command. Use add, list, or migrate.")


if __name__ == "__main__":
    main()
