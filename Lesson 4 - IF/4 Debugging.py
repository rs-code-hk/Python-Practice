print("--- Daily Step Tracker ---")
# Get amount of steps
steps = input("How many steps did you walk today? ")
# Convert to int
try:
    steps = int(steps)
except:
    print("That isn't a number")
else:
    # If more than 10k steps
    if steps >= 10000:
        print("Amazing! You walked over 10,000 steps! You are a Pro Athlete.")
    # If more than 5k steps
    elif steps >= 5000:
        print("Good start, but try to walk a bit more tomorrow!")
    # If any other number of steps
    else:
        print("Did you even walk today???")

    # Set daily step goal
    DAILY_GOAL = 5000
    if steps == DAILY_GOAL:
        # If exactly on goal
        print("Bullseye! You hit your target exactly!")
    if steps == 0: 
        # If 0 steps
        print("You have 0 steps. Did you forget your phone today?")

print("Tracker closing")