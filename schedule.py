schedule = []


def add_study_session():
    subject = input("Enter subject: ")
    day = input("Enter day: ")
    time = input("Enter study time: ")
    duration = input("Enter duration (in hours): ")

    session = {
        "subject": subject,
        "day": day,
        "time": time,
        "duration": duration
    }

    schedule.append(session)

    print("Study session added successfully!")


def view_schedule():
    if not schedule:
        print("No study sessions scheduled.")
        return

    print("\n--- STUDY SCHEDULE ---")

    for i, session in enumerate(schedule, 1):
        print(
            f"{i}. {session['day']} | "
            f"{session['time']} | "
            f"{session['subject']} | "
            f"{session['duration']} hours"
        )