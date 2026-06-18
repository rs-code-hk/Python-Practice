hero_data = {
    "Player1": {
        "class": "Warrior", 
        "health": 100, 
        "gear": ["shield", "sword"]
    },
    "Player2": {
        "class": "Mage", 
        "health": 65, 
        "gear": ["staff"]
    }
}
print("Current Players:")
for i in range(len(hero_data)):
    print(f"Player {i+1}")
    if hero_data["Player1"]["class"] == "Warrior":
        print("Player 1 is a frontline fighter.")
    starting_weapon = hero_data["Player1"]["gear"]["0"]
    print(f"Starting weapon for Player 1: {starting_weapon}")
    hero_data["Player2"]["health"] = 75
    print(f"Updated Player 2 Data: {hero_data["Player2"]}")
# IF the string "staff" is IN the list stored at hero_data "Player2" "gear"
# THEN print "Mage is fully equipped"