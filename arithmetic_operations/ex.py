def main():
    age = int(input("Enter the age: "))
    print(["adult", "minor"][age <= 18])

main()