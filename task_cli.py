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

def main():
    if len(sys.argv) < 2:
        print("Usage: python task_cli.py <command> [arguments]")
        return
