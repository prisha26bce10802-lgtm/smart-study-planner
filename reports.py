from tasks import tasks
from subjects import subjects
from schedule import schedule


def generate_report():
    print("\n========== STUDY REPORT ==========")

    print("\nTotal Subjects:", len(subjects))
    print("Total Tasks:", len(tasks))
    print("Study Sessions:", len(schedule))

    if tasks:
        completed = sum(1 for task in tasks if task["completed"])
        pending = len(tasks) - completed

        print("\nCompleted Tasks:", completed)
        print("Pending Tasks:", pending)

        percentage = (completed / len(tasks)) * 100
        print(f"Overall Progress: {percentage:.2f}%")

    print("\n===================================")