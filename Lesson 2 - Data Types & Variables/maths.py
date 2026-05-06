import math
# Print the answers to the following questions. Get the computer to do the math for you!

# What is 376 + 209 + 44439?
print(f"376 + 209 + 44439 = {376 + 209 + 44439}")

# What is 2345678 - 678 - 1?
print(f"2345678 - 678 - 1 = {2345678 - 678 - 1}")

# What is 345 divided by 34?
print(f"345 / 34 = {345 / 34}")

# What is 567 * 34 * 3?
print(f"567 * 34 * 3 = {567 * 34 * 3}")

# Print 'hello' 32 times.
print("Hello" * 32)

# -------------------------

# EXTENSION

# What is 2345 / 766 rounded to the nearest whole number?
print(f"2345 / 766 to the nearest whole number = {2345 // 76}")

# What is 456 to the power of 23?
print(f"456 raised to the power of 23 = {456**23}")

# What is the remainder if you divide 345 by 32?
print(f"The remainder of 345 / 23 is {345%32}")

# --------------------------

# EXPERT (for those who already know some Python)
# Create a simple calculator
# GOAL: The user chooses Add, Subtract, Multiply or Divide, then inputs 2 numbers
#       The computer will output the result.
# (Optional) Make sure the user can only input numbers

while True:
    validEquation = True
    numbers = []
    print("Input a number, operator, then another number")
    print("sin, cos, and tan work, the first number will either multiply or divide the second, which is the one being operated on.")
    inputEquation = input()
    equationElements = inputEquation.split(" ")

    if len(equationElements) != 3:
        print("Please input exactly 3 elements, a number, then operator, then another number.")
        validEquation = False
    
    if validEquation:
        try:
            numbers.append(int(equationElements[0]))
        except:
            print("The first element isn't a number")
            validEquation = False

    if validEquation:
        try:
            numbers.append(int(equationElements[2]))
        except:
            print("The second element isn't a number")
            validEquation = False
    
    if validEquation:
        match equationElements[1]:
            case "+":
                print(numbers[0] + numbers[1])
            case "-":
                print(numbers[0] - numbers[1])
            case "*":
                print(numbers[0] * numbers[1])
            case "/":
                print(numbers[0] / numbers[1])
            case "//":
                print(numbers[0] // numbers[1])
            case "**":
                print(numbers[0] ** numbers[1])
            case "root":
                print(numbers[0] ** (1.0 / numbers[1]))
            case "sin*":
                print(numbers[0] * math.sin(numbers[1]))
            case "sin/":
                print(numbers[0] / math.sin(numbers[1]))
            case "cos*":
                print(numbers[0] * math.cos(numbers[1]))
            case "cos/":
                print(numbers[0] / math.cos(numbers[1]))
            case "tan*":
                print(numbers[0] * math.tan(numbers[1]))
            case "tan/":
                print(numbers[0] / math.tan(numbers[1]))
            case _:
                print("The inputted operator isn't valid")

    input("Enter/Return\n")