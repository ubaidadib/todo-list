#To DO List

#Function to add a task to the list.
def add_task(todo_list):
    task = input("Enter a task: ").strip()
    if task:
        todo_list.append(task)
        print(f"Task '{task}' added.")
    else:
        print("Task cannot be empty.")

#Function to view the tasks in the list.
def view_tasks(todo_list):
    if not todo_list:
        print("No tasks to display.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")
        print(f"\nTotal tasks: {len(todo_list)}")

#Function to remove a task from the list.
def remove_task(todo_list):
    if not todo_list:
        print("No tasks to remove.")
    else:
        try:
            task_number = int(input("Enter the task number to remove: ").strip())
            if 1 <= task_number <= len(todo_list):
                removed_task = todo_list.pop(task_number - 1)
                print(f"Task '{removed_task}' removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

#Function to run the program.
def main():
    todo_list = []
    while True:
        user_action = input("Enter a command (add, view, remove, exit): ").strip().lower()

        if user_action == "add":
            add_task(todo_list)
        elif user_action == "view":
            view_tasks(todo_list)
        elif user_action == "remove":
            remove_task(todo_list)
        elif user_action == "exit":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid command. Please enter 'add', 'view', 'remove', or 'exit'.")

# Call the main function to run the program
if __name__ == "__main__":
    main()
