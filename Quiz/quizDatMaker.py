import pickle

class gameRound():
    def __init__(self, inQuestion, inAnswers, inInterim, inAsciiArt, inImportPlayerDat):
        # Ran when creating question
        self.question = inQuestion
        self.answers = inAnswers
        self.interim = inInterim
        self.asciiArt = inAsciiArt
        self.playerDat = inImportPlayerDat
        self.pluralPronouns = self.playerDat()["pluralPronouns"]

    def askQuestion(self):
        # Run when asking question
        # Get player data
        playerDat = self.playerDat()

        # Print ascii art
        for i in self.asciiArt:
            print(i)

        # Get player response
        answer = input(self.question.format(playerDat["pronouns"][0], playerDat["pronouns"][1], playerDat["pronouns"][2], playerDat["pronouns"][3], playerDat["name"])).upper().strip().replace("/", "").replace("\\", "")

        # Print result
        if answer in self.answers:
            # Answer correct
            playerDat["points"] += 1
            print(self.interim[0].format(playerDat["pronouns"][0], playerDat["pronouns"][1], playerDat["pronouns"][2], playerDat["pronouns"][3], playerDat["name"]))
        else:
            # Answer incorrect
            print(self.interim[1].format(playerDat["pronouns"][0], playerDat["pronouns"][1], playerDat["pronouns"][2], playerDat["pronouns"][3], playerDat["name"]))

        input(f"{playerDat['name']} has now scored {playerDat["points"]} points! {playerDat["pronouns"][0].capitalize()} {self.pluralGrammar("is", "are")} well on {playerDat["pronouns"][1]} way to completing the quiz. \nHit enter/return to continue.\n")

        return playerDat

    def pluralGrammar(self, nonPlural, plural):
        if self.pluralPronouns:
            # If pronouns are plural
            return plural
        else:
            # If pronouns aren't plural
            return nonPlural
