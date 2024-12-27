class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        print(f"Contact '{name}' added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        print("\nContact List:")
        for name, details in self.contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}")

    def search_contact(self, search_term):
        found_contacts = {name: details for name, details in self.contacts.items() if search_term in name or search_term in details['phone']}
        if not found_contacts:
            print("No contacts found.")
            return
        print("\nSearch Results:")
        for name, details in found_contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}")

    def update_contact(self, name):
        if name not in self.contacts:
            print(f"Contact '{name}' not found.")
            return
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")
        self.contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        print(f"Contact '{name}' updated successfully.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def display_menu(self):
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Choose an option: ")
            if choice == '1':
                name = input("Enter name: ")
                phone = input("Enter phone number: ")
                email = input("Enter email: ")
                address = input("Enter address: ")
                self.add_contact(name, phone, email, address)
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                search_term = input("Enter name or phone number to search: ")
                self.search_contact(search_term)
            elif choice == '4':
                name = input("Enter the name of the contact to update: ")
                self.update_contact(name)
            elif choice == '5':
                name = input("Enter the name of the contact to delete: ")
                self.delete_contact(name)
            elif choice == '6':
                print("Exiting the Contact Manager.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    contact_manager = ContactManager()
    contact_manager.run()
