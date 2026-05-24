# Functions to change questions based on pronouns
def pluralGrammar(nonPlural, plural):
    if pluralPronouns:
        # If pronouns are plural
        return plural
    else:
        # If pronouns aren't plural
        return nonPlural

# Introduction
print("Welcome to the 'Ultimate Quiz'! This will ask about random stuff from any topic!")

# Getting player information and setting up other data
points = 0 # How many questiosn has the player answered correctly
name = input("What your name?\n").capitalize()
pronouns = []
pluralPronouns = False

# Getting pronouns
print("The next section is about pronouns. Roll on pronouns currently aren't supported, sorry!")
validPronouns = False
while validPronouns == False:
    pronouns = input("What are your preferred pronouns? (Yes I am going overboard).\nUse all 4 (e.g. He/Him/His/Himself)\n").lower().replace(" ", "").split("/")
    if pronouns.__len__() == 4:
        validPronouns = True
    else:
        print("Please input exactly 4 pronouns")

if input("Are your pronouns plural? ('_ are' instead of '_ is'). Any answer except for yes will be assumed to be a no.\n").upper() == "YES":
    pluralPronouns = True

# Finish introduction
print("Alright, let the show begin!")
print("------------------------------")
print(f"This is {name} and {pronouns[0]} {pluralGrammar("is", "are")} about to take on the 'Ultimate Quiz!'")

# Load questions and interims
# Round class
class gameRound():
    question = ""
    answers = []
    # If win, print interim[0], else interim[1]
    interim = []
    asciiArt = []

    def __init__(self, inQuestion, inAnswers, inInterim, inAsciiArt):
        self.question = inQuestion
        self.answers = inAnswers
        self.interim = inInterim
        self.asciiArt = inAsciiArt

    def askQuestion(self):
        # Run when asking question
        global points
        for i in self.asciiArt:
            print(i)

        answer = input(self.question).upper()
        if answer in self.answers:
            points += 1
            print(self.interim[0])
        else:
            print(self.interim[1])

        input(f"{name} has now scored {points} points! {pronouns[0].capitalize()} {pluralGrammar("is", "are")} well on {pronouns[1]} way to completing the quiz. Hit enter/return to continue.\n")

# Create Ascii art printed before every round
ASCII_ART = [
    ["       _", "     _|=|__________", "    /              \\", "   /                \\", "  /__________________\\", "   ||  || /--\ ||  ||", "   ||[]|| | .| ||[]||", " ()||__||_|__|_||__||()", "( )|-|-|-|====|-|-|-|( ) ", "^^^^^^^^^^====^^^^^^^^^^^"],
    ["  _", " (_)", "<___>", " | |______", " | |* * * )", " | | * * (_________", " | |* * * |* *|####)", " | | * * *| * |   (________________", " | |* * * |* *|####|##############|", " | | * * *| * |    |              |", " | |* * * |* *|####|##############|", " | |~~~~~~| * |    |              |", " | |######|* *|####|##############|", " | |      |~~~'    |              |", " | |######|########|##############|", " | |      |        |              |", " | |######|########|##############|", " | |~~~~~~|        |              |", " | |      |########|##############|", " | |      '~~~~~~~~|              |", " | |               |##########JGS#|", " | |               '~~~~~~~~~~~~~~~", " | |", " | |", " | |"],
    ["              |))    |))", " .             |  )) /   ))", " \\\\   ^ ^      |    /      ))", "  \\\\(((  )))   |   /        ))", "   / G    )))  |  /        ))", "  |o  _)   ))) | /       )))", "   --' |     ))`/      )))", "    ___|              )))", "   / __\             ))))`()))", "  /\@   /             `(())))", "  \/   /  /`_______/\   \  ))))", "       | |          \ \  |  )))", "       | |           | | |   )))", "       |_@           |_|_@    ))", "      /_/           /_/_/"],
    ["temp"],
    ["temp"],
    ["temp"]
]

# Make list of every round
ROUNDS = [
    gameRound(f"Now, {name}, your first question. What is the tallest building in the world?\n", ["BURJ KHALIFA", "THE BURJ KHALIFA", "DEBUG"], [f"That answer is correct! {name} has earned {pronouns[3]} another point!", f"Sorry {name}, that is incorrect. The correct answer is 'The Burj Khalifa'."], ASCII_ART[0]),
    gameRound(f"{name}, prepare for your second question. In North Carolina, what game is it illegal to play for six hours?\n", ["BINGO"], [f"That is correct. What a wierd law huh. Do you have any experience with it {name}?", f"That is incorrect, the answer is bingo. Honestly the real question is who is playing bingo for six hours straight."], ASCII_ART[1]),
    gameRound(f"The third question! In greek mythology, who was described as having 'A face that launched a thousand ships?'\n", ["HELEN", "HELEN OF TROY"], ["That is correct! You know your myths huh!", f"Nope! It was Helen of Troy. Everyone boo {pronouns[1]} for not knowing about greek mythology, BOOO!"], ASCII_ART[2]),
    gameRound(f"Let's see how {name} does at a science question! Humans have 1 pair of sex chromosones. How many do platypus have?\n", ["FIVE", "5"], ["Good job! That is the correct answer.", f"No, that is incorrect. The correct answer is 5. Better luck next time {name}"], ASCII_ART[3]),
    gameRound(f"Here's your fifth question, good luck {name}! X raised to the power of X equals 4 raised to the power of 1024. What is X?\n", ["256", "TWO HUNDRED AND FIFTY SIX"], [f"Correct! Fun fact, this question is on the SAT in America. Did you have to take the SAT {name}?", "No, the correct answer is 256! Sorry, the math was probably to hard. On with the quiz."], ASCII_ART[4]),
    gameRound(f"Final question! Can {name} add one final point to {pronouns[1]} total! What programming language was Tetris originally made in?\n", ["C"], ["Correct! An amazing ending to the run. Let's see how well you did.", "Incorrect, the correct answer is C. That is an unfortunate end. Let's see how the run went."], ASCII_ART[5])
]

# Run questions
for x in ROUNDS:
    x.askQuestion()

# Conclusion
print(f"{name}, out of {len(ROUNDS)} questions, you answered {points} correctly! That's a {points / len(ROUNDS) * 100}% success rate!")
print(f"Thank you for playing. Everyone in the crowd, give it up for {name}.")