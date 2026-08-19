def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


def main():
    num = int(input("Enter a number: "))

    result = factorial(num)

    print("Factorial:", result)


main()
    
    