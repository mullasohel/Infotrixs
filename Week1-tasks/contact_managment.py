
contacts = {}  # This contacts dictionary to store contacts

def add_contact():
    name = input("Enter contact name: ")
    number = input("Enter contact number: ")
    contacts[name] = number
    print("Contact added successfully!")

def search_contact():
    name = input("Enter contact name to search: ")
    if name in contacts:
        print("Contact found!")
        print("Name: ", name)
        print("Number: ", contacts[name])
    else:
        print("Contact not found!")

def main():
    print("Welcome to the Contact Management !")
    while True:
        print("\nChoose an option:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            print("See you soon !")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
