#   collection = single "variable" used to store multiple values
#   list = [] ordered and changeable. Duplicates are okay
#   Set = {} unordered and immutable, but add/remove ok. NO DUPLICATES
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER



#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER
fruits = ("apple", "banana", "orange", "coconut", "coconut")

#prints all methods you can use with fruits tuple
#print(dir(fruits))
#explains the methods in more detail
#print(help(fruits))
#============================================================================================

#list.index("object") to find the index of a specific element use
#list.count("object") find the amount of an object that is found in a list
#len(list) returns the amount of elements in the list
#use the "in" operator to find if a value is in the list, this returns true or false
                        #print("apple" in fruits)

fruits.index("apple")
print(fruits.count("coconut"))