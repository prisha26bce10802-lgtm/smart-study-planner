import json
from tasks import tasks
from subjects import subjects
from schedule import schedule


FILE_NAME = "study_data.json"


def save_data():
    data = {
        "subjects": subjects,
        "tasks": tasks,
        "schedule": schedule
    }

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

    print("Data saved successfully!")


def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

        subjects.extend(data.get("subjects", []))
        tasks.extend(data.get("tasks", []))
        schedule.extend(data.get("schedule", []))

        print("Previous data loaded.")

    except FileNotFoundError:
        print("No previous data found.")