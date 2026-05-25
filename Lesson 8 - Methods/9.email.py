# Create a student email creator that uses first and lat name plus id
# eg. smithjohn123@fake.school.nz

# Get input (first, last, id) and save in variables

"""firstName = input("What is your first name?\n").strip().lower()
lastName = input("What is your last name?\n").strip().lower()
userId = ""

while type(userId) == str:
    userId = input("What is your id?\n").strip().lower()
    try:
        userId = int(userId)
    except:
        print("Please input a number")
        userId = ""


# Strip input to remove accidental spaces and turn names into lowercase (resave in variables)




# Output the final email address
print(f"{firstName}{lastName}{userId}@fake.school.nz")

# --------------------------------

# EXTENSION
# Create a temporary password to output as well
# It should be their names in all uppercase and their id divided by 10
password = input("Enter your password\n")
if password == f"{firstName.upper()}{lastName.upper()}{(int(userId) / 10).__ceil__()}":
    print("Access granted")
else:
    print("That is not your password")
"""
# --------------------------------

# EXPERT
# Create a WSCW email creator
# Get the users first and last name, then randomly generate an ID number (8 digits long)
# Output the email addess (lastf.wsc.school.nz) 
# - you'll need to strip down the first name to just first letter
# Output their id number
# Output a temporary password (all uppercase). You can choose how you create this, 
# but it needs to be unique for each user

import datetime, random

lastChar = input("What is your first name?\n").strip().lower()[0]
lastName = input("What is your last name?\n").strip().lower()
classCode = input("What is your whanau class code?\n").strip().lower()
startDate = str(datetime.date.today().year)[2] + str(datetime.date.today().year)[3]
idNumber = random.randint(100, 999)

email = f"{lastName}{lastChar}@wsc.school.nz"
password = f"{classCode}{startDate}{idNumber}"

print(email)
print(f"Your ID is {idNumber}")
while True:
    if input("What is your password?\n") == password:
        print("Access granted!")
    else:
        print("Wrong password")