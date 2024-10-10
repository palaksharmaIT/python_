import json

# Dictionary to store contacts
contacts = {}

# Function to add a new contact
def add_contact(name, phone, email):
    if name in contacts:
        print(f"Contact with name {name} already exists.")
    else:
        contacts[name] = {'Phone': phone, 'Email': email}
        print(f"Contact {name} added successfully!")

# Function to delete a contact
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print(f"Contact {name} not found.")

# Function to search for a contact
def search_contact(name):
    if name in contacts:
        contact = contacts[name]
        print(f"Name: {name}, Phone: {contact['Phone']}, Email: {contact['Email']}")
    else:
        print(f"Contact {name} not found.")

# Function to display all contacts
def display_contacts():
    if contacts:
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['Phone']}, Email: {info['Email']}")
    else:
        print("No contacts available.")

# Function to save contacts to a JSON file
def save_contacts(filename="contacts.json"):
    with open(filename, 'w') as f:
        json.dump(contacts, f)
    print("Contacts saved successfully!")

# Function to load contacts from a JSON file
def load_contacts(filename="contacts.json"):
    global contacts
    try:
        with open(filename, 'r') as f:
            contacts = json.load(f)
        print("Contacts loaded successfully!")
    except FileNotFoundError:
        print("No saved contacts found.")

# Main function to run the application
def main():
    load_contacts()  # Load contacts from file on startup

    while True:
        print("\n--- ContactMaster ---")
        print("1. Add a new contact")
        print("2. Delete a contact")
        print("3. Search for a contact")
        print("4. Display all contacts")
        print("5. Save contacts")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            add_contact(name, phone, email)
        
        elif choice == '2':
            name = input("Enter name of the contact to delete: ")
            delete_contact(name)
        
        elif choice == '3':
            name = input("Enter name of the contact to search: ")
            search_contact(name)
        
        elif choice == '4':
            display_contacts()
        
        elif choice == '5':
            save_contacts()
        
        elif choice == '6':
            save_contacts()  # Auto-save on exit
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

# Run the program
if __name__ == "__main__":
    main()
