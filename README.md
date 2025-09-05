# Task Tracker CLI

A simple **command line interface (CLI)** application to track and manage your tasks. This project allows you to add, update, delete, and mark tasks as `todo`, `in-progress`, or `done`. Tasks are stored in a local **JSON file** for persistence.  

This project is part of the [roadmap.sh projects](https://roadmap.sh/projects/task-tracker) collection.

---

## Features

- Add new tasks  
- Update existing tasks  
- Delete tasks  
- Mark tasks as:
  - **todo** (default when created)  
  - **in-progress**  
  - **done**  
- List tasks:
  - All tasks  
  - Only `done` tasks  
  - Only `todo` tasks  
  - Only `in-progress` tasks  

---

## Task Properties

Each task is stored with the following properties:  

- `id`: Unique identifier for the task  
- `description`: Short description of the task  
- `status`: `todo`, `in-progress`, or `done`  
- `createdAt`: Date and time when the task was created  
- `updatedAt`: Date and time when the task was last updated  

---

## Installation & Setup

1. Clone or download this project.  
2. Ensure you have **Python 3.x** installed.  
3. Open your terminal in the project folder.  

---

## Usage

Run commands using the `task-cli` script (or `python task-cli.py` depending on your setup).  

### Add a new task
```bash
task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)
