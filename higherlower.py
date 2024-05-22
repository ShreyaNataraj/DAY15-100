# Initialize an empty list to store tasks
todo_list = []

def display_tasks():
    """Displays the current list of tasks."""
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")

def add_task(task):
    """Adds a task to the to-do list."""
    todo_list.append(task)
    print(f"Task '{task}' added to the list.")

# Main loop
while True:
    print("\nTo-Do List Menu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        display_tasks()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
