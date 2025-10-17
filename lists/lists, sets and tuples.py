#   collection = single "variable" used to store multiple values
#   list = [] ordered and changeable. Duplicates are okay
#   Set = {} unordered and immutable, but add/remove ok. NO DUPLICATES
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

#this is a list
fruits = ["apple", "banana", "orange", "peach"]

#prints all methods you can use with fruits list
#print(dir(fruits))
#explains the methods in more detail
#print(help(fruits))

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

#shows everything you can do with this list, basically a help function
print(dir(fruits))

#-----------------------------------------------------------------------------
#prints the amount of elements in the list
print(len(fruits))

#use the "in" operator to find if a value is in the list, this returns true or false
print("apple" in fruits)

#changes the element of the specified index
fruits[0] = "coconutt"
for fruit in fruits:
    print(fruit)

#-----------------------------------------------------------------------------
#adds an element to the end of the list
fruits.append("MANGO")

# removes an element from the list (ERROR IF THE ELEMENT DOES NOT EXIST)
fruits.remove("banana")

#list.insert(index, object) , this inserts an object into the list at a specific location, does not destroy item at the location
            #instead just moves it over
fruits.insert(0, "crabapple")

print(" NEXT")


#list.sort() sorts a list in alphabetical order
fruits.sort()
print(fruits)

#reverses the order based on what was first listed, can also be reversed
#   if the list was previously modified using sort()
fruits.reverse()
print(fruits)

# to clear all elements out of a list use list.clear()
fruits.clear()
print(fruits)

# to find the index of a specific element use list.index("object")
    #if the object is not in the list it returns error
fruits.index("crabapple")

#find the amount of an object that is found in a list
    #list.count("object")

fruits.count("crabapple")
#              since there is only one crabapple the output will be 1
#                       if it doesn't exist it will return 0



