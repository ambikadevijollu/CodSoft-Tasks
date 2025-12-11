# To - Do List Task
def show_title():
    print("\n=======YOUR PERSONAL TASK MANAGER=======")

def display_menu():
    print("\nChoose an option:")
    print(" A - Add a new task ")
    print(" L - List all tasks ")
    print(" R - Remove a task")
    print(" E - Edit an existing task")
    print(" C - Mark a task as completed")
    print(" Q  - Quit ")

def add_task(task_list):
    new_task = input("Enter the task to add:")
    task_list.append({"name": new_task, "done": False})
    print(f"Task added: '{new_task}'")

def list_task(task_list):
    if not task_list:
       print("No tasks found yet!")
       return
    print("\nYour Tasks:")
    for index, task in enumerate(task_list, start=1):
        status = "✅" if task["done"] else "❌"
        print(f" {index}. [{status}] {task['name']}")

def remove_task(task_list):
    list_task(task_list)
    if not task_list:
        return
    try:
        number = int(input("Enter task number to delete:"))
        removed = task_list.pop(number - 1)
        print(f"Removed task: '{removed}'")
    except(ValueError , IndexError):
        print("Invalid choice! Try again.")
def edit_task(task_list):
    list_task(task_list)
    if not task_list:
       return
    try:
        num = int(input("Enter task number to edit: "))
        new_name = input("Enter new task name: ")
        task_list[num - 1]["name"] = new_name
        print("Task updated successfully!")
    except (ValueError, IndexError):
        print("Invalid selection!")

def complete_task(task_list):
    list_task(task_list)
    if not task_list:
       return
    try:
        num = int(input("Enter task number to mark as completed: "))
        task_list[num - 1]["done"] = True
        print(f"Task'{task_list[num-1]['name']}' marked as completed!")
    except (ValueError, IndexError):
        print("Invalid input!")
def main():
    tasks = []
    show_title()

    while True:
        display_menu()
        choice = input("Your option: ").strip().upper()

        if choice == "A":
            add_task(tasks)
        elif choice == "L":
            list_task(tasks)
        elif choice == "R":
            remove_task(tasks)
        elif choice == "E":
            edit_task(tasks)
        elif choice == "C":
             complete_task(tasks)
        elif choice == "Q":
            print("Exiting program...Goodbye!")
            break
        else:
            print("Invalid option! Please choose again.")

if __name__ == "__main__":
  main()