def main() :
    w1 = (input("Enter the first word: "))
    w2 = (input("enter the second word: "))
    
    if len (w1) == len(w2) and sorted(w1) == sorted(w2):
        print("anagram")
    else:
        print("Not anagram")
        
main()
        