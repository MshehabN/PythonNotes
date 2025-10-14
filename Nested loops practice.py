# program to prompt the user to print a rectangle

rows = int(input("how many rows do you want it to have: "))
columns = int(input("how many columns do you want it to have? "))

#for x in range(rows):  this counts every number of rows that was input by the user
#this statement takes the number that was inputted by the user and loops it the given number of times
#       this is good for rows because when the loop makes a new line each time, that will be another row
#               so it will print 7 rows for example if the user inputs 7
for x in range(rows):
    #this print statement makes a new row so we can goto the next line
    print(" ")


    #for y in range(1, columns + 1):
    #this counts from 1 to the input column number + 1 because the last number doesn't count so it works out
    #       logically,
    #
    # and it continuously loops the print statement for the amount of columns there are
    #so if the column input was 5, it would run 5 times in total.
    #   and then after it's done running 5 times it would go back to the row loop and start over again for another row
    #       so the "column" is basically how many times the symbol gets printed and that starts a new column

    for y in range(1, columns + 1):

    #the chosen symbol to show off the rectangle is "X" and i used ,end = "   " to make the rectangle more obvious
        print("X", end="     " )
print("")
print(f"your rectangle has {rows} rows, and {columns} columns!")


#full code
rows = int(input("how many rows do you want it to have: "))
columns = int(input("how many columns do you want it to have? "))
for x in range(rows):
    print(" ")
    for y in range(1, columns + 1):
        print("X" , end="     " )
print("")
print(f"your rectangle has {rows} rows, and {columns} columns!")