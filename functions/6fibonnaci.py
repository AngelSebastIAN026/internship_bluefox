def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    n = int(input("Enter n: "))
    print("Fibonacci number:", fibonacci(n))


main()