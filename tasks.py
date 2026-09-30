tasks = []


def add_task():
    task_name = input("Enter task/assignment name: ")
    subject = input("Enter subject: ")
    deadline = input("Enter deadline (DD-MM-YYYY): ")

    task = {
        "name": task_name,
        "subject": subject,
        "deadline": deadline,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")


def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\n--- TASKS ---")

    for i, task in enumerate(tasks, 1):
        status = "Completed" if task["completed"] else "Pending"

        print(f"\n{i}. {task['name']}")
        print(f"Subject: {task['subject']}")
        print(f"Deadline: {task['deadline']}")
        print(f"Status: {status}")


def complete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("\nEnter task number to mark completed: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")