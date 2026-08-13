def main():
    numbers = input("Enter numbers: ").split()
    n = int(input("Enter n: "))

    numbers = [int(number) for number in numbers]

    result = numbers[n:] + numbers[:n]

    print(result)

main()