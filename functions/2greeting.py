
    
    
def greetings_name(name, greetings = "Hello"):
    print(greetings + "," + name)
    
    
def main():
    
    name = (input("Enter the name: "))
    greetings_name(name)
    greetings_name(name, greetings = "hi")
    
main()
