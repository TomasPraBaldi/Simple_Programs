import os

memory = []
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the secret live auction program.")

def infos():
    name = input("What is your name?\nName: ")
    bid = input("Place your bid: $")
    os.system('cls')
    memory.append({"name":name,"bid":bid})
    if input("Are other user who want to bid? Y/N: ").lower() == "y":
        os.system('cls')
        infos()
infos()
os.system('cls')
winner = max(memory, key=lambda x:x['bid'])

print(f"The winner is {winner['name']}, with the highest bid of {winner['bid']}")
