# *args  = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#               * unpacking operator
#               1. positional, 2. default, 3. keyword, 4. ARBITRARY

#when passing in *args, it turns the values that are placed into the call into a TUPLE
def add(*args):
    #here we initialize a total variable set to 0
    total = 0
    #for every "arg" in the tuple "args", since the call values are now a tuple
    for arg in args:
        #add the number to the total
        total = total +arg
        #return the total
    return total

print(add(1,2,4,5,6))

#REMEMBER *args PARAMETER IS JUST A VARIABLE NAME, WE CAN CALL IT ANYTHING ELSE AS WELL

def displayName(*args):
    for arg in args:
        print(arg, end=" ")
    return

print(displayName("Professor","moe","real one", "shehab"))


#**kwargs
#instead of a tuple, it becomes a DICTIONARY
def printAddress(**kwargs):
    for key, value in kwargs.items(): #THIS IS A DICTIONARY FUNCTION
        print(f"{key}, {value}")

printAddress(street= "bank", city ="ottawa", province= "Ontario", zip ="")

print("========================================================================")
#here we are using both args and kwargs
def shippingLabel(*args, **kwargs):
    for arg in args:
        print(arg, end = " ")
    print()
    for value in kwargs.values():
        print(value, end= " ")

#make sure that the args, precede the kwargs
shippingLabel("Dr", "spongebob", "squarepants", "III",
                street="Bank street",
                houseNum = "204",
                city = "ottawa")
