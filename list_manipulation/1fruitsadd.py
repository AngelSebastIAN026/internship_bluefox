def main() :

    fruits = ["Apple","Banana","Mango","blue berry","black berry"]
    print("existing fruits: ", fruits)

    new_fruit = input("Enter a new fruit : ")

    fruits.append(new_fruit)
    del fruits[1]

    print("updated fruits:", fruits)
    
main()

