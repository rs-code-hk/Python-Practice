import random
# =====================================================================
# Task: Country Guessing Game
# =====================================================================

# VALUES
# TODO: Create a variable to store the correct country (e.g., "Italy").
def main():
    while True:
        possibleCountry = ["ITALY", "FRANCE", "EGYPT", "AUSTRALIA", "USA", "DUBAI", "VATICAN CITY"]
        country = random.choice(possibleCountry)
        print(country)
        # TODO: Create a variable to keep track of the user's current guess. 
        guess = ""
        points = 20
        #       (Hint: Start it as an empty string "" so the loop runs at least once!)

        print("This is a game where you guess the country!")

        # LOOP
        # TODO: Start a 'while' loop. 
        #       The loop should keep running AS LONG AS the user's guess 
        #       is NOT EQUAL to the correct country.
        while guess != country:
            print(f"You have {points} {"point" if points == 1 else "points"}.")
            guess = input("What country do you think it is?\n").strip().upper()

            if guess != country:
                print("That's wrong. Try again")
                points -= 1

            if points == 0:
                print("You lose!")
                break
            
            # TODO: Ask the user for their guess and save it to your guess variable.
            #       (Remember: This changes the loop condition so it doesn't run forever!)
            
            # TODO: (Optional) Add an 'if' statement inside the loop.
            #       If they guessed wrong, print an encouraging message or an extra hint.
            #       If they guessed right, the loop will automatically exit on the next check!

        if points > 0:
            print("Congratulations! You win!")
            print(f"You have {points} {"point" if points == 1 else "points"}.")

        if input("Type yes to play again\n").strip().upper() != "YES":
            break


main()
# GAME OVER / WINNING MESSAGE
# TODO: Print a congratulatory message celebrating their win!

# ================================================================
# EXTENSION
# TODO: Add an introduction
# TODO: Add a scoring system (starts at 20, lose 1 point for each wrong guess)
# TODO: Add a lose condition (if score reaches 0)

#==================================================================
# EXPERT
# TODO: Make the game unique (use a list of countries and randomly select one)
# TODO: Add a play again option