import time

task = []

print("=" * 50)
print("           TO-DO LIST APPLICATION")
print("=" * 50)

ch = input("Do you want to continue? (y/n): ")

while ch.lower() == 'y':

    print("\n" + "=" * 50)
    print("                 MAIN MENU")
    print("=" * 50)
    print("1. Add Task")
    print("2. Delete Task")
    print("3. View Tasks")
    print("4. Show Progress Bar")
    print("=" * 50)

    choice = int(input("Enter your choice: "))
# ---------------add tasks---------------
    if choice == 1:

        no = int(input("How many tasks do you want to add? "))

        for i in range(no):
            task.append(input(f"Enter Task {i+1}: "))

        print("-" * 50)
        print("Tasks Added Successfully!")
        print("-" * 50)
# --------------delete tasks------------
    elif choice == 2:

        if len(task) == 0:
            print("-" * 50)
            print("No Tasks Available.")
            print("-" * 50)

        else:
            print("-" * 50)
            print("Current Tasks")
            print("-" * 50)

            for i in range(len(task)):
                print(i + 1, ".", task[i])

            n = int(input("Enter task number to remove: "))

            if 1 <= n <= len(task):
                print("Removing Task...")
                time.sleep(2)
                task.pop(n - 1)
                print("Task Removed Successfully!")
            else:
                print("Invalid Task Number!")
# -------------view list of tasks--------------
    elif choice == 3:

        if len(task) == 0:
            print("-" * 50)
            print("No Tasks In The List.")
            print("-" * 50)

        else:
            print("-" * 50)
            print("YOUR TO-DO LIST")
            print("-" * 50)

            for i in range(len(task)):
                print(i + 1, ".", task[i])

            print("-" * 50)
#  -------------- show progress of your tasks---------
    elif choice == 4:

        total = len(task)

        if total == 0:
            print("-" * 50)
            print("Progress: [##########] 100%")
            print("All Tasks Completed!")
            print("-" * 50)

        else:

            if total >= 10:
                total = 10

            bar = "#" * (10 - total) + "-" * total

            print("-" * 50)
            print("Progress Bar")
            print("-" * 50)
            print("[" + bar + "]")
            print("-" * 50)

    else:
        print("Invalid Choice!")

    ch = input("\nDo you want to continue? (y/n): ")

print("\n" + "=" * 50)
print(" Thank You For Using To-Do List Application ")
print("=" * 50)