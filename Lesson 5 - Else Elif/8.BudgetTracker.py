### Budget Tracker ###
# Create a budget tracker that gives financial recommendation around an item

# Get user variables
BUDGET = 1000.0
SAVINGS = 0.5
ExpInc = BUDGET * (1 - SAVINGS)
# Create a constant to hold your savings (percentage) goal

# Ask user for item name and save in variable
# Ask user for cost and save in variable
# Change the cost into an integer

while True:
    # Get item details, and print amount of money left
    print(f"You have {ExpInc}$ left")
    itemName = input("What item are you trying to buy?\n")
    itemPrice = input("What is the price of this item?\n").replace("$", "").replace(" ", "")

    try:
        # Change price to number
        itemPrice = int(itemPrice)
    except:
        # If inputted price isn't a number
        print("Price is not a number")
    else:
        costPercent = itemPrice / ExpInc
        match costPercent:
            case 0:
                print("It's free, get it!")
            case _ if costPercent > 0 & costPercent < 0.1:
                print("It's a small treat, get it")
                ExpInc -= itemPrice
            case _ if costPercent >= 0.1 & costPercent < 0.5:
                print("You should sleep on it.")
                print("One sleep later")
                if input("Do you still want to buy it?\n").upper() == "YES":
                    ExpInc -= itemPrice
                    print("I hope you enjoy it")
                else:
                    print("You made a good choice")
            case _ if costPercent > 1:
                print("You don't have enough money")
            case _:
                print("You shouldn't buy that")

# Calculate the percentage of budget (cost / budget) * 100
# Tell your user the percentage of your budget

# Check if percentage is 0 and say it's free if it is

# Check if the percentage is less then 10 and say it's a small treat so enjoy

# Check if it is less than 50 percent and if it is tell them it's a major spend and should sleep on it

# Check if it's over 100 and if it is tell them they don't have enough money

# Otherwise, tell them it costs way too much and isn't worth it

# _______________________

# EXTENSION
# Include an item type question and change answers based on this. 
# Eg. food shouldn't cost as much as a bill so if it's a food, 
# tell them to not buy it at a lower percentage


# _______________________

# EXPERT
# Try to create a budget tracker that saves data in a file 
# so the remaining_budget can be updated every time the program is used
# You will need to create a save.txt file to go with this (keep it in the same folder)
# If you're not sure how to do this check here: https://www.w3schools.com/python/python_file_write.asp 