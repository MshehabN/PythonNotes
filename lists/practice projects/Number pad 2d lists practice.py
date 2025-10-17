# will output a numberpad

numpad = [(1, 2, 3),
          (4, 5, 6),
          (7, 8, 9),
          ('*', 0, '#')]

# for every row(that's what im calling the lists)
#   the second line, iterates every character in the list

#print character, and the end= "  " adds a little space between*

#and the last print statement prints a blank line every time a "row" or list in completely printed
for row in numpad:
    for character in row:
        print(character, end= "  ")
    print()


#so it iterates once for every row in the numpad 2d list which means it will iterate 4 times

#and within each iteration there is a nested loop which prints every character in the row
        # the last 2 print statements are only for format