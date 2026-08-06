def main():
    num = int(input("Enter the year: "))

    if num % 400 == 0:
        print(f"{num} is a leap year")
    elif num % 100 == 0:
        print(f"{num} is not a leap year")
    elif num % 4 == 0:
        print(f"{num} is a leap year")
    else:
        print(f"{num} is not a leap year")
main()