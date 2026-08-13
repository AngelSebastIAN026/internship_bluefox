def main():
    numbers = []

    even = []
    odd = []

    for i in range(10):
        number = int(input("Enter a number: "))
        numbers.append(number)

    for number in numbers:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)

    print("Even:", even)
    print("Odd:", odd)


main()