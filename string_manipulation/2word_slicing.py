def remove_chars(s, n):
   return s[n:]
    
    
def main() :
    s = (input("Enter the word: "))
    n = int(input("Enter the number of characters to be removed: "))
    
    print (remove_chars(s, n))
    
main()