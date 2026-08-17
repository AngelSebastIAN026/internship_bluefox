def sum_of_two(num1, num2): 
    return(num1 + num2)
        
def mul_of_two(num1,num2):
    return(num1 * num2)
        
def div_of_two(num1,num2):
    return(num1 / num2)
        
def diff_of_two(num1,num2):
    return(num1 - num2)
        
def factorial(num):
    pass
    
    
def main() :

    select_option_message = """
        Select the operation:
        1. Sum
        2. Mul
        3. Div
        4. diff
        5. Exit
        Enter your choice:
        """

    while True:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        
        if num1 < 1 or num1 > 5 or num2 < 1 or num2 > 5:
            print("Invalid choice, only enter number between 1-5")
            continue
            
        choice = int(input(select_option_message))
        match choice:
            case 1:
                print(f"Sum of {num1} and {num2} is {sum_of_two(num1, num2)}")

            case 2:
                print(f"Mul of {num1} and {num2} is {mul_of_two(num1, num2)}")

            case 3:
                print(f"Div of {num1} and {num2} is {div_of_two(num1, num2)}")

            case 4:
                print(f"Diff of {num1} and {num2} is {diff_of_two(num1, num2)}")

            case 5:
                print("Exiting...")
                break

            case _:
                print("Invalid choice. Please select 1-5.")
main()