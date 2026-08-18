import random

def start_game():
    number = random.randint(1, 100)
    userguess = 0
    
    while True:
        guess = int(input("Guess the number: "))
        userguess = userguess + 1
            
        if guess < number:
            print("Higher!")
            
        elif guess > number:
            print("Lower!")
            
        else:
            print("Correct!")
            break
        
    return userguess
        
    
        
def main(): 
        
        high_score = None
              
        while True:
            print("""
                select options:
                1.play game
                2. view highscore
                3.Exit
                """)
            
            choice = int(input("select the option: "))
                
            if choice == 1:
                score = start_game()
                 
                if high_score is None or score < high_score:
                    high_score = score
                    print("New High Score!")   
        
            elif choice == 2:
                if high_score is None:
                    print("High score is not yet :")
                else:
                    print("High score is: ", high_score, "guesses")
                
        
            elif choice == 3:
                print("Exiting...")
                break
        
            else:
                print("Invalid choice")

main()