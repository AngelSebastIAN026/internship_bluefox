def main():
    integers = []

    even = []
    odd = [] 
 
 
 for i in range(n):
         number = int(input("Enter a number: "))
        integers.append(number)

    for number in integers:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)

    print("Even:", even)
    print("Odd:", odd)


main()