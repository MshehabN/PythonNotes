import random
#variable = random.choice(list) --> picks a random element from the sequence
#picks a number from 1-6 to use to find a face in dictionary


diceArt = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

#numOfDice = int(input("how many dice do you want?"))


user = int(input("How many dice would you like?: "))

for times in range(user):
    randomNum = random.randint(1, 6)
    for die in diceArt.get(randomNum):#im not sure why this works
        print(die)



            #value?       #diction.get(key) ???
#       for die in diceArt.get(randomNum):#im not sure why this works
            #print(die)
#       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#from what I understand, for x in the diceArt dictionary, where x is ENTIRE list (the list being the face of the die)
                #we do diceArt.get() to GET the values of the specified key, this is how we assign the list to the die variable
                #randomNum randomizes numbers 1-6 to randomize the key from where to pull the list
                #though im not sure why its already formatted properly, im not complaining tho