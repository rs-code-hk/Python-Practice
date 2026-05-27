import random

bossTitle = ["Lord of chaos", "Battery sold seperately", "FDA approved", "Lawman for hire", "R18 (Gore)", "DM's favourite child", "Employee of the month", "Registered trademark of Hydranger Co", "Survivor of 7/11", "1000 hours in weather.com", "Lord of Reddit", "Average basement dweller", "Tacos?"]

playerHealth = 50.0
playerPotions = 5
playerArrows = 10

bossHealth = 100.0

while bossHealth > 0 and playerHealth > 0:
    print(f"You have {playerHealth/50*100}% health")
    print(f"True aspect of hydranger, {random.choice(bossTitle)} has {bossHealth}% health")
    print()
    match input(f"Would you like attack with your sword, bow ({playerArrows} arrows left), or heal ({playerPotions} potions left)?\n").strip().upper():
        case "SWORD":
            damage = random.randint(2, 6)
            bossHealth -= damage
            print(f"You dealt {damage} damage to True aspect of hydranger, {random.choice(bossTitle)}, it has {bossHealth}% health")
            damage = random.randint(4, 8)
            playerHealth -= damage
            print(f"True aspect of hydranger, {random.choice(bossTitle)} dealt {damage} damage. You have {playerHealth * 2}% health")
        case "BOW":
            if playerArrows == 0:
                print("You have no arrows left")
            else:
                playerArrows -= 1
                damage = random.randint(5, 10)
                bossHealth -= damage
                print(f"You dealt {damage} damage to True aspect of hydranger, {random.choice(bossTitle)}, it has {bossHealth}% health")
                damage = random.randint(4, 8)
                playerHealth -= damage
                print(f"True aspect of hydranger, {random.choice(bossTitle)} dealt {damage} damage. You have {playerHealth * 2}% health")

        case "HEAL":
            if playerPotions == 0:
                print("You have no potions left")
            else:
                playerPotions -= 1
                playerHealth += 20
                print(f"You healed 20 health, you now have {playerHealth * 2}%")
                if playerHealth > 50:
                    print("The magic flowing through your body is too much. You die!")
                    playerHealth = 0
        case _:
            print("This isn't a option")

if playerHealth < 1:
    print(f"True aspect of hydranger, {random.choice(bossTitle)} has claimed victory")
else:
    print(f"You have defeated True aspect of hydranger, {random.choice(bossTitle)}")