# To-Do List Application
# This program allows users to add, view, delete, save, load, and mark tasks as done.

# Store all tasks in a list (backend handles file I/O)
import todo_app_backend as backend

tasks = []

# Display all tasks with their numbers and status, or show "No tasks" if list is empty
def show_tasks():
    if len(tasks) == 0:
        print("No tasks")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task.get("done") else "Pending"
            print(f"{i}. [{status}] {task['text']}")

# Add a new task to the list
def add_task():
    task_text = input("Enter task: ").strip()
    if not task_text:
        print("Task cannot be empty.")
        return

    backend.add_task(tasks, task_text)
    print(f"Added task: {task_text}")
    backend.save_tasks(tasks)

# Ask the user for a task number and validate the input
def get_task_number():
    if len(tasks) == 0:
        print("No tasks available.")
        return None

    print(f"Total tasks: {len(tasks)}")
    show_tasks()
    print("Enter 'back' to cancel.")

    choice = input("Enter number: ").strip().lower()
    if choice == "back":
        print("Operation canceled.")
        return None

    try:
        num = int(choice)
    except ValueError:
        print("Please enter a valid number or 'back'.")
        return None

    if 0 < num <= len(tasks):
        return num

    print("Invalid number")
    return None

# Delete a task by its number
def delete_task():
    num = get_task_number()
    if num is None:
        return

    removed = backend.delete_task(tasks, num - 1)
    print(f"Removed task: {removed['text']}")
    backend.save_tasks(tasks)

# Mark a task as done
def mark_done():
    num = get_task_number()
    if num is None:
        return

    task = tasks[num - 1]
    if task.get("done"):
        print(f"Task already marked done: {task['text']}")
        return

    backend.mark_done(tasks, num - 1)
    print(f"Marked done: {task['text']}")
    backend.save_tasks(tasks)

# Save tasks to a file using with open and error handling
def save_tasks():
    try:
        backend.save_tasks(tasks)
        print("Tasks saved.")
    except OSError as error:
        print(f"Error saving tasks: {error}")

# Load tasks from a file using with open and error handling
def load_tasks():
    try:
        loaded = backend.load_tasks()
        tasks.clear()
        tasks.extend(loaded)
        print(f"Loaded {len(tasks)} tasks from storage.")
    except OSError as error:
        print(f"Error loading tasks: {error}")

# Main menu loop - runs continuously until user chooses to exit
def main():
    load_tasks()  # Load tasks from file at the start of the program

    while True:
        print("\n1 Add")
        print("2 Show")
        print("3 Delete")
        print("4 Mark Done")
        print("5 Save")
        print("6 Load")
        print("7 Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            mark_done()
        elif choice == "5":
            save_tasks()
        elif choice == "6":
            load_tasks()
        elif choice == "7":
            break
        else:
            print("Please choose a valid option.")


if __name__ == "__main__":
    main()
