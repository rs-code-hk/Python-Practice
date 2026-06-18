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
def main():
    class attack():
        def __init__(self, inName:str, inDesc:str, inPower:int, inMoveType:str, inSpecial:bool):
            self.name = inName
            self.desc = inDesc
            self.power = inPower
            self.moveType = inMoveType
            self.special = inSpecial

        def useAttack(self, pokemonType, pokemonAttack):
            print(f"Uses {self.name}")
            print(f"Uses {self.desc}")
            dmgMult = 1.0
            if random.randint(1, 24) == 1:
                print("It crit!")
                dmgMult *= 1.5

            if self.moveType in pokemonType:
                dmgMult *= 1.5

            print(f"It dealt {self.power * pokemonAttack} damage!")
            return self.power * pokemonAttack

    # Pokemon class
    class pokemon():
        def __init__(self, inName:str, inHealth:int, inType:list, inMoves:list, inAttack:int, inSpecialAttack:int):
            self.name = inName
            self.health = inHealth
            self.pokemonType = inType
            self.moves = inMoves
            self.attack = inAttack
            self.specialAttack = inSpecialAttack

        def pickAttack(self, atkNum):
            atk = self.moves[atkNum]
            if atk.special:
                return atk.useAttack(self.pokemonType, self.specialAttack)
            return atk.useAttack(self.pokemonType, self.attack)

    # List of wild pokemon
    bulbasaurMoves = [
        attack("Tackle", "A full-body charge attack", 0.4, "normal", False),
        attack("Vine Whip", "Whips the foe with slender vines", 0.45, "grass", False),
        attack("Razor Leaf", "Cuts the enemy with leaves", 0.55, "grass", False),
        attack("Magical Leaf", "Attacks with a strange leaf that cannot be avoided", 0.6, "grass", True)
    ]

    wildPokemonList = [
        pokemon("bublasaur", 45, ["grass"], bulbasaurMoves, 49, 65)
    ]

    # List of player pokemon

    giratinaMoves = [
        attack("Slash", "The target is slashed by claws", 0.7, "normal", False),
        attack("Dragon Breath", "A strong breath attack", 0.6, "dragon", True),
        attack("Ancient Power", "An ancient power is used to attack", 0.6, "rock", True),
        attack("Shadow Sneak", "The user extends his shadow and attacks the foe from behind", 0.4, "shadow", False)
    ]

    playerPokemonList = [
        pokemon("giratina", 150, ["dragon", "ghost"], giratinaMoves, 100, 100)
    ]

    playerPokemon = random.choice(playerPokemonList)
    wildPokemon = random.choice(wildPokemonList)

    print(f"{playerPokemon.name} (Player) VS {wildPokemon.name}")

    while playerPokemon.health > 0 and wildPokemon.health > 0:
        print(f"Player Health: {playerPokemon.health}")
        print(f"Enemy Health: {wildPokemon.health}")

        print("What attack would you like to use? (Use number)")
        for i, j in enumerate(playerPokemon.moves):
            print(f"{i+1}. {j.name}")

        attackNum = input()

        try:
            attackNum = int(attackNum)
            wildPokemon.health -= playerPokemon.pickAttack(attackNum - 1)
        except ValueError:
            print("Please put a number")
            continue
        except IndexError:
            print("That isn't a move")
            continue

        playerPokemon.health -= wildPokemon.pickAttack(random.randint(0, 3))

    if playerPokemon.health < 1 and wildPokemon.health < 1:
        print("It's a tie!")
    elif playerPokemon.health < 1:
        print("You lose!")
    elif wildPokemon.health < 1:
        print("You won!")
    else:
        print("Error! Match ended early")

main()