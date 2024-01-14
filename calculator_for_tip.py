# Display a welcome message
print("We gonna help you to calculate your tip!")

# Get input for the total bill
bill = float(input("What was the total bill? $"))

# Get input for the number of people to split the bill
numppl = int(input("How many people to split the bill? "))

# Get input for the tip percentage
perc = float(input("What percentage tip would you like to give? 10, 12, or 15? "))

# Function to convert percentage to a multiplier
def percentage(pcent):
    if pcent == 10:
        return float(1.10)
    elif pcent == 12:
        return float(1.12)
    elif pcent == 15:
        return float(1.15)
    else:
        # Handle invalid input and recursively ask for a valid percentage
        print("Invalid tip value, must insert 10, 12, or 15")
        x = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
        return percentage(x)

# Get the final tip multiplier using the percentage function
final_per = percentage(perc)

# Calculate the total amount to be paid by each person
total = ((bill / numppl) * final_per)

# Display the amount each person should pay, rounded to 2 decimal places
print(f"Each person should pay: {round(total, 2)} ")