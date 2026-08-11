def main() :
    
    word = (input("Enter the word: "))
    
    for i in word:
        if i == " ":
            print("_", end="")
        else:
            print(i, end="")

        
main()