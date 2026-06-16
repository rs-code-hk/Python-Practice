# =====================================================================
# PROJECT: Pokemon
# Create a battle program where you battle a random pokemon
# =====================================================================

# TODO Import random module

# Wild Pokemon
# TODO Create a multidimensional list that holds 4 pokemon names and their max health (you choose)
# User Pokemon
# TODO Create a multidimensional list that holds 4 pokemon attacks and their different damage

# TODO Create a variable to hold a randomised wild pokemon
# TODO Create a current_health variable and set it to the max health of the random pokemon
# TODO Tell the user what pokemon they're facing
# TODO Create a while loop that continues until current health <= 0
    # TODO Ask the user which attack they'd like to use (list all 4 options, numbered); save input
    # TODO Use try except to ensure the user has input a number; if they didn't tell them so and then use 'continue' to restart the loop
    # TODO Using the number, get the attack damage value and minus it from current health

# TODO Tell the user they defeated the pokemon

# ====================================================
# EXTENSION
# NOTE: Only do the extension once you have completed the project update (with dictionaries)

# TODO: Give your wild pokemon each an attack value as well, then allow it to attack the user back each turn (You'' need a player health)
# TODO: Change your 'user pokemon' to a list of different pokemon they can choose from. Each pokemon will have their own list of attacks.
# TODO: Give all pokemon a type. Create a new dictionary of types that each has a dictionary of strengths and weaknesses. Use this to change the damage.

import random

# Attack class
class attack():
    def __init__(self, inName:str, inDesc:str, inPower:int, inMoveType:str, inSpecial:bool):
        self.name = inName
        self.desc = inDesc
        self.power = inPower
        self.moveType = inMoveType
        self.special = inSpecial

    def useAttack(self, pokemonType, pokemonAttack):
        print(f"Uses {self.name}")
        dmgMult = 1.0
        if random.randint(1, 24) == 1:
            dmgMult *= 1.5

        if pokemonType == self.moveType:
            dmgMult *= 1.5

        return self.power * pokemonAttack

# Pokemon class
class pokemon():
    def __init__(self, inName:str, inHealth:int, inType:str, inMoves:list, inAttack:int, inSpecialAttack:int):
        self.name = inName
        self.health = inHealth
        self.pokemonType = inType
        self.moves = inMoves
        self.attack = inAttack
        self.specialAttack = inSpecialAttack

    def pickAttack(self):
        atk = random.choice(self.moves)
        if atk.special:
            return atk, self.specialAttack

# List of wild pokemon
bulbasaurMoves = [
    attack("Tackle", "A full-body charge attack", 40, "normal", False),
    attack("Vine Whip")
]

wildPokemon = {
    "Bulbasaur": [pokemon("bublasaur", 45, )]
}