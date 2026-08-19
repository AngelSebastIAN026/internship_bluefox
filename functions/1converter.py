
def celisus_to_farenheit(c):
    f = (c * 9/5) + 32
    print("Farenheit:", f)
        
def farenheit_to_celisus(f):
    c = (f - 32) * 5/9
    print("Celsius:", c) 
    
    


def main ():
    
    while True:
        print("""
         Select options:
         1.celesius to farenheit
         2.Farenheit to celesius
         3.Exit
        """)
        
        choice = int(input("choose the option: "))
        
        if choice == 1:
            c = float(input("Enter celesius: "))
            celisus_to_farenheit(c)
            
        elif choice == 2:
            f = float(input("Enter farenheit:  "))
            farenheit_to_celisus(f)
            
        elif choice == 3:
            break
        
        else:
            print("Invalid choice!!!")
            
            
main()
         
        