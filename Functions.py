#function = block of reusable code
                #place () after the function name to invoke it


# to define a function, you use "def"

def happyBirthday():
    print(f"Happy birthday to you!")

#here we are calling the functions 
happyBirthday()


# we can pass in parameters into the function
# here we pass in a name variable to be used

def happyBirthday(name):
    print(f"Happy birthday to you {name}!")

# when we call the function we can assign that variable a value which I used "shehab" for name
happyBirthday("Shehab")

# we can pass in multiple arguments
def happyBirthday(name, age):
    print(f"Happy birthday to you {name}!")
    print(f"you are {age} years old!")

happyBirthday("Shehab", 21)
happyBirthday("Abaan", 20)
happyBirthday("elmo", 40)

# you NEED a matching number of arguments, and they need to be in order


#return = statement used to end a function
                #and send the result back to the call function

def add(x, y):
    z = x +y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1,2 ))
print(divide(1,2 ))
print(subtract(1,2 ))
print(multiply(1,2 ))

def createName(firstName, lastName):
    firstName = firstName.capitalize()
    lastName = lastName.capitalize()
    return firstName +" " + lastName

fullName = createName("moe", "shehab")
print(fullName)