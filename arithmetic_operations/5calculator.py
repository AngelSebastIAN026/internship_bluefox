def simple_intrest():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest: "))
    time = float(input("Enter the time (in years): "))
    
    interest = (principal * rate * time) / 100
    
 
    print(f"Simple Interest: {interest}")
    
simple_intrest()