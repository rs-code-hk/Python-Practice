def check_play():
    play = input("Do you want to play again")
    if play.lower() in ["y", "yes"]:
        return True
    else:
        return False

print(check_play())
