temp = [1, 3, 5, 4, 8, 8, 0, 9, 2]
for x, y in enumerate(temp):
    if temp.__contains__(x):
        temp.pop(temp.index(x))

print(temp)