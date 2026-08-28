def main():
    with open("existing.txt", "r") as file:
        contents = file.read()

    words = contents.split()
    word_count = len(words)

    print("Total number of words:", word_count)


main()