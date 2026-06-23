# Represent 
# 111
# 222
# 333
# as 111222333
validNums = []

for num1 in range(3):
    for num2 in range(3):
        for num3 in range(3):
            for num4 in range(3):
                for num5 in range(3):
                    for num6 in range(3):
                        for num7 in range(3):
                            for num8 in range(3):
                                for num9 in range(3):
                                    i = int(f"{num1}{num2}{num3}{num4}{num5}{num6}{num7}{num8}{num9}")
                                    validNums.append(i)

print("Done!")