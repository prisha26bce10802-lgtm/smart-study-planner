from subjects import add_subject, view_subjects
from tasks import add_task, view_tasks, complete_task
from schedule import add_study_session, view_schedule
from progress import calculate_progress
from reports import generate_report
from storage import save_data, load_data


def main():

    load_data()

    while True:

        print("\n")
        print("======================================")
        print("       SMART STUDY PLANNER")
        print("======================================")
        print("1. Add Subject")
        print("2. View Subjects")
        print("3. Add Task")
        print("4. View Tasks")
        print("5. Complete Task")
        print("6. Add Study Session")
        print("7. View Study Schedule")
        print("8. View Progress")
        print("9. Generate Report")
        print("10. Save Data")
        print("11. Exit")
        print("======================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_subject()

        elif choice == "2":
            view_subjects()

        elif choice == "3":
            add_task()

        elif choice == "4":
            view_tasks()

        elif choice == "5":
            complete_task()

        elif choice == "6":
            add_study_session()

        elif choice == "7":
            view_schedule()

        elif choice == "8":
            calculate_progress()

        elif choice == "9":
            generate_report()

        elif choice == "10":
            save_data()

        elif choice == "11":
            save_data()
            print("Thank you for using Smart Study Planner!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()