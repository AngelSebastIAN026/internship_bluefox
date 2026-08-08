def main() :
    word = (input("Enter the word: "))
    reversed_word = ""
    
    for char in word:
        reversed_word = char + reversed_word
        
    print("reversed_word:", reversed_word)
        
main()  
     
