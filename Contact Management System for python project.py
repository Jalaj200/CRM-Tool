import sqlite3


conn = sqlite3.connect('contacts.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        email TEXT,
        address TEXT
    )
''')
conn.commit()


def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email (optional): ")
    address = input("Enter contact address (optional): ")

    cursor.execute('''
        INSERT INTO contacts (name, phone, email, address)
        VALUES (?, ?, ?, ?)
    ''', (name, phone, email, address))
    conn.commit()
    print("Contact added successfully!")


def view_contacts():
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    if contacts:
        for contact in contacts:
            print(contact)
    else:
        print("No contacts found.")


def update_contact():
    contact_id = input("Enter the ID of the contact to update: ")
    field = input("Which field do you want to update? (name/phone/email/address): ").lower()
    new_value = input(f"Enter new value for {field}: ")

    if field in ["name", "phone", "email", "address"]:
        cursor.execute(f"UPDATE contacts SET {field} = ? WHERE id = ?", (new_value, contact_id))
        conn.commit()
        print("Contact information updated successfully!")
    else:
        print("Invalid field selection.")


def delete_contact():
    contact_id = input("Enter the ID of the contact to delete: ")
    cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
    conn.commit()
    print("Contact deleted successfully!")


def search_contact():
    search_term = input("Enter the name or phone number of the contact to search: ")
    cursor.execute("SELECT * FROM contacts WHERE name LIKE ? OR phone LIKE ?", (f'%{search_term}%', f'%{search_term}%'))
    contacts = cursor.fetchall()
    if contacts:
        for contact in contacts:
            print(contact)
    else:
        print("No contact found with that information.")


def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            search_contact()
        elif choice == '6':
            print("Exiting Contact Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


conn.close()
