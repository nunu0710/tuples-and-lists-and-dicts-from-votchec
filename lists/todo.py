todo_list = ["Cook dinner", "Do homework", "Go to the grocery store"]

while True:
    print("\nTo-Do List:")
    for item in todo_list:
        # .index() allows us to get index of an item from list based on value
        print(f"{todo_list.index(item) + 1}. {item}")

    print("\nOptions: add, remove, exit")
    action = input("Command: ").lower()

    if action == "exit":
        break
    elif action == "add":
        task = input("Enter a task to add: ")
        todo_list.append(task)
    elif action == "remove":
        task_id = int(input("Enter task ID to remove: "))
        if task_id > len(todo_list):
            print("\nItem out of range!\n")
        else:
            todo_list.pop(task_id - 1)
    else:
        print("\nInvalid command!!\n")