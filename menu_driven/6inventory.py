def main() :
    
    items = {}

        
        
    
    while True:
        print("""
        select options:
        1. Add stock
        2. remove stock
        3. view inventory
        4. Exit
        """)
        choice = int(input("select a choice: "))
        
        if choice == 1:
            stock = (input("Enter the item name :"))
            number = int(input("enter the quantity : "))
            items[stock] = number
            print("item details added")
        
            
        elif choice == 2:
            name = input("Enter the stock name to delete: ")

            if items[name] >= number:
                items[name] = items[name] - number
            else:
                print("Cannot remove. Not enough stock.")
            
            
        elif choice == 3:
            print(items)
            
        elif choice == 4:
            break
        
        else:
            print("invalid choice")
    
main()
        
        