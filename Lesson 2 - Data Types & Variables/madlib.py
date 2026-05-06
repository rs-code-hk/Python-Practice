import random
# Create a short Madlib: Get input from your user (a bunch of words), 
print("Please input a random . . .")

# then output a madlib using those words.

# Ask user for a name and save it in a variable
name = input("Name\n")
# Ask user for an animal and save it in a variable
animal = input("Animal\n")
# Ask user for a colour and save it in a variable
colour = input("Colour\n")
# Ask user for an object and save it in a variable
inputObject = input("Object\n")
# Print your madlib using the 4 variables above.
#print(f"{name}'s {animal} is playing with their {colour} {inputObject}.")


# ----------------------------

# EXTENSION
# Research about 'print formatting in python'. 
# Use what you learn to rewrite your madlib into easier to read code.

# ----------------------------

# EXPERT (for those who already know some Python)
# Create a randomised madlib game
# GOAL: Just like above except...
#       Write 4-6 different madlibs and randomise which one is output.

# Name = 0, Animal = 1, Colour = 2, Object = 3
madlibs = ["{0}'s {1} is playing with their {2} {3}", 
           "Have you been feeding you {2} {1}, {3}s {0}?",
           "{0}, do you own this {1}? It's been chewing on my {2} {3}",
           "Well {0}, I'll have you know that my {1} is {2}, and it likes {3}"]

print(random.choice(madlibs).format(name, animal, colour, inputObject))