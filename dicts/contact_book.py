"""
This program demonstrates using a dictionary to store and manage a contacts book. 
It allows adding, removing, and searching for contacts.
"""

contacts = {}

while True:
    print("\nContacts Book")
    for name, number in contacts.items():
        print(f"{name}: {number}")

    print("\nOptions: add, remove, search, exit")
    action = input("What would you like to do? ").lower()

    if action == "add":
        name = input("Enter the contact's name: ")
        number = input("Enter the contact's phone number: ")
        contacts[name] = number
        print("Contact added.")
    elif action == "remove":
        name = input("Enter the contact's name to remove: ")
        if name in contacts:
            del contacts[name]
            print("Contact removed.")
        else:
            print("Contact not found.")
    elif action == "search":
        name = input("Enter the contact's name to search: ")
        if name in contacts:
            print(f"{name}'s phone number is {contacts[name]}")
        else:
            print("Contact not found.")
    elif action == "exit":
        break
    else:
        print("Invalid option. Please choose 'add', 'remove', 'search', or 'exit'.")
