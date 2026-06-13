def main():
    my_tasks = []
    print("--- DecodeLabs To-Do List Manager ---")
    while True:
        print("\nOptions: 1. Add Task | 2. View Tasks | 3. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            task = input("Enter the task: ")
            my_tasks.append(task)
            print("Task added successfully.")
        elif choice == '2':
            print("\nYour Current Tasks:")
            if not my_tasks:
                print("The list is empty.")
            else:
                # Using enumerate for Professional Polish
                for index, task in enumerate(my_tasks):
                    print(f"{index}: {task}")

        elif choice == '3':
            print("Exiting program.")
            break    
        else:
            print("Invalid option. Please try again.")
if __name__ == "__main__":
    main()