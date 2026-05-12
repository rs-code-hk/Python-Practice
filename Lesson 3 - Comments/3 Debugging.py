import sys

# Define constants
STEPS_IN_KM = 1312
GOAL = 5.0

# Get user data
user_name = input("Enter athlete name: ")  
steps = input("How many steps did you walk? ")

# Try to cast steps to int
try:
    km_walked = float(steps) / STEPS_IN_KM
except:
    print("Please input an actual number")
    sys.exit()
    
km_rounded = round(km_walked, 2) 
print(user_name + " walked " + str(km_rounded) + " km.")
goal_reached = km_rounded >= GOAL
print("Daily 5km Goal Met:")
print(km_rounded)