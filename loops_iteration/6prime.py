def main() :
    count = 0
    
    for num in range (2, 21):
    
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            count += 1
            if count % 2 == 0:
                print(num)
        
   
        
main()