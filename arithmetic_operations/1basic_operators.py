def sum_of_two_numbers(num1, num2):
    return num1 + num2

def sub_of_two_numbers(num1, num2):
    return num1 - num2

def mul_of_two_numbers(num1, num2):
    return num1 * num2

def div_of_two_numbers(num1, num2):
    return num1 / num2

def floor_div_of_two_numbers(num1, num2):
    return num1 // num2

def remain_of_two_numbers(num1, num2):
    return num1 % num2

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    print(f"Sum of {num1} + {num2} = {sum_of_two_numbers(num1, num2)}")
    print(f"Product of {num1} * {num2} = {mul_of_two_numbers(num1, num2)}")
    print(f"dividion of {num1} / {num2} = {div_of_two_numbers(num1, num2)}")
    print(f"Floor of {num1} // {num2} = {floor_div_of_two_numbers(num1, num2)}")
    print(f"modulus of {num1} % {num2 } = {remain_of_two_numbers(num1, num2)}")


main()