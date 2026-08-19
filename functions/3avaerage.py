def avg(*args):
    total = sum(args)
    average = total / len(args)
    return average


def main():
    print(avg(4, 8, 15, 16))
    


main()
    
