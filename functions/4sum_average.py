def sum_average(num):
    total = sum(num)
    avg = total / len(num)
    
    return total, avg


def main() :
    
    num = list(map(int, input("Enter the numbers: ").split()))
    
    result = sum_average(num)
    
    print(result)
    
main()
    