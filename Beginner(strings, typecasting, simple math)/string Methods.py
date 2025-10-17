name = input("enter your full name: ")

#len() will give you the length of a string
print(len(name))


#finds the first LOCATION where the character occurs
#if find is looking for the letter M and its the first letter the output will be 0
print(name.find("M"))

#rfind is the same idea as find but its for the LAST occurance instead
print(name.rfind("D"))

#capitalizes the name variable
print(name.capitalize())

#makes everything capital
print(name.upper())

#makes everything lowercase
print(name.lower())

#isdigit() returns either true or false depending on if the string contains ONLY digits
print(name.isdigit())

#isalpha() returns either true or false depending on if the string contains ONLY alphabets
print(name.isalpha())

#count. counts how many times a specific character appears wheras len() gives the total length of a string
phoneNumber= input("enter your phone number: ")

print(phoneNumber.count("6"))

#the .replace method will replace any character with another
# where the first character is the number to be replaced and the second is doing the replacing
print(phoneNumber.replace("6", "23"))

#doing this print(help(str)) will print out all string methods available