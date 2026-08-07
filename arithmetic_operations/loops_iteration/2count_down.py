import time

def main() :
    num = int(input("Enter the number: "))
    
    for i in range(num, -1, -1):
        print(i)
        time.sleep(1)
    print("Blast off")
        
main()