# =====================================================================
# PROGRAM: Safe Cracker (The Digital Vault)
# =====================================================================

# SETUP YOUR VARIABLES
# TODO: Create a variable for the correct vault combination (e.g., "742").
# TODO: Create a variable to keep track of how many attempts the player has used (start at 0).


# INTRODUCE THE GAME
# TODO: Print a cool message explaining they are trying to hack a safe.
# TODO: Let them know that typing 'exit' will quit the game entirely.


# LOOP
# TODO: Create an infinite while loop
# Note: By using 'True', this loop will run forever unless we use 'break'!

    # TODO: Ask the user to enter the 3-digit combination (or type 'exit').
    #       Save their input into a variable called 'user_input'.


    # -----------------------------------------------------------------
    # SCENARIO A: The user wants to quit
    # -----------------------------------------------------------------
    # TODO: Check if 'user_input' is equal to the word 'exit'.
    #       If it is, print "Aborting mission..." and use 'break' to stop the loop!


    # -----------------------------------------------------------------
    # SCENARIO B: Invalid Input
    # -----------------------------------------------------------------
    # TODO: Check if their input is a valid number
    #       (Hint: use try except)
    #       If it's not, print "Error: Safe only accepts digits. Try again."
    #       Then, use 'continue' to skip the rest of the code and restart the loop.


    # -----------------------------------------------------------------
    # SCENARIO C: Processing a valid attempt
    # -----------------------------------------------------------------
    # If the code gets past Scenario B, it means they entered a valid 3-digit attempt!
    
    # TODO: Increase your attempts tracker variable by 1.


    # TODO: Check if 'user_input' matches the correct vault combination.
    #       If it does: Print "Vault unlocked! You found the treasure!" and 'break' out of the loop.
    #       If it doesn't: Print a message telling them the combination failed.


# GAME OVER
# ---------------------------------------------------------------------




# =========================================
# EXTENSION
# TODO Add a scenario D to your loop: Running out of time
    # -----------------------------------------------------------------
    # SCENARIO D: Running out of time (EXTENSION)
    # -----------------------------------------------------------------
    # TODO: Check if their attempts tracker has reached 5.
    #       If it has, print "Alarm triggered! Security is on the way!" and 'break' the loop.

# =========================================
# EXPERT
# Mastermind Version:
# Add a part that lets you check each digit (you'll need to use split()) and tells the user how many digits are correct in their guess
import random

correctCombo = random.randint(100, 999)
attempts = 0
MAX_ATTEMPTS = 15
print("Welcome Mr Bond, Mr White's goons are on the way, you must steal the P.L.O.T device. It is a 3 digit code")
print("If you type 'exit', then the program will exit")

while True:
    guess = input("What do you think the code is?\n").strip()
    if guess.upper() == "exit":
        attempts = -1
        break

    try:
        guess = int(guess)
    except:
        print("Error: Safe only accepts numbers")
    else:
        if attempts == MAX_ATTEMPTS:
            break

        attempts += 1
        if guess == correctCombo:
            break
        else:
            print("Incorrect")
            correctGuesses = 0
            
            tempCorrectGuess = list(str(correctCombo))
            tempCorrectGuess = list(map(int, tempCorrectGuess))
            tempGuess = list(str(guess))
            tempGuess = list(map(int, tempGuess))
            for i in tempGuess:
                if tempCorrectGuess.__contains__(i):
                    correctGuesses += 1
                    tempCorrectGuess.pop(tempCorrectGuess.index(i))

            print(f"You got {correctGuesses} numbers correct")

if attempts == MAX_ATTEMPTS:
    print("Mr white's men have caught you.")
    print(f"The number is {correctCombo}")
elif attempts == -1:
    print("You have exited the game")
else:
    print(f"You escaped in {attempts} attempts")

print("\n--- Game Over ---")