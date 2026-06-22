# To-Do List Application
# This program allows users to add, view, delete, save, and load tasks.

# Store all tasks in a list
tasks = []
TASKS_FILE = "tasks.txt"

# Display all tasks with their numbers, or show "No tasks" if list is empty
def show_tasks():
    if len(tasks) == 0:
        print("No tasks")
    else:
        # enumerate() gives both index and value; add 1 to show user-friendly numbering
        for i, task in enumerate(tasks):
            print(i + 1, task)

# Add a new task to the list
def add_task():
    task = input("Enter task: ").strip()
    if not task:
        print("Task cannot be empty.")
        return

    tasks.append(task)  # append() adds the task to the end of the list
    print(f"Added task: {task}")
    save_tasks()

# Delete a task by its number
def delete_task():
    if len(tasks) == 0:
        print("No tasks to delete.")
        return

    print(f"Total tasks: {len(tasks)}")
    show_tasks()
    print("Enter 'back' to cancel.")

    choice = input("Enter number: ").strip().lower()
    if choice == "back":
        print("Delete canceled.")
        return

    try:
        num = int(choice)
    except ValueError:
        print("Please enter a valid number or 'back'.")
        return

    # Check if the entered number is valid (between 1 and list length)
    if 0 < num <= len(tasks):
        removed = tasks.pop(num - 1)  # pop() removes item at the given index (subtract 1 for 0-based indexing)
        print(f"Removed task: {removed}")
        save_tasks()
    else:
        print("Invalid number")

# Save tasks to a file using with open and error handling
def save_tasks():
    try:
        with open(TASKS_FILE, "w", encoding="utf-8") as file:
            for task in tasks:
                file.write(task + "\n")
        print(f"Tasks saved to {TASKS_FILE}.")
    except OSError as error:
        print(f"Error saving tasks: {error}")

# Load tasks from a file using with open and error handling
def load_tasks():
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            loaded_tasks = [line.rstrip("\n") for line in file]
        tasks.clear()
        tasks.extend(loaded_tasks)
        print(f"Loaded {len(tasks)} tasks from {TASKS_FILE}.")
    except FileNotFoundError:
        print(f"No saved task file found ({TASKS_FILE}).")
    except OSError as error:
        print(f"Error loading tasks: {error}")
load_tasks()  # Load tasks from file at the start of the program    
# Main menu loop - runs continuously until user chooses to exit
while True:
    # Display menu options
    print("\n1 Add")
    print("2 Show")
    print("3 Delete")
    print("4 Save")
    print("5 Load")
    print("6 Exit")

    choice = input("Choose: ")

    # Execute the function based on user's choice
    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        save_tasks()
    elif choice == "5":
        load_tasks()
    elif choice == "6":
        break  # Exit the while loop when user chooses 6
    else:
        print("Please choose a valid option.")