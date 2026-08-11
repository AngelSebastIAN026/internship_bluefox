def main():
    str = (input("Enter the sentence: "))

    words = str.split()

    for word in words:
        print(word[0].upper() + word[1:], end=" ")

main()