def sum_of_two_numbers(num1, num2):
    return num1 + num2


def mul_of_two_numbers(num1, num2):
    return num1 * num2


def sub_of_two_numbers(num1, num2):
    return num1 - num2


def div_of_two_numbers(num1, num2):
    return num1 / num2


def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(f"Sum: {sum_of_two_numbers(num1, num2)}")
    print(f"Product: {mul_of_two_numbers(num1, num2)}")
    print(f"Difference: {sub_of_two_numbers(num1, num2)}")
    print(f"Quotient: {div_of_two_numbers(num1, num2)}")


if __name__ == "__main__":
    main()

