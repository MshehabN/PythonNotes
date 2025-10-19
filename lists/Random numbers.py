import random #gives us access to a lot of useful methods

#print(help(random))
#variable = random.randint(min, max)
#variable = random.random() --> returns a random floating point number (between 0-1)
#variable = random.choice(list) --> picks a random element from the sequence
#random.shuffle(list) --> randomly shuffles the list element locations indexes

#example
num = random.randint(1, 6)

#can use variables
low = 1
high = 100
num2 = random.randint(low, high)

#variable = random.random() --> returns a random floating point number(between 0-1)
num3 = random.random()
print(num)
print(num2)
print(num3)

#we create the list, and use random.choice to pick a random element
options = ("rock","paper", "scissors")
option = random.choice(options)
print(option)

#shuffling all cards
cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
random.shuffle(cards)
print(cards)
