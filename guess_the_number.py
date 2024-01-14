import random
import os

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

def replay():
    print(logo)
    guessing = True
    #randomizing a number
    answer = random.choice(range(1, 100)) 
    # the answer for debug print(answer)

    #WELCOME and choosing difficulty
    print("Welcome to the guessing the number game!\nThe number is between 1 and 100")
    if input("Choose a difficulty, type: 1 for easy(10 lives) or 2 for hard(5 lives)\n") == "1":
        lives = 10
    else:
        lives = 5
    print(f"You have {lives} attempts remaining to guess the number.")
       
    while guessing == True:
        guess = int(input("Make a guess: "))
        # CHECK IF THE GUESS WAS RIGHT
        if guess == answer:
            guessing = False
            if input("You did it!\nPlay again? Y/N: ").lower() == "y":
                os.system('cls')
                replay()
            else:
                guessing = False
                os.system('cls')
                print("Thank you for playing!")
                return  
        # CHECK IF THE GUESS WAS HIGHER OR LOWER
        elif guess < answer:
            print("The number is higher than that!")
            lives = lives - 1       
        elif guess > answer:
            print("The number is lower than that!")
            lives = lives - 1
        # CHECK IF PLAYER HAVE GUESSES LEFT
        if lives == 0:
            os.system('cls')
            guessing = False
            if input("You don't have more attempts...\nPlay again? Y/N: ").lower() == "y":
                os.system('cls')
                replay()
            else:
                guessing = False
                os.system('cls')
                print("Thank you for playing!")
                return                             
        print(f"You have {lives} attempts remaining to guess the number.")


replay()
