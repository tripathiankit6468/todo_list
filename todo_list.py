# -----------------------------
# Console Based To-Do List App
# -----------------------------

FILE_NAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
        return

    print("\nYour To-Do List:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
    print()

def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append("[ ] " + task)
    save_tasks(tasks)
    print("Task added successfully!\n")

def mark_completed(tasks):
    show_tasks(tasks)
    if not tasks:
        return

    try:
        task_no = int(input("Enter task number to mark completed: "))
        if 1 <= task_no <= len(tasks):
            tasks[task_no - 1] = tasks[task_no - 1].replace("[ ]", "[✔]")
            save_tasks(tasks)
            print("Task marked as completed!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return

    try:
        task_no = int(input("Enter task number to delete: "))
        if 1 <= task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            save_tasks(tasks)
            print(f"Deleted task: {removed}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def main():
    tasks = load_tasks()

    while True:
        print("==== TO-DO LIST MENU ====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Thank you for using To-Do List App!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
