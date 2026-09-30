from tasks import tasks


def calculate_progress():
    if not tasks:
        print("No tasks available.")
        return

    total = len(tasks)
    completed = sum(1 for task in tasks if task["completed"])

    percentage = (completed / total) * 100

    print("\n--- STUDY PROGRESS ---")
    print("Total Tasks:", total)
    print("Completed:", completed)
    print("Pending:", total - completed)
    print(f"Progress: {percentage:.2f}%")