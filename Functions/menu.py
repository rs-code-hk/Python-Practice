"""
PROGRAM: Menu
This starts with a menu so users can run 1 of 3 different programs:
1.
2.
3.
"""

# INSTRUCTIONS
# TODO Create a menu that will run three different programs based on user input.
# TODO Each program will need to be its own function OR check out the EXPERT instructions below.

import sys
from pathlib import Path

root_dir = str(Path(__file__).resolve().parents[1])
sys.path.append(root_dir)

from MultidimensionalData import pokemon
from While import countryGuesser, numberGuesser

def main():
    while True:
        match input("What program would you like to run? 1. Pokemon, 2. country guesser, 3. number guesser?").strip().upper():
            case "1" | "POKEMON":
                pokemon.main()
            case "2" | "COUNTRY GUESSER":
                countryGuesser.main()
            case "3" | "NUMBER GUESSER":
                numberGuesser.main()

            case _:
                print("That's not an option")


main()























#===============================
#===============================
# EXTENSION
# TODO Go back to each program you chose and structure them with functions. 
# TODO Then recopy them over as multiple functions (rather than one)
# NOTE The main() function in your programs can be renamed as run_program_name() so it doesn't clash with this program's main()
#===============================
#===============================
# EXPERT
# TODO Instead of bringing the code from other programs into this file, use import to import locally.
# You'll need to start by editing your other files so all their code is in functions, with a main() function too.
# NOTE Check this out for info on importing locally: https://github.com/Year-11-Programming/Python-Practice-Projects/wiki/Import-Locals