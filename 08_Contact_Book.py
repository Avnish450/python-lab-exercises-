contacts = []

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    contact = {"name": name, "phone": phone}
    contacts.append(contact)
    print("Contact added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\nContact List")
        for contact in contacts:
            print("Name:", contact["name"], "| Phone:", contact["phone"])

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        print("Exiting contact book.")
        break
    else:
        print("Invalid choice. Try again.")
