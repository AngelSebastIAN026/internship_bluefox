def main():
    students = {
        "angel": {
            "Maths": "A",
            "English": "B",
            "Science": "A"
        },
        "emil": {
            "Maths": "B",
            "English": "A",
            "Science": "B"
        }
    }

    name = input("Enter student name: ")

    if name in students:
        print(students[name])
    else:
        print("Student not found")


main()