#   collection = single "variable" used to store multiple values
#   list = [] ordered and changeable. Duplicates are okay
#   Set = {} unordered and immutable, but add/remove ok. NO DUPLICATES
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

#this is a list
fruits = ["apple", "banana", "orange", "peach"]

print(fruits)
#-----------------------------------------------------------------------------
#   fruit is basically the x value which is ONE of the items
# and fruits is the LIST
for fruit in fruits:

    #basically for every fruit(iteration) in fruits(list) print fruit(the iteration)
    print(fruit)

#-----------------------------------------------------------------------------
#this is how we access the list with an index
#where 0 is the first element
print(fruits[0])

#we can iterate as well
print(fruits[::-1])