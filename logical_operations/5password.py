def main() :
    password = str(input("Enter the password: "))
    
    if len(password) <= 8:
       print("password is incorrect, must have 8 characters")
    if not any(char.isdigit() for char in password):
        print("password must have a digit")
    if not any(char.isupper() for char in password):
        print("password must have a uppercase")
        
main()