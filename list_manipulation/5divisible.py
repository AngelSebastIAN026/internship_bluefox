def main():
    n = int(input("How many numbers "))

    numbers = []

    for i in range(n):
        num = int(input("Enter a number: "))
        numbers.append(num)

    for num in numbers:
        if num % 5 == 0:
            print(num)


main()