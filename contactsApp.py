from save import *
from contact import *
import sys
import textwrap
import shutil
import random

class ContactsApp:
    def __init__(self):
        self.contactFile = load()
        self.contactList = []
        for i in self.contactFile["contacts"]:
            # Ensure all keys are present
            i.setdefault("first_name", "N/A")
            i.setdefault("middle_name", "N/A")
            i.setdefault("last_name", "N/A")
            i.setdefault("phone", "N/A")
            i.setdefault("email_address", "N/A")
            i.setdefault("addressLine1", "N/A")
            i.setdefault("addressLine2", "N/A")
            i.setdefault("city", "N/A")
            i.setdefault("state", "N/A")
            i.setdefault("zip", "N/A")
            i.setdefault("first_last", "N/A")
            i.setdefault("last_first", "N/A")
            i.setdefault("full_address", "N/A")
            i.setdefault("full_name", "N/A")
            i.setdefault("unique_id", "N/A")
            self.contactList.append(Contact(
                i["first_name"], i["middle_name"], i["last_name"], i["phone"], i["email_address"],
                i["addressLine1"], i["addressLine2"], i["city"], i["state"], i["zip"], i["first_last"], i["last_first"],
                i["full_address"], i["full_name"], i["unique_id"]
            ))

    def redoList(self):
        self.contactList = []
        for i in self.contactFile["contacts"]:
            self.contactList.append(Contact(
                i["first_name"], i["middle_name"], i["last_name"], i["phone"], i["email_address"],
                i["addressLine1"], i["addressLine2"], i["city"], i["state"], i["zip"], i["first_last"], i["last_first"], i["full_address"], i["full_name"], i["unique_id"])
            )

    def add_contact(self):
        try:
            zing = {
                "first_name": input("First Name: "), "middle_name": input("Middle Name: "), "last_name": input("Last Name: "), 
                "phone": input("Phone: "), "email_address": input("Email Address: "), "addressLine1": input("Address Line 1: "), 
                "addressLine2": input("Address Line 2: "), "city": input("City: "), "state": input("State: "), "zip": input("Zip: ")
            }
            zing["first_last"] = zing["first_name"] + " " + zing["last_name"]
            zing["last_first"] = zing["last_name"] + " " + zing["first_name"] + ", " + zing["first_name"]
            if zing["addressLine2"] == "":
                zing["full_address"] = zing["addressLine1"] + ", " + zing["city"] + ", " + zing["state"] + ", " + zing["zip"]
            else:
                zing["full_address"] = zing["addressLine1"] + ", " + zing["addressLine2"] + ", " + zing["city"] + ", " + zing["state"] + ", " + zing["zip"]
            if zing["middle_name"] == "":
                zing["full_name"] = zing["first_last"]
            else:
                zing["full_name"] = zing["first_name"] + " " + zing["middle_name"] + " " + zing["last_name"]
            zing["unique_id"] = str(random.randint(100000, 999999))
        except EOFError:
            sys.exit(0)
        contact = Contact(
            zing["first_name"], zing["middle_name"], zing["last_name"], zing["phone"], zing["email_address"], 
            zing["addressLine1"], zing["addressLine2"], zing["city"], zing["state"], zing["zip"], 
            zing["first_last"], zing["last_first"], zing["full_address"], zing["full_name"], zing["unique_id"]
        )
        for key, value in contact.__dict__.items():
            if not contact.__dict__[key]:
                contact.__dict__[key] = "N/A"

        # Check if the contact already exists to avoid duplicates
        if contact.__dict__ not in self.contactFile["contacts"]:
            self.contactList.append(contact)
            self.contactFile["contacts"].append(contact.__dict__)
            save(self.contactFile)
        else:
            print("This contact already exists.")

    def remove_contact(self, query):
        config = loadConfig()
        contact_to_remove = None
        for contact in self.contactList:
            if contact.__dict__[config["query"]] == query:
                contact_to_remove = contact
                break
        if contact_to_remove:
            self.contactList.remove(contact_to_remove)
            self.contactFile["contacts"] = [contact.__dict__ for contact in self.contactList]
            print(f"Contact '{query}' removed successfully.")
        else:
            print(f"Contact '{query}' not found.")
        save(self.contactFile)

    def edit_contact(self, query):
        config = loadConfig()
        for contact in self.contactList:
            if contact.__dict__[config["query"]] == query:
                for key, value in contact.__dict__.items():
                    print(f"{key}: {value}")
                while True:
                    choice = input("Enter the field to edit (or type 'exit' to finish): ")
                    if choice in contact.__dict__:
                        contact.__dict__[choice] = input(f"Enter the new value for {choice}: ")
                        for key, value in contact.__dict__.items():
                            if not contact.__dict__[key]:
                                contact.__dict__[key] = "N/A"
                    elif choice == "exit":
                        break
                    else:
                        print("Invalid field.")
                    save(self.get_contacts_as_dict())
                return
        print(f"Contact '{query}' not found.")

    def get_contacts(self):
        save(self.contactFile)
        return self.contactList

    def get_contacts_as_dict(self):
        return {"contacts": [contact.__dict__ for contact in self.contactList]}

    def search_contact(self, query):
        config = loadConfig()
        for contact in self.contactList:
            if contact.__dict__[config["query"]] == query:
                for key, value in contact.__dict__.items():
                    if key != 'unique_id':
                        print(f"{key}: {value}")
                print(f"unique_id: {contact.unique_id}")
                save(self.contactFile)
                return contact

    def list_contacts(self):
        # Get the terminal width
        terminal_width = shutil.get_terminal_size().columns

        # Define headers with fixed column widths
        headers = [
            "First Name", "Middle Name", "Last Name", "Phone", "Email Address",
            "Address Line 1", "Address Line 2", "City", "State", "Zip", "Unique ID"
        ]
        header_str = " | ".join([
            f"{headers[0]:<12}", f"{headers[1]:<15}", f"{headers[2]:<12}", f"{headers[3]:<15}",
            f"{headers[4]:<25}", f"{headers[5]:<20}", f"{headers[6]:<15}", f"{headers[7]:<15}",
            f"{headers[8]:<10}", f"{headers[9]:<10}"
        ])
        wrapped_headers = textwrap.wrap(header_str, width=terminal_width)

        # Print the header once
        for line in wrapped_headers:
            print(line)
        print("-" * terminal_width)

        # Print each contact with fixed column widths and line wrapping
        for contact in self.contactList:
            contact_str = f"{contact.first_name:<12} | {contact.middle_name:<15} | {contact.last_name:<12} | {contact.phone:<15} | {contact.email_address:<25} | {contact.addressLine1:<20} | {contact.addressLine2:<15} | {contact.city:<15} | {contact.state:<10} | {contact.zip:<6} | {contact.unique_id:<10}"
            wrapped_contact_str = textwrap.wrap(contact_str, width=terminal_width)

            # Print the contact details
            for line in wrapped_contact_str:
                print(line)

            # Print a separator line for clarity
            print("-" * terminal_width)

    def ui(self):
        while True:
            print("Contacts App")
            print("add - Add Contact")
            print("remove - Remove Contact")
            print("search - Search Contact")
            print("list - List Contacts")
            print("edit - Edit Contact")
            print("exit - Exit")
            choice = input("Enter your choice: ")
            if choice == "add":
                self.add_contact()
            elif choice == "remove":
                self.remove_contact(input("Enter the first name of the contact to remove: "))
            elif choice == "search":
                contact = self.search_contact(input("Enter the query to search for a contact: "))
                if contact:
                    for key, value in contact.__dict__.items():
                        if key != 'unique_id':
                            print(f"{key}: {value}")
                    print(f"unique_id: {contact.unique_id}")
                else:
                    print("Contact not found.")
            elif choice == "list":
                self.list_contacts()
            elif choice == "edit":
                self.edit_contact(input("Enter the first name of the contact to edit: "))
            elif choice == "exit":
                save(self.get_contacts_as_dict())
                break
            else:
                print("Invalid choice")

if __name__ == "__main__":
    app = ContactsApp()
    app.ui()
