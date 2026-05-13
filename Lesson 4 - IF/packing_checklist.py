### Create a packing checklist based on input

# Tell the user what this program is about

# Ask the user for the current temperature and save it

# Change the temperature input into an integer

# If the temperature is below 15, tell them to pack a jacket

# If the temperature is above 15, tell them to pack sunscreen

# Ask the user their destination (beach or mountains)

# If beach, tell them to pack a towel

# If mountains, tell them to pack hiking boots

# ___________________________

# EXTENSION

# Add some more conditions (eg. one day or overnight? solo or with others?)

# ____________________________

# EXPERT (for those who already know Python)

# Create a packing checklist (start with something similar to the main program) then 
# display all items to pack with a X or O for packed or not. 
# Allow the user to select an item to change its status.


# Define pack list
packList = []

# Introduce program
print("Welcome to your packing list. This program will create a packing list for you!")

# Temp
if int(input("What is your current temperature?\n")) >= 15:
    packList.append("Sunscreen")
    print("Remember to pack sunscreen!")
else:
    packList.append("Jacket")
    print("Remember to pack a Jacket")

# Destination
dest = input("Where are you going?\n")

match dest.upper():
    case "BEACH":
        packList.append("Towel")
        print("Remember to pack a towl")
    case "MOUNTAIN" | "MOUNTAINS":
        packList.append("Hiking boots")
        print("Remember to pack hiking boots")
    case _:
        packList.append("Snacks")
        print("Remember to pack snacks")

# Travel Time
time = input("Are you going during the night or the day?\n")

match time.upper():
    case "DAY":
        packList.append("Sunglasses")
        print("Remember to pack sunglasses")
    case "NIGHT":
        packList.append("Remember to pack a sleeping bag")
        print("Remember to pack a sleeping bag")

# Amount of people
people = int(input("How many people are coming along?\n"))

# Get list to display
displayList = []

# Load the displayed items
for i in packList:
    for j in range(people):
        displayList.append([f"Person {j}'s {i}", False])

# Packing loop
while [any, False] not in displayList:
    # Print all items
    for i in displayList:
        if i[1] == False:
            print(f"O - {i[0]}")
        else:
            print(f"X - {i[0]}")

    packedItem = input("What item have you packed?\n")
    for i in displayList:
        if i == [packedItem, False]:
            i = [packedItem, True]
