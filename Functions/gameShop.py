"""
PROGRAM: Game Shop
This program runs a game shop for items.
"""

# INSTRUCTIONS
# TODO Code a game shop for players to buy and sell items
class item():
    def __init__(self, inGold, inDesc):
        self.gold = inGold
        self.desc = inDesc

    def __str__(self):
        return f"{self.desc} - Costs {self.gold} gold"

gold = 50
forSale = {
    "SWORD": item(10, "A basic longsword"),
    "SWORD OF DANGER DETECTION": item(5, "Of course it's always glowing, swords are sharp!"),
    "RING OF FIRE DETECTION": item(10, "A fire distinguisher (Range: Touch)"),
    "GUN OF IMMACULATE ACCURACY": item(50, "Always hits the closest thing to it"),
    "HAMSTER OF WORLD DEVOURING": item(1, "The hamster that must destroy the world. PLS BUY THIS. I AM VERY SCARED."),
    "BAG OF HOLDING": item(20, "Unfortunately it's full of air"),
    "BAG OF WITHOLDING": item(20, "It witholds any items you put in it")
}
print("This is a item shop. Buy your favourite, totally not cursed items here.")
print("Type exit to exit")
while True:
    print(f"You have {gold} gold left")
    for i in forSale:
        print(f"{i.lower().capitalize()} - {str(forSale[i])}")

    purchase = input("What would you like to buy?\n").strip().upper()
    if purchase.upper() == "EXIT":
        print("I hope you had a nice shopping trip")
        break

    try:
        getItem = forSale[purchase]
        if gold >= getItem.gold:
            print(f"You bought a {purchase.lower().capitalize()}")
            gold -= getItem.gold
            del forSale[purchase]

    except:
        print("That isn't an item")















#===============================
#===============================
# EXTENSION
# Display extra info for each item (on top of price): attack, defence, item_description, etc.