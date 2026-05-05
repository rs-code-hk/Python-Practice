### Create a 3-part guessing game ###

# Give your user the first hint and wait for input

# Give your user the second hint and wait for input

# Give your user the final hint and wait for input

# Tell your user the answer

hints = ["This is an amphibian\n", "This has green skin\n", "This animals ribbits around\n"]

print("Welcome to the AMAZING DIGITAL GUESSING GAME!")
print("(Not derivative)")
name = input("But first, what's your name?\n")
print(f"Good to meet you {name}. My name is staff.")
print("Okay, your first hint!!!")
answered = False

for x in hints:
    if not answered:
        guess = input(x).upper()
        if guess == "FROG":
            print("That is correct!!! Good job!")
            answered = True

if not answered:
    print("The correct answer was a frog.")


# ------------------------------

# EXTENSION
# Create another guessing game


# ------------------------------

# EXPERT (for those who already know some Python)
# Your 3-part guessing game should have:
# + An introduction
# + A conclusion
# + It should check if the user is correct and stop giving hints if they are
# + It should give points based on how quickly the user got it correct