def main() :
    
    tasks =[]
    
    while True:
        print("""
        select options :
        1.Add a task
        2.Remove a task
        3.show all tasks
        4.Exit
        """)
        choice = int(input("Select one: "))
    
        if choice == 1:
            task = input("Add a task: ")
            tasks.append(task)
    
        elif choice == 2:
            task = input("Remove a task: ")
            if task in tasks:
                tasks.remove(task) 
        
        elif choice == 3:
            print(tasks)
        
        elif choice == 4:
            break
    
        else:
            print("Invalid choice: ")
            
main()