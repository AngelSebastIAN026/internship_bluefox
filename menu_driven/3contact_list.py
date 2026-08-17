def main() :
    
    contacts = {}

        
        
    
    while True:
        print("""
        select options:
        1. Add a contact
        2. search for contact
        3. delete contact
        4. list all contacts
        5. Exit
        """)
        choice = int(input("select a choice: "))
        
        if choice == 1:
            name = (input("Enter the name :"))
            number = (input("enter the phone number: "))
            contacts[name] = number
            print("contact details added")
        
            
        elif choice == 2:
            search = input("Enter the name: ")

            if search in contacts:
                print(contacts[search])
            else:
                print("Contact not found")
            
        elif choice == 3:
            name = input("Enter the name to delete: ")

            if name in contacts:
                del contacts[name]
                print("Contact deleted")
            else:
                print("Contact not found")
            
        elif choice == 4:
            print(contacts)
            
        elif choice == 5:
            break
        
        else:
            print("invalid choice")
    
main()
        
        