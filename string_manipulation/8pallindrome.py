def main() :
    
    str = (input("Enter the word: "))
    
    str = str.replace(" ", " ").lower()
    
    if str == str[::-1]:
        print("pallindrome")
    else:
        print("not Pallindrome")
        
main()