# =====================================================================
# PROJECT: Wordle
# Create a program where the user must guess the 5 letter word.
# =====================================================================

# TOOLS
# TODO Import random so you can randomise the word

# VALUES
# TODO Create a list of at least 5 different 5-letter words
# TODO Create a variable called play and set it to True

# INTRODUCTION
# TODO Tell your user how to play wordle (make sure they know they must input 5 letter words)

# MAIN
# TODO Create a while loop that runs if play is true

    # TODO Create word variable and store a random word from your list (using random.choice)

    # USER INPUT
    # TODO Get user's first guess and save it into a variable
    # TODO Create a while loop if the guess is not 5 characters long
        # TODO Tell them it's not 5 letters and to try again

    # TODO Check if they got it correct and if they did, tell them so and then break the loop

    # TODO Create a for loop that loops 5 times
        # TODO Check if the current letter of user_input (user_input[i]) is the same as the i letter of the word and if it is tell them they got that letter correct

        # TODO Otherwise check if the current letter of user_input is in the word and if it is, tell them that letter is in the wrong position

        # TODO Else tell them that letter is wrong

# TODO Ask if they want to play again. If they don't, set play to false.


# ==========================================================
# EXTENSION
# Instead of telling the user one by one about their letters, put each correct letter and _ for a wrong letter into a list. 
# Then finally print the list (you can use "".join(list_name) to merge them into a string if you like)

# ==========================================================
# EXPERT
# Following on from the extension, add colour to the letters instead (Don't use _ for incorrect anymore). Green for correct, orange for wrong place, red for incorrect. You'll need to add the colour as you add them to the list

# print("\033[31mThis is Red Text\033[0m")
# print("\033[38;2;255;165;0mThis is Orange Text\033[0m")
# print("\033[32mThis is Green Text\033[0m")

# Further Extension: Structure with user defined functions

import random

words = ["BACON", "INPUT", "MATHS", "AUDIO", "CRATE"]
guess = ""
attempts = 6
answer = random.choice(words)

print("This is wordle. Guess a five letter word, and see what letters are correct.")
print("Green is right spot, right letter. Yellow is right letter, wrong spot. Red is completely wrong.")

while guess != answer and attempts != 0:
    print(f"You have {attempts} guesses left")
    guess = input("What word would you like to guess?\n").upper().strip()

    if len(guess) == 5:
        if guess == answer:
            break
        guessInfo = []
        for x in range(5):
            if guess[x] == answer[x]:
                guessInfo.append("32")

            elif guess[x] in answer:
                guessInfo.append("38;2;255;165;0")

            else:
                guessInfo.append("31")
            
        returnGuess = []
        for x in range(5):
            returnGuess.append(f"\033[{guessInfo[x]}m{guess[x]}\033[0m")

        print("".join(returnGuess))
        attempts -= 1

    else:
        print("Please input exactly 5 letters")

if attempts == 0:
    print(f"You didn't get it, lol. The answer was {answer}")
else:
    print(f"You got it in {6 - attempts} guesses")