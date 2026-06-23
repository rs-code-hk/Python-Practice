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

gold = 50
forSale = {
    "Sword": item(10, "A basic longsword"),
    "Sword of Danger Detection": item(5, "Of course it's always glowing, swords are sharp!"),
    "Ring of Fire Detection": item(10, "A fire distinguisher (Range: Touch)"),
    "Gun of Immaculate Accuracy": item(50, "Always hits the closest thing to it"),
    "Hamster of World Devouring": item(1, "The hamster that must destroy the world. PLS BUY THIS. I AM VERY SCARED."),
    "Bag of Holding": item(20, "Unfortunately it's full of air"),
    "none": None
}













#===============================
#===============================
# EXTENSION
# Display extra info for each item (on top of price): attack, defence, item_description, etc.