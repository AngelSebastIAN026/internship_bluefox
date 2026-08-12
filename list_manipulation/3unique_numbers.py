def main():
    numbers = input("Enter numbers: ")
    print(numbers)

    unique = []

    for number in numbers:
        if number not in unique:
            unique.append(number)

    print(unique)

main()

