# Simple To-Do List

tasks = []

def add_task(task_name):
    """Add a task to the list"""
    tasks.append(task_name)
    print(f"Added: {task_name}")

def view_tasks():
    """Show all tasks"""
    print("\n=== MY TO-DO LIST ===")
    if len(tasks) == 0:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Test the program
add_task("Buy groceries")
add_task("Study for SEN 201")
add_task("Exercise")

view_tasks()