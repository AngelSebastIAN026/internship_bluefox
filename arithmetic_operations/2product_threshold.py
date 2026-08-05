def compare_product_and_sum(a, b):
    product = a * b
    if product <= 1000:
        return product
    else:
        return a + b

def main():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print(compare_product_and_sum(a, b))

if __name__ == "__main__":
    main()
