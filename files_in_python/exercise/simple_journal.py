# ✅ Task 1: Simple Journal
# Write a script where the user types their thoughts and it saves into a file called journal.txt.

# Use append mode so it saves every time

# After saving, ask if they want to read past entries

from datetime import datetime


# current date & time
current_date = datetime.today().strftime("%d/%m/%Y")
current_time = datetime.now().strftime("%I:%M:%S %p")

# open file in append mode.
with open("journal.txt", "a") as file:
    your_thoughts = input(f"what are you thoughts today ({current_date}): ")
    file.write(f"Journal Entry - {current_date} & {current_time}\n{'---' * 100}\n\n{your_thoughts}\n\n\n")
