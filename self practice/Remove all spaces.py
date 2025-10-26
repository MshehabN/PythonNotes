#function that returns the string but without spaces
def spaceRemover(sentence):
    spareList = []
    for space in sentence:
        if space == " ":
            space = ""
            spareList.append(space)
        else:
            spareList.append(space)
    spaceless = "".join(spareList)
    return spaceless

print(spaceRemover("function that returns the string but without spaces"))


#SIMPLER CODE
def spaceRemover(sentence):
    spareList = []
    for char in sentence:
        if char != " ":
            spareList.append(char)
    return "".join(spareList)