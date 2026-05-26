# Create a roller coaster access screener (determine if the user is allowed to ride)
# Rules:    They must be over 150cm and over 10 years old
#           They must not have a heart condition
#           OR they can ride if they have a VIP pass

# Get input





# Check conditions and output verdict




# ------------------------------
# EXTENSION
# Change your screener to work for 3 different rides (ask user which ride at the beginning) with different rules

# ------------------------------
# EXPERT
# Follow the same task (with extension), but use dictionaries to make the code more efficient
class ride():
    minHeight = 0
    minAge = 0

    def __init__(self, inMinHeight, inMinAge):
        self.minHeight = inMinHeight
        self.minAge = inMinAge

    def checkRiderValid(self, rider):
        if (rider[0] >= self.minHeight and rider[1] >= self.minAge) or rider[2] == True:
            return True
        
        return False
    
rides = {
    "rollercoaster": ride(150, 10),
    "the big drop": ride(168, 15),
    "the child missile": ride(168, 15),
    "el diablo": ride(178, 18),
    "this was built by someone in rollercoaster tycoon": ride(420, 69)
}

name = input("What is your name?\n").strip().lower().capitalize()
vipPass = ""
while type(vipPass) == str:
    vipPass = input("Do you have a VIP pass?\n").upper().strip()
    match vipPass:
        case "TRUE" | "YES":
            vipPass = True
        case "FALSE" | "NO":
            vipPass = False
        case _:
            vipPass = ""

age = ""
height = ""

if vipPass == False:
    while type(age) == str:
        try:
            age = int(input("How old are you?\n").strip())
        except:
            if age == "":
                raise KeyboardInterrupt

            print("Please input a number")
            age = ""


    while type(height) == str:
        try:
            height = int(input("How tall are you? (cm)\n").strip().replace("cm", ""))
        except:
            if height == "":
                raise KeyboardInterrupt

            print("Please input a number")
            height = ""

while True:
    print(f"What ride would you like to go on {name}?")
    for i in rides.keys():
        print(i.capitalize())

    targetRide = input().lower().strip()

    try:
        if rides[targetRide].checkRiderValid([height, age, vipPass]) == True:
            print(f"You can go on the ride {name}")
        else:
            print(f"You cannot go on the ride")
    except:
        print("That ride doesn't exist")