import random
import os
import time

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def show(choice):
    if choice == "1":
        print(rock)
    elif choice == "2":
        print(paper)
    elif choice == "3":
        print(scissors)

def compare(player, cpu):
    if player == cpu:
        return "draw"
    elif player == "1":
        if cpu== "2":
            return "lose"
        else:
            return "win"
    elif player == "2":
        if cpu == "1":
            return "win"
        else:
            return "lose"
    elif player == "3":
        if cpu == "1":
            return "lose"
        else:
            return "win"

def game():
    nowinner = True
    score = 0
    cpu_score = 0

    while nowinner:
        input("First to get 5 points wins! Press enter to continue.")
        os.system('cls')
        player_choice = input("type 1 to rock, 2 to paper or 3 to scissors: ")
        while player_choice != "1" and player_choice !="2" and player_choice != "3":
            player_choice = input("Type a valid number: 1, 2 or 3: ")

        cpu_choice = str(random.randint(1,3))
        
        show(player_choice)
        print("YOU")
        print("________\n")
        print("CPU")
        show(cpu_choice)
        
        if compare(player_choice, cpu_choice) == "draw":
            print("It's a draw!")
            print(f"Your score is: {score}\nCPU score is: {cpu_score}")
        elif compare(player_choice, cpu_choice) == "win":
            print("You got a point!")
            score += 1
            print(f"Your score is: {score}\nCPU score is: {cpu_score}")
            if score == 5 or cpu_score == 5:
                nowinner = False
        else:

            print("you lose")
            cpu_score += 1
            print(f"Your score is: {score}\nCPU score is: {cpu_score}")
            if score == 5 or cpu_score == 5:
                nowinner = False

    if input("Let's play again? Type Y or N: ").lower() == "y":
        game()
    else:
        print("Thanks for playing!")

game()