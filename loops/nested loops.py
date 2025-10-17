#nested loops = a loop within another loop (outer, inner)
#                                    outer loop:
#                                       inner loop:


for x in range(3):
    for y in range(1, 10):
        # , end="" makes all the characters on the same line
        print(y, end="")
    print(" ")

