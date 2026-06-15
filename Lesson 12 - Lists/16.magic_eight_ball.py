# =====================================================================
# PROJECT: The Magic 8-Ball Fortune Teller
# Create a program that gives random responses to yes/no questions
# =====================================================================

import random
commonResponses = ["Yes", "No", "Maybe", "Try again later", "Absolutely", "Absolutely not"]
rareResponses = ["You should talk to a professional about that", "I'm not legally obligated to answer anything", "Uhh, uhh, umm, IDK", "Talk to me later, I'm playing Balatro RN"]
print("This is a magic eight ball")
print("Type Exit to leave")

# TOOLS
# TODO: Import the 'random' module so we can pick a random index later.


# RESPONSES
# TODO: Create a list called 'responses' that contains at least 8 different 
#       8-ball answers (strings). There should be positive answers, negative answers and neutral answers.
#       Examples: "Yes, definitely!", "Ask again later.", "Outlook not so good."


# MAIN LOOP
while True:
# TODO Create an infinite loop
    
    # TODO: Ask the user to type in a Yes/No question about their future and save it in a variable.
    #       (Or tell them to type 'quit' to leave).
    
    # Check if the user wants to exit and break from the loop if they do.
        
    # RANDOM REPSONSE
    # TODO: Step A: Calculate the last valid index of your list.
    #       (Remember: If a list has 5 items, the indexes are 0, 1, 2, 3, 4).
    #       Use random.randint() to get a number between 0 and that last index.
    #       Save it in a variable called 'random_index'.
    
    
    # TODO: Step B: Use your 'random_index' to grab the matching answer 
    #       out of your 'responses' list.
    #       Save it in a variable called 'chosen_fortune'.

    # TODO Print the result

    # OR
    if input("What is your question?\n").strip().upper() == "EXIT":
        break
    
    chance = random.random()
    print(f"Magic Eight Ball: {random.choice(rareResponses if chance > 0.8 else commonResponses)}")

# TODO Say goodbye to let them know the program has ended.
print("Goodbye")

# ==================================================
# EXTENSION
# Common and rare responses
# TODO Split your responses into 2 lists. A common responses list and a rare responses list
# TODO Use random.random() or randint() to get a percentage
# TODO Check if the number is lower than 0.8 and use the common list to give a response if it is
# TODO Otherwise use the rare list

# ===================================================
# EXPERT
# Try creating a magic eight ball that gives random responses based on the question (eg. positive, negative, snarky, funny responses)
# TODO Create a dictionary (or multiple lists)
# TODO Check for key words in the question to decide what type of response. Eg. "will I" has positive responses, short questions have snarky responses, "think" has funny responses, etc.


