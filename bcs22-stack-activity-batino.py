import time


class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.task_complete = False


class TaskManager:
    def __init__(self, max_size):
        self.tasks = []
        self.max_size = max_size

    def add_task(self, title, description):
        new_task = Task(title, description)
        self.tasks.append(new_task)
        print("A NEW TASK has been listed.")
        time.sleep(2)

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].task_complete = True
            print(f"Task #{task_index + 1} is now COMPLETED.")
            time.sleep(2)
        else:
            print("INVALID task index.")
            time.sleep(1)

    def display_tasks(self):
        for i, task in enumerate(self.tasks):
            status = "COMPLETED" if task.task_complete else "PENDING"
            print(f"Task #{i + 1}: {'{:<5}'.format(task.title)} - {'{:<5}'.format(task.description)} ({'{:<5}'.format(status)})")
        time.sleep(2)

    def open(self):
        while True:
            print("\nTask Manager Menu:")
            print("1. Add a Task")
            print("2. Mark Task as Completed")
            print("3. Display Tasks")
            print("4. Exit")
            choice = input("Enter your choice: [1][2][3][4] ---> ")
            print()

            if choice == "1":
                if len(self.tasks) < self.max_size:
                    title = input("Enter the task title: ")
                    description = input("Enter the task description: ")
                    self.add_task(title, description)
                else:
                    print("Your task manager is FULL.")
                    time.sleep(2)

            elif choice == "2":
                if not self.tasks:
                    print("No tasks in the task manager.")
                    time.sleep(1)
                else:
                    self.display_tasks()
                    task_index = int(input("Enter the task index to mark as completed: "))
                    self.complete_task(task_index - 1)

            elif choice == "3":
                if not self.tasks:
                    print("No tasks in the task manager.")
                    time.sleep(1)
                else:
                    self.display_tasks()

            elif choice == "4":
                print("Closing Task Manager...")
                time.sleep(2)
                break
            else:
                print("Invalid choice. Choose only between: [1][2][3][4]")
                time.sleep(2)


task_manager = TaskManager(5)
task_manager.open()
