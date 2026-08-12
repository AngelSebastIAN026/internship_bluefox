def check(numbers):
    return numbers[0] == numbers[-1]

 

def main():
    n = int(input("How many numbers :"))
    numbers = []

    for i in range(n):
        num = int(input("Enter a number: "))
        numbers.append(num)

    print(check(numbers))


main()