import tkinter as tk
import random

# Function to generate band name
def generate_band_name():
    v1 = entry_disease.get()
    v2 = entry_body_part.get()
    v3 = entry_action.get()
    things = ["skeleton", "demon", "fire", "hell", "cat", "turtle"]
    band_name = f"{v1}'n {v2} {random.choice(things)}'s {v3}"
    result_label.config(text=f"Your band can be called:\n{band_name}")

# Set up the GUI
root = tk.Tk()
root.title("Hellfire Band Killer Name Generator")
root.geometry("600x400")

# Title
title_label = tk.Label(root, text="WELCOME TO\nTHE HELLFIRE BAND KILLER\nNAME GENERATOR!", font=("Arial", 12, "bold"))
title_label.pack(pady=10)

# Input for disease
disease_label = tk.Label(root, text="What was the baddest disease you got?")
disease_label.pack()
entry_disease = tk.Entry(root)
entry_disease.pack(pady=5)

# Input for body part
body_part_label = tk.Label(root, text="Which part of your body did you have horrible pain?")
body_part_label.pack()
entry_body_part = tk.Entry(root)
entry_body_part.pack(pady=5)

# Input for action
action_label = tk.Label(root, text="When you are angry, what's the first thing you want to do?")
action_label.pack()
entry_action = tk.Entry(root)
entry_action.pack(pady=5)

# Button to generate band name
generate_button = tk.Button(root, text="Generate Name", command=generate_band_name)
generate_button.pack(pady=10)

# Result display
result_label = tk.Label(root, text="", font=("Arial", 10))
result_label.pack(pady=20)

# Run the GUI main loop
root.mainloop()
