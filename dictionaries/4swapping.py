def main() :
    word1 = {
        
        "a" : 1,
        "b" : 2,
        "c" : 3,
        "d" : 4
    }
    
    print(word1)
    
    word2 = {}
    
    for key in word1:
    
        value = word1[key]
        word2[value] = key
        
    print( )
    
    print(word2)
    
main()
    