#will execute code WHILE some condition remains true

name  = input("enter your name: ")

while name == "":
    print("you did not enter your name")
    name = input("enter your name: ")
print(f"hello {name}")

age = int(input("how old are you: "))

while age < 0:
    print("age cant be negative")
    age = int(input("how old are you: "))

print(f"you are {age} years old")

#how to escape
food = input("enter a food you like (q to quit)")

while not food == "q":
    print(f"you like {food}")
    food = input("enter another food you like (q to quit)")

print("bye")

num = int(input("enter a number between 1-10: "))

while num < 1 or num > 10:
    print(f"{num} not valid")
    num = int(input("enter a number between 1-10: "))

print(f"your number is {num}")




