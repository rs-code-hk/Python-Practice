# Create a calculator that asks the user for a number (of days)
# and outputs how many seconds in that number of days

# Values - start by writing constants to hold:
# The number of seconds in a minute
SECONDS_PER_MINUTE = 60
# The number of minutes in an hour
MINUTES_PER_HOUR = 60
# The number of hours in a day
HOURS_PER_DAY = 24

# Get input from the user and save it in a variable
days = input("How many days would you like to calculate?\n")
# Change the value into an integer and resave in the variable
try:
    numberDays = int(days)
except:
    print("Please input an actual number")
    numberDays = "NAN"

if numberDays != "NAN":
    print(f"The amount of seconds in {numberDays} days is {numberDays * HOURS_PER_DAY * MINUTES_PER_HOUR * SECONDS_PER_MINUTE}")

# Calculate the number of seconds using * with the input and your constants. 
# Save it in a new variable.

# Output the answer

# ---------------------------------

# EXTENSION
# Also output how many total hours and how many total minutes in the days
# Create another calculator that does the opposite (input is seconds, output is days)

# ---------------------------------

# EXPERT (for those who already know some Python)
# Create the calculator above, but...
#   allow your user to choose the input and output type (seconds, minutes, hours, days)
#   Loop the calculator so they can do it again with having to reopen the program.