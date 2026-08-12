def main() :
    
    integers = [4,5,6,7,8,9,10]
    
    largest = integers[0]
    smallest = integers[0]

    for num in integers:
        if num > largest:
            largest = num

        if num < smallest:
            smallest = num

    print("Largest:", largest)
    print("Smallest:", smallest)
    
main()