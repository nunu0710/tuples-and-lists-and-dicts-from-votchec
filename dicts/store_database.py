inventory = {
    "apple": {"category": "Fruit", "price": 0.99, "stock": 100},
    "pear": {"category": "Fruit", "price": 0.99, "stock": 100},
    "milk": {"category": "Dairy", "price": 2.99, "stock": 50},
    "bread": {"category": "Bakery", "price": 2.49, "stock": 75},
}

while True:
    print("Welcome to the store!")
    print("Available commands: all, category, exit")
    command = input("Enter a command: ")

    if command == "all":
        print("Inventory: ")
        for item, details in inventory.items(): # iterating through dict, assigning key to item (for example apple), value to details (nested dict)
            print(f"{item.capitalize()}: ")
            for detail, value in details.items():
                print(f"- {detail.capitalize()}: {value}")
    elif command == "category":
        category = input("Enter a category: ")
        print(f"Inventory in {category.capitalize()}: ")
        for item, details in inventory.items():
            if details["category"] == category:
                print(f"\n{item.capitalize()}\n")

    elif command == "add":
        item_name = input("Provide item name: ")
        category = input("Provide category: ")
        price = float(input("Provide price per item: "))
        stock = int(input("Provide the amount of items: "))

        inventory[item_name] = {"category": category, "price": price, "stock": stock}

    elif command == "exit":
        print("Goodbye! :)")
        break
    else:
        print("Invalid command!")