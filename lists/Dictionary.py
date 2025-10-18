# dictionary = a collection of {key:value} pairs
#                ordered and changeable. no duplicates

#dictionary.get("key") --> gets the associated value of the key
#dictionary.update({"Key" : "Value"}) --> adds to the dictionary(can also change existing values)
#dictionary.pop("key") ---> removes a value
#dictionary.popitem() ---> to remove the latest key value item in the dictionary (no value needed)
#dictionary.clear() ---> clears the dictionary
#dictionary.keys() ---> gets all keys (no value)
#dictionary.values() ---> gets all values (no keys)
#dictionary.items() returns a 2d list of the keys and values as a tuple(see bottom page for example)

#dictionary = {key:value}

capitals ={"USA":"Washington D.C",
           "Canada": "Ottawa",
           "China": "Beijing",
           "Russia": "Moscow"}


#print(dir(capitals)) prints all functions that can be used with this dictionary

print(capitals.get("Canada"))

#how to check if a key is within the dictionary
if capitals.get("Japan"):
    print("found the key")
else:
    print("No such key")

#how to add to the dictionary
capitals.update({"Germany": "Berlin"})

#can change existing values as well
capitals.update({"USA":"Detroit"})

#to remove a value
capitals.pop("China")

#to remove the latest key value item in the dictionary (no value needed)
capitals.popitem()
print(capitals)


print(capitals)

# to get ALL keys in the dictionary, do
capitals.keys()

#can be used in a for loop

for key in capitals.keys():
    print(key)

#can also do this for the values
capitals.values()

for value in capitals.values():
    print(value)
#=============================================================================
#capitals.items() returns a 2d list of the keys and values as a tuple
# it will return something like this:
#
# capitals =[("USA":"Washington D.C"),
#            ("Canada": "Ottawa"),
#            ("China": "Beijing"),
#            ("Russia": "Moscow")]

items = capitals.items()
for key, value in capitals.items():
    print(key, value)