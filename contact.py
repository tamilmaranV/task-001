contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return
    print("\nContact List:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")
    print()

def search_contact():
    query = input("Search by name or phone number: ").lower()
    results = [c for c in contacts if query in c['name'].lower() or query in c['phone']]
    if results:
        for contact in results:
            print(f"\nName: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
    else:
        print("No contact found.\n")

def update_contact():
    name = input("Enter name of contact to update: ").lower()
    for contact in contacts:
        if contact['name'].lower() == name:
            print("Leave blank to keep existing value.")
            new_name = input("New name: ") or contact['name']
            new_phone = input("New phone: ") or contact['phone']
            new_email = input("New email: ") or contact['email']
            new_address = input("New address: ") or contact['address']
            contact.update({
                "name": new_name,
                "phone": new_phone,
                "email": new_email,
                "address": new_address
            })
            print("Contact updated successfully!\n")
            return
    print("Contact not found.\n")

def delete_contact():
    name = input("Enter name of contact to delete: ").lower()
    for i, contact in enumerate(contacts):
        if contact['name'].lower() == name:
            del contacts[i]
            print("Contact deleted successfully!\n")
            return
    print("Contact not found.\n")

def show_menu():
    while True:
        print("\n=== Contact Management System ===")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

# Start the program
show_menu()
