### WHAT ANIMAL ARE YOU QUIZ ###

# FIRST, create a basic Flowchart using the FLowchart Shapes to plan the flow of your 'what animal are you' quiz. 
# __________________________

# Write a 'what animal are you' quiz. 
# You can base this on the picture from last lesson, but make it simpler - 
# 3 questions and 4 animals.

notFinishedQuestion = True
outside = ""
meat = ""
level = ""
while notFinishedQuestion:
    outside = input("Do you prefer to be outside or inside?\n").upper()
    if outside in ["OUTSIDE", "INSIDE"]:
        notFinishedQuestion = False

notFinishedQuestion = True
while notFinishedQuestion:
    if outside == "INSIDE":
        meat = input("Do you prefer vegetables or meat?\n").upper()
        if meat == "VEGETABLES":
            print("You are a bunny")
            notFinishedQuestion = False
        elif meat == "MEAT":
            print("You are a dog")
            notFinishedQuestion = False
    elif outside == "OUTSIDE":
        level = input("Do you prefer to be high up or at sea level\n").upper()
        if level == "HIGH UP":
            print("You are a eagle")
            notFinishedQuestion = False
        elif level == "SEA LEVEL":
            print("You are a turtle")
            notFinishedQuestion = False

# Ask your user a question about themselves, giving them 2 options

# Check if they picked the first option

    # Ask the next question

    # Check if they picked the first option

        # Tell them they're animal 1

    # Otherwise

        # Tell them they're animal 2

# Otherwise

    # Ask the next question

    # Check if they picked the first option

        # Tell them they're animal 3

    # Otherwise

        # Tell them they're animal 4 

# __________________________

# EXTENSION
# Extend the quiz so there are 8 possible animals
# Create a Flowchart using the FLowchart Shapes to 

# __________________________

# EXTENSION 2
# Create a 'Which ??? are you?' Quiz
# This time allow all questions to have 4 possible answers (a,b,c and d) 
# and tally how many times they choose each
# Determine what they are at the end using the letter with the highest tally.
# Eg. If they picked mostly As, maybe they are Pikachu.