subjects = []


def add_subject():
    name = input("Enter subject name: ")

    if name.strip() == "":
        print("Subject name cannot be empty.")
        return

    subjects.append(name)
    print("Subject added successfully!")


def view_subjects():
    if not subjects:
        print("No subjects added.")
        return

    print("\n--- SUBJECTS ---")
    for i, subject in enumerate(subjects, 1):
        print(f"{i}. {subject}")