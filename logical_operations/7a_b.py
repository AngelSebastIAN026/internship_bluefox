def main() :
    mark = int(input("Enter the mark: "))
    
    if mark >= 85:
        print("The grade is A")
    elif mark >= 74:
        print("The grade is B")
    elif mark >= 64:
        print("The grade is C")
    elif mark >= 54:
        print("The grade is D")
    else:
        print("The grade is F")
    
    print("mark is", mark)    
    
        
main()