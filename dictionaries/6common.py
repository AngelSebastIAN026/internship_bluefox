def main() :
    list1 = ["1","2","3","4","5","6"]
    list2 = ["3","8","9","7","6"]
    
    common = []
    
    common = set(list1) & set(list2)
    
    print(common)
main()