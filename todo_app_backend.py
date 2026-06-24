import datetime
import json

TASKS_FILE = "tasks.json"
DEFAULT_PRIORITY = "Normal"
DEFAULT_CATEGORY = "General"


def normalize_task(task):
    return {
        "text": task.get("text", ""),
        "done": task.get("done", False),
        "priority": task.get("priority", DEFAULT_PRIORITY),
        "category": task.get("category", DEFAULT_CATEGORY),
        "created_at": task.get("created_at", datetime.datetime.now().isoformat()),
    }


def load_tasks():
    """Load tasks from JSON file. Returns empty list if file doesn't exist or is corrupted."""
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            return [normalize_task(task) for task in json.load(file)]
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2, ensure_ascii=False)


def make_task(text, priority="Normal", category="General"):
    return {
        "text": text,
        "done": False,
        "priority": priority,
        "category": category,
        "created_at": datetime.datetime.now().isoformat(),
    }


def add_task(tasks, text, priority="Normal", category="General"):
    """Add a new task to the tasks list."""
    tasks.append(make_task(text, priority, category))


def delete_task(tasks, index):
    """Delete a task by index and return the deleted task."""
    return tasks.pop(index)


def mark_done(tasks, index):
    """Mark a task as done by index."""
    tasks[index]["done"] = True
    return tasks[index]