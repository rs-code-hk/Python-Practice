# Represent 
# 111
# 222
# 333
# as 111222333

import random

def checkSet(set):
    if "".join(set) in ["123", "321", "111", "222", "333"]:
        return 1
    return 0

def checkGrid(grid):
    # Check Rows
    gridValid = 0
    gridValid += checkSet([grid[0], grid[1], grid[2]])
    gridValid += checkSet([grid[3], grid[4], grid[5]])
    gridValid += checkSet([grid[6], grid[7], grid[8]])
    # Check Columns
    gridValid += checkSet([grid[0], grid[3], grid[6]])
    gridValid += checkSet([grid[1], grid[4], grid[7]])
    gridValid += checkSet([grid[2], grid[5], grid[8]])
    # Check Diagonals
    gridValid += checkSet([grid[0], grid[4], grid[8]])
    gridValid += checkSet([grid[6], grid[4], grid[2]])

    return gridValid == 0

def printGrid(grid):
    retGrid = ""
    retGrid += " _ _ _ \n"
    retGrid += f"|{grid[0]}|{grid[1]}|{grid[2]}|\n"
    retGrid += f"|{grid[3]}|{grid[4]}|{grid[5]}|\n"
    retGrid += f"|{grid[6]}|{grid[7]}|{grid[8]}|\n"
    retGrid += " _ _ _ \n"

    return retGrid

# List of all possible numbers
numList = []

# List of all sets of 3
setNums = []

# List of all valid numbers
validNums = []

for num1 in range(1, 4):
    for num2 in range(1, 4):
        for num3 in range(1, 4):
            for num4 in range(1, 4):
                for num5 in range(1, 4):
                    for num6 in range(1, 4):
                        for num7 in range(1, 4):
                            for num8 in range(1, 4):
                                for num9 in range(1, 4):
                                    i = list(f"{num1}{num2}{num3}{num4}{num5}{num6}{num7}{num8}{num9}")
                                    numList.append(i)

for i in numList:
    x = list(i)
    try:
        for k in ["1", "2", "3"]:
            for j in range(3):
                x.remove(k)
    except:
        continue
    if x == []:
        setNums.append(i)

for i in setNums:
    if checkGrid(i):
        validNums.append(i)


print(f"The length of grids is {len(validNums)}")
dumpString = ""
for i in validNums:
    dumpString += printGrid(i)

with open("dump.txt", "w") as f:
    f.write(dumpString)

print("Done!")