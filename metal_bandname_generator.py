import random

print("WELCOME TO THE HELLFIRE BAND KILLER NAME GENERATOR!")
      
# Gather input from the user
v1 = input("What was the baddest disease you got?\n")
v2 = input("Which part of your body did you have a horrible pain?\n")
v3 = input("When you are angry, what's the first thing you wanna do? ")

# List of possible things to add to the band name
things = ["skeleton", "demon", "fire", "hell", "cat", "turtle"]

# Generate and display the band name using random choice
print(f"Your band can be called:\n{v1}'n {v2} {random.choice(things)}'s {v3}")