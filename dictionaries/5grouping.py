def main() :
    words1 = (input("Enter the words: ")).split()
    words2 = {}
    
    for word in words1:
        first = word[0] 
        
        if first not in  words2:
            words2[first] = []
        
            words2[first].append(words1)
        
    print(words2)
main()
    