school = {
    "name": "Green Valley School",

    "campus": {
        "main_block": {
            "classrooms": {
                "grade_8": {
                    "attendance_app": {
                        "status": "working"
                    },
                    "smart_board": {
                        "status": "bug"
                    }
                },
                "grade_10": {
                    "lab_booking": "working"
                }
            },

            "library": {
                "issue_book": {
                    "status": "bug",
                    "priority": "medium"
                },
                "return_book": {
                    "status": "working"
                }
            }
        },

        "sports_block": {
            "ground": {
                "booking": "bug"
            }
        }
    },

    "exams": {
        "internal": {
            "marks_entry": {
                "status": "working"
            }
        },
        "board": {
            "hall_ticket": {
                "download": {
                    "status": "bug"
                }
            }
        }
    }
}



def solve_bugs(data):

    for key, value in data.items():

        if isinstance(value, dict):
            solve_bugs(value)

        elif value == "bug":
            data[key] = "solved"


solve_bugs(school)

print(school)