food_app = {
    "app": "QuickBite",

    "modules": {
        "customer": {
            "home": {
                "search": {
                    "filter": {
                        "status": "working"
                    }
                },
                "offers": "working"
            },

            "cart": {
                "add_item": {
                    "status": "bug"
                },
                "remove_item": {
                    "status": "working"
                }
            }
        },

        "restaurant": {
            "menu": {
                "update_price": "bug"
            },
            "orders": {
                "accept": {
                    "status": "working"
                },
                "reject": {
                    "reason": {
                        "status": "bug"
                    }
                }
            }
        }
    },

    "payments": {
        "upi": {
            "status": "working"
        },
        "card": {
            "otp": {
                "verify": "bug"
            }
        }
    },

    "support": {
        "chat": "working",
        "call": {
            "connect": {
                "status": "bug"
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


solve_bugs(food_app)

print(food_app)