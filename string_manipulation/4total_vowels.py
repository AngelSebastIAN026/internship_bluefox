def main() :
    str = (input("Enter the word: "))
    
    vowels = {"a", "e", "i", "o", "u"}
    count = 0
    
    for ch in str:
        if ch.lower() in vowels:
            count += 1

    print("Number of vowels:", count)

main()