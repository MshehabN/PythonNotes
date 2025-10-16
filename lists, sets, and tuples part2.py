#   collection = single "variable" used to store multiple values
#   list = [] ordered and changeable. Duplicates are okay
#   Set = {} unordered and immutable, but add/remove ok. NO DUPLICATES
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

#list.append() adds an element to the end of the list
#list.remove() removes an element from the list (ERROR IF THE ELEMENT DOES NOT EXIST)
#list.insert(index, object) , this inserts an object into the list at a specific location
#list.sort() sorts a list in alphabetical order
#list.reverse() reverses the order based on what was first listed
#list.clear() to clear all elements out of a list
#list.index("object") to find the index of a specific element use
#list.count("object") find the amount of an object that is found in a list

#len(list) returns the amount of elements in the list

#use the "in" operator to find if a value is in the list, this returns true or false
                        #print("apple" in fruits)

#list[index] this is how we access the list with an index
#list[index] = "object "changes the element of the specified index

#==============================================================================#
#list.add("object") we use this instead of #list.append() for sets
#list.remove still works
#list.pop() will remove whichever element is first, (removes a random element)


#   Set = {} unordered and immutable, but add/remove ok. NO DUPLICATES

fruits = {"apple", "banana", "orange", "coconut"}

#prints all methods you can use with fruits set
#print(dir(fruits))
#explains the methods in more detail
#print(help(fruits))

print(fruits)

#print(fruits[0]) will NOT work because sets are unordered, therefore there is no indexes

#we CAN however, add and remove different elements.
# but instead we use list.add("object")
fruits.add("mango")
print(fruits)

#list.remove still works
fruits.remove("banana")
print(fruits)

#list.pop() will remove whichever element is first,
#       however since the list is unordered, it will remove a random element
fruits.pop()
print(fruits)

#list.clear() still works
fruits.clear()
#=========================================================================
