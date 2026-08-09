def main() :
    num = int(input("Enter the number: "))
    
    prev = num -1
    total = prev + num
    
    for i in range (prev, num, total):
        print(i)
    
    print("num: ", num)
    print("prev: ", prev) 
    print("sum:", total)  
     
    
main() 

    