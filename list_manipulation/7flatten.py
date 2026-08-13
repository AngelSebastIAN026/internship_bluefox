def main():

    numbers = [1, [2, 3], [4, [5, 6]]]
    result = []

    def flatten(numbers):
        for item in numbers:
            if type(item) == list:
                flatten(item)
            else:
                result.append(item)

    flatten(numbers)

    print(result)


main()