import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
          'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
          'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
          'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
          'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
nr_letters = int(input("How many letters you want in your password?\n")) 
nr_symbols = int(input(f"How many symbols you want?\n"))
nr_numbers = int(input(f"How many numbers you want?\n"))

result = str()

# Generate random letters for the password
for _ in range(0, nr_letters):
    result += letters[random.randint(0, len(letters) - 1)]

# Generate random symbols for the password
for _ in range(0, nr_symbols):
    result += symbols[random.randint(0, len(symbols) - 1)]

# Generate random numbers for the password
for _ in range(0, nr_numbers):
    result += numbers[random.randint(0, len(numbers) - 1)]

# Convert the result string to a list and shuffle it
result_sfle = list(result)
random.shuffle(result_sfle)

# Display the generated password
print('Your password is: ' + ''.join(result_sfle))