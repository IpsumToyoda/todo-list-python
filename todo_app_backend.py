import json

TASKS_FILE = "tasks.json"


def load_tasks():
    """Load tasks from JSON file. Returns empty list if file doesn't exist or is corrupted."""
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2, ensure_ascii=False)


def add_task(tasks, text):
    """Add a new task to the tasks list."""
    tasks.append({"text": text, "done": False})


def delete_task(tasks, index):
    """Delete a task by index and return the deleted task."""
    return tasks.pop(index)


def mark_done(tasks, index):
    """Mark a task as done by index."""
    tasks[index]["done"] = True