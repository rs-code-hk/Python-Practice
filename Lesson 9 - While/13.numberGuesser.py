# =====================================================================
# PROGRAM: Higher or Lower Number Guesser
# =====================================================================

# IMPORTS
# TODO: Import the 'random' module so you can generate a secret number.
import random
import sys



def checkNumber(number):
    global secret_number
    match number:
        case _ if number > secret_number:
            return [False, f"Less than {number}"]
        case _ if number < secret_number:
            return [False, f"More than {number}"]
        
        case secret_number:
            return [True, f"The number is {number}"]
        
# VARIABLES
# TODO: Generate a random number between 1 and 100 and save it to 'secret_number'.
while True:
    secret_number = random.randint(1, 100)
    guess = [False, 0]
    guesses = 0
    # TODO: Create a variable to keep track of the user's current guess.
    #       (Hint: Start it as 0 so it doesn't accidentally match the secret number!)


    # INTRODUCE THE GAME
    # TODO: Print a welcome message explaining that the number is between 1 and 100.
    print("In this game, you have to guess the number! (1-100)")

    while guess[0] == False:
        try:
            print(f"You have done {guesses} {"guess" if guesses == 1 else "guesses"}")
            guess[1] = input("What number would you like to guess?\n").strip()
            if guess[1] == "exit":
                print("Exiting")
                break
            guess[1] = int(guess[1])
        except:
            print("That isn't a number")
            guess[1] = 0
        else:
            guesses += 1
            returnedNum = checkNumber(guess[1])
            guess[0] = returnedNum[0]
            print(returnedNum[1])

    print(f"You did it in {guesses} {"guess" if guesses == 1 else "guesses"}")
    print("Type yes to play again")
    if input().upper().strip() != "YES":
        break




# START THE GAME
# TODO: Start a 'while' loop that keeps running AS LONG AS the 
#       user's guess is NOT EQUAL to the secret_number.

    
    # TODO: Ask the user to guess a number. 
    #       (CRITICAL HINT: Remember to convert their input into an integer!)


    # TODO: Create an 'if' statement to check if their guess is TOO LOW.
    #       If it is, print "Too low! Try a higher number."


    # TODO: Create an 'elif' statement to check if their guess is TOO HIGH.
    #       If it is, print "Too high! Try a lower number."


# GAME OVER / WINNING MESSAGE
# TODO: Print a big victory message telling them they got it right!

# ===========================================
# EXTENSION
# TODO: Create a play again option (you'll need to loop the whole code, including creating the random number)
# TODO: Add an extra condition that tells them if they are within 5 of the secret number

# ===========================================
# EXPERT
# TODO: Try to structure the program using defined functions