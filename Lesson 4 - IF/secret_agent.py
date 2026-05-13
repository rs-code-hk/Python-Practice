### Secret Agent Login
# Create a login process for a secret agent
print("Hello agent, please enter your username")
# Ask for the user's name and save it in a variable
username = input("Enter your username\n")
# Ask for the password and save it in a variable
if username in ["definitelynotaspy", "trustworthy", "idontexist"]:
    password = input("Enter your password\n")
    # Check if the password == 'Falcon'
    if password == "Falcon":
        print(f"Access has been granted, welcome {username}")
        # Ouput that access has been granted and welcome user using their name

        # Ask for the user's age and save it in a variable
        age = input("Enter your age\n")
        # Change the age into an integer
        try:
            age = int(age)
        except:
            # Check inputted age is int, and kick out user if not
            print("You are obviously not smart enough to be a spy")
        else:
            match age:
                case _ if age < 13:
                    print("You are a spy in training")
                
                case _ if age > 12 and age < 18:
                    print("You are a junior spy")
                
                case _:
                    print("You are a field agent")

            print(f"Goodbye {username}")

    else:
        print("Incorrect password")
    # If the user's age is under 13, tell them they are a spy in training

    # If their age is under 18, tell them they are a junior spy

    # If their age is 18 or over, tell them they are a Field Agent
else:
    print("Username not recognised")

# Output a goodbye

# ___________________________

# EXTENSION

# Ask more questions to give your spy more information
# Look up how to use 'and' and 'or' to force more conditions (eg. they must be one of 3 users AND get the password correct)

# ___________________________

# EXPERT (For those who already know python)

# Create a SPY ID GENERATOR
# Your user must login using the correct password to access the generator
# Use a bunch of questions to generate an id. Eg. If their name has 4 or fewer letters, their ID is a random fruit plus other logic...