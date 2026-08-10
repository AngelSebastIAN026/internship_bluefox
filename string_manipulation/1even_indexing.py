def main() :
    str = (input("Enter the word: "))
    
    for i in range(len(str)):
        if i % 2 == 0:
            print(str[i])
main()