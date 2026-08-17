import random

def main():
    
    while True:
        print("""
            select options:
            1.play game
            2. view highscore
            3.Exit
            """)
        
        choice = int(input("select the option: "))
        
        if choice == 1:
            number = random.randint(1, 100)
            
            while True:
                    guess = int(input("Guess the number: "))

                    if guess < number:
                        print("Higher!")

                    elif guess > number:
                        print("Lower!")

                    else:
                        print("Correct!")
                        break

        elif choice == 2:
            print("High score: Not available")

        elif choice == 3:
            print("Exiting...")
            break

        else:
            print("Invalid choice")


main()