def celsius_to_fahrenheit(c):
    f = (c * 9/5) + 32
    print("Fahrenheit:", f)

def fahrenheit_to_celsius(f):
    c = (f - 32) * 5/9
    print("Celsius:", c)

def main():
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        c = float(input("Enter temperature in Celsius: "))
        celsius_to_fahrenheit(c)
    elif choice == "2":
        f = float(input("Enter temperature in Fahrenheit: "))
        fahrenheit_to_celsius(f)
    else:
        print("Invalid choice")


main()