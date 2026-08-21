def main():
    with open("ex.txt", "w") as file:
        file.write("Hi I'm Angel \n")
        file.write("Hello I'm Angel \n")
        file.write("Bye I'm Angel \n")

    with open("ex.txt", "r") as file:
        contents = file.read()

    print(contents)


main()