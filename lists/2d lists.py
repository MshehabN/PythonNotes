# a 2d list is a list, made up of lists
# good if you need a matrix of data, like an Excel spreadsheet

#to visualize it, each individual list, represents a row
#       and each element represents a column

#   1-dimensional lists
fruits =     ["apple", "orange", "banana", "coconut"]
vegetables = ["carrot", "lettuce", "tomato" ]
meat =       ["beef", "chicken", "fish"]

#   2-dimensional list

groceries = [fruits, vegetables, meat]

#print everything in the list
#       for x in groceries:
#                print(x)

# the lists become the elements
# here we are printing the index of 0 which is the fruits list, to print other lists, think of them as indexes
print(groceries[0])
print(groceries[1])
print(groceries[2])

# to find a specific item within a list, think of it like coordinates
#           to find the apple in the fruits list we do

#print(2dlist[listIndex][index])
print(groceries[0][0]) #find apple
print(groceries[1][2]) # find tomato

print("===============================")

# now we use a nested loop to print everything, where "food" is the new variable for it
for lists in groceries:
    for food in lists:
     print(food, end= "    ")
    print()

# NOT LIMITED TO JUST LISTS
#       Can also create a 2d list with tuples and sets

# can make a tuple, made up of sets
#   or a set, made up of lists,
#       can be created interchangeably

#   groceries =  {["apple", "orange", "banana", "coconut"]
#                  ["carrot", "lettuce", "tomato" ]
#                   ["beef", "chicken", "fish"]}

