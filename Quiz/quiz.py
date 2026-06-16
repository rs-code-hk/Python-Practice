import yaml
import pickle
import os
from quizDatMaker import *

os.system("cls")

def sortBoard(e):
    return e["SCORE"]

leaderboard = []
with open("leaderboard.yaml") as f:
    leaderboard = yaml.safe_load(f)["leaderboard"]

# Check if leaderboard is none, set to list
if leaderboard is None:
    leaderboard = []

# Sort leaderboard
leaderboard.sort(key = sortBoard, reverse = True)

# Functions to change questions based on pronouns
def pluralGrammar(nonPlural, plural):
    if playerDat["pluralPronouns"]:
        # If pronouns are plural
        return plural
    else:
        # If pronouns aren't plural
        return nonPlural

# Introduction
print("Welcome to the 'Ultimate Quiz'! This will ask about random stuff from any topic!")

# Getting player information and setting up other data
playerDat = {
    "points": 0, # Number of correct questions
    "name": input("What your name?\n").capitalize().strip(), # Player's name
    "pronouns": [], # Player's pronouns
    "pluralPronouns": False # Are player's pronouns plural
}

# Getting pronouns
print("The next section is about pronouns. Roll on pronouns currently aren't supported, sorry!")
validPronouns = False
while validPronouns == False:
    playerDat["pronouns"] = input("What are your preferred pronouns? (Yes I am going overboard).\nUse all 4 (e.g. He/Him/His/Himself)\n").lower().replace(" ", "").split("/")
    if playerDat["pronouns"].__len__() == 4:
        validPronouns = True
    else:
        print("Please input exactly 4 pronouns")

if input("Are your pronouns plural? ('_ are' instead of '_ is'). Any answer except for yes will be assumed to be a no.\n").upper().strip() == "YES":
    playerDat["pluralPronouns"] = True

# Finish introduction
print("Alright, let the show begin!")
print("------------------------------")
print(f"This is {playerDat["name"]} and {playerDat["pronouns"][0]} {pluralGrammar("is", "are")} about to take on the 'Ultimate Quiz!'")

def sendPlayerDat():
    return playerDat

# Create Ascii art printed before every round
ASCII_ART = [
    ["       _", "     _|=|__________", "    /              \\", "   /                \\", "  /__________________\\", "   ||  || /--\ ||  ||", "   ||[]|| | .| ||[]||", " ()||__||_|__|_||__||()", "( )|-|-|-|====|-|-|-|( ) ", "^^^^^^^^^^====^^^^^^^^^^^"],
    ["  _", " (_)", "<___>", " | |______", " | |* * * )", " | | * * (_________", " | |* * * |* *|####)", " | | * * *| * |   (________________", " | |* * * |* *|####|##############|", " | | * * *| * |    |              |", " | |* * * |* *|####|##############|", " | |~~~~~~| * |    |              |", " | |######|* *|####|##############|", " | |      |~~~'    |              |", " | |######|########|##############|", " | |      |        |              |", " | |######|########|##############|", " | |~~~~~~|        |              |", " | |      |########|##############|", " | |      '~~~~~~~~|              |", " | |               |##########JGS#|", " | |               '~~~~~~~~~~~~~~~", " | |", " | |", " | |"],
    ["               |))    |))", " .             |  )) /   ))", " \\\\   ^ ^      |    /      ))", "  \\\\(((  )))   |   /        ))", "   / G    )))  |  /        ))", "  |o  _)   ))) | /       )))", "   --' |     ))`/      )))", "    ___|              )))", "   / __\             ))))`()))", "  /\@   /             `(())))", "  \/   /  /`_______/\   \  ))))", "       | |          \ \  |  )))", "       | |           | | |   )))", "       |_@           |_|_@    ))", "      /_/           /_/_/"],
    [""],
    [""],
    [""]
]

# Make list of every round
# Numbers to variables list
# 0-3 = pronouns of that number
# 4 = Name
ROUNDS = [
    gameRound("Now, {4}, your first question. What is the tallest building in the world?\n", ["BURJ KHALIFA", "THE BURJ KHALIFA"], ["That answer is correct! {4} has earned {3} another point!", "Sorry {4}, that is incorrect. The correct answer is 'The Burj Khalifa'."], ASCII_ART[0], sendPlayerDat),
    gameRound("{4}, prepare for your second question. In North Carolina, what game is it illegal to play for six hours?\n", ["BINGO"], ["That is correct. What a wierd law huh. Do you have any experience with it {4}?", "That is incorrect, the answer is bingo. Honestly the real question is \nwho is playing bingo for six hours straight."], ASCII_ART[1], sendPlayerDat),
    gameRound("The third question! In greek mythology, who was described as having \n'A face that launched a thousand ships?'\n", ["HELEN", "HELEN OF TROY"], ["That is correct! You know your myths huh!", "Nope! It was Helen of Troy. \nEveryone boo {1} for not knowing about greek mythology, BOOO!"], ASCII_ART[2], sendPlayerDat),
    gameRound("Let's see how {4} does at a science question! Humans have 1 pair of sex chromosones. \nHow many do platypus have?\n", ["FIVE", "5"], ["Good job! That is the correct answer.", "No, that is incorrect. The correct answer is 5. \nBetter luck next time {4}"], ASCII_ART[3], sendPlayerDat),
    gameRound("Here's your fifth question, good luck {4}! \nX raised to the power of X equals 4 raised to the power of 1024. What is X? (x^x = 4^1024)\n", ["256", "TWO HUNDRED AND FIFTY SIX"], ["Correct! Fun fact, this question is on the SAT in America. \nDid you have to take the SAT {4}?", "No, the correct answer is 256! Sorry, the math was probably to hard. \nOn with the quiz."], ASCII_ART[4], sendPlayerDat),
    gameRound("Final question! Can {4} add one final point to {1} total! \nWhat programming language was Tetris originally made in?\n", ["C"], ["Correct! An amazing ending to the run. Let's see how well you did.", "Incorrect, the correct answer is C. That is an unfortunate end. \nLet's see how the run went."], ASCII_ART[5], sendPlayerDat)
]

# Run questions
for x in ROUNDS:
    # Ask question
    print("")
    print(f"Question {[i for i, j in enumerate(ROUNDS) if j == x][0] + 1}")
    print("--------------------")
    playerDat = x.askQuestion()

# Conclusion
print(f"{playerDat["name"]}, out of {len(ROUNDS)} questions, you answered {playerDat["points"]} correctly! That's a {playerDat["points"] / len(ROUNDS) * 100}% success rate!")
print(f"Thank you for playing. Everyone in the crowd, give it up for {playerDat["name"]}.")

# Print leaderboard
if len(leaderboard) == 0:
    print("Nobody is on the leaderboards")
else:
    print("Leaderboard \n--------------------")
    for i in leaderboard:
        print(f"{i["PLAYER"]} - {i["SCORE"]} points")

# Ask if player wants to be on leaderboards
onBoards = None

while onBoards == None:
    match input("Would you like to be on the leaderboards?\n").strip().upper():
        case "YES" | "TRUE":
            onBoards = True

        case "NO" | "FALSE":
            onBoards = False
    
    if onBoards is None:
        print("Please respond yes or no")

# If they want to be, add player to leaderboards
if onBoards:
    leaderboard.append({"PLAYER": playerDat["name"], "SCORE": playerDat["points"]})

    # Resort and reprint boards
    leaderboard.sort(key = sortBoard, reverse = True)
    print("New leaderboard \n--------------------")
    for i in leaderboard:
        print(f"{i["PLAYER"]} - {i["SCORE"]} {"point" if i["SCORE"] == 1 else "points"}")

    # Save boards
    dumpBoards = {"leaderboard": leaderboard}
    with open("leaderboard.yaml", "w") as f:
        yaml.dump(dumpBoards, f, indent=4)