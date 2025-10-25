# keyword arguments = an argument preceded by an identifier
#                     helps with readability
#                     order of arguments doesn't matter
#                     1.positional, 2. default, 3. KEYWORD, 4. arbitrary

def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

#prefix the strings with the variable name and the order doesnt matter anymore
#can mix and match, here im using positional AND keyword arguments
#just make sure the positional arguments are first other you will get an error
hello("Hello", first="Moe", last ="Shehab",title= "Mr",)


for x in range(1, 11):
    print(x, end=" ") #end = " " is a keyword argument

print("1", "2", "3", "4", "5", sep="-") #sep=" " seperates the strings with a given string (we used -)
                                        #       it is also a keyword argument
def getPhone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phoneNum = getPhone(country=1, area=613, first=737,last=1111) #assigning a value to the getPhone function return output
print(phoneNum)