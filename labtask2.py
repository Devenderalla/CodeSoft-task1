To do list


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            return True
        return False

    def update_task(self, task_index, new_task):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index] = new_task
            return True
        return False

    def display_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty!")
        else:
            print("Your to-do list:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")


def main():
    todo_list = TodoList()

    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Update task")
        print("4. Display tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
            print("Task added successfully!")

        elif choice == "2":
            task_index = int(input("Enter the index of the task to remove: ")) - 1
            if todo_list.remove_task(task_index):
                print("Task removed successfully!")
            else:
                print("Invalid task index.")

        elif choice == "3":
            task_index = int(input("Enter the index of the task to update: ")) - 1
            new_task = input("Enter the new task: ")
            if todo_list.update_task(task_index, new_task):
                print("Task updated successfully!")
            else:
                print("Invalid task index.")

        elif choice == "4":
            todo_list.display_tasks()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
