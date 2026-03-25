def display_menu():
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")

def get_name():
    name = input() 
    return name

def get_attributes():
    phone = input()
    email = input()
    address = input()
    return phone, email, address

def add_contact(contact_book):
    name = get_name()
    if name in contact_book:
        print("Contact already exists!")
    
    phone, email, address = get_attributes()
    contact_book[name] = {"phone": phone, "email": email, "address": address}
    print("Contact added successfully!")

def view_contact(contact_book):
    name = get_name()
    if name in contact_book:
        print(f"Name: {name}")
        print(f"Phone: {contact_book[name]['phone']}")
        print(f"Email: {contact_book[name]['email']}")
        print(f"Address: {contact_book[name]['address']}") 
            
    else:
        print("Contact not found!")

def list_all_contacts(contact_book):
    if contact_book:
        for name in contact_book:
            print(f"Name: {name}")
            print(f"Phone: {contact_book[name]['phone']}")
            print(f"Email: {contact_book[name]['email']}")
            print(f"Address: {contact_book[name]['address']}")
            print()         
    else:
        print("No contacts available.")         

def edit_contact(contact_book):
    name = input()
    if name in contact_book:
        phone = input()
        email = input()
        address = input()

        if phone == '':
            phone = contact_book[name]['phone']
        if email == '':
            email = contact_book[name]['email']
        if address == '':
            address = contact_book[name]['address']

        contact_book[name] = {"phone": phone, "email": email, "address": address}
        print("Contact updated successfully!")
    else:
        print("Contact not found!")

def delete_contact(contact_book):
    name = get_name()
    if name in contact_book:
        contact_book.pop(name)
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")   

def select_option(option: int, contact_book: dict) -> bool:
    match option:
        case 1:
            add_contact(contact_book)
        case 2:
            view_contact(contact_book)
        case 3:
            edit_contact(contact_book)
        case 4:
            delete_contact(contact_book)
        case 5:
            list_all_contacts(contact_book)
        case 6:
            return False  # Signal to exit
        case _:
            print("Invalid choice. Please try again.")
    return True  # Continue loop

is_program_open = True
contact_book = {}

while is_program_open:
    display_menu()
    option = int(input())
    is_program_open = select_option(option, contact_book) 