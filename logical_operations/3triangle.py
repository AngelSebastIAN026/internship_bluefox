def main():
    num1 = int(input("Enter the first side: "))
    num2 = int(input("Enter the second side: "))
    num3 = int(input("Enter the third side: "))
    
    if num1 == num2 == num3:
        print("it is an equilateral triangle")
    
    elif (num1 == num2 or num2 == num3 or num1 == num3):
        print("it is an isosceles triangle")
    
    else:
        print("it is an scalene triangle")
    
main()
