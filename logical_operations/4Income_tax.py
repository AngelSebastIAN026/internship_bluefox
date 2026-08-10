def main() :
    num = int(input("Enter the income: "))
    
    if num <= 10000:
        tax = 0
        
    elif num <= 20000:
        tax = (num - 10000) * 0.10
        
    else:
        tax = ((10000 * 0.10) + (num - 20000) * 0.20)
        
        print("tax = ", tax)
        
main()