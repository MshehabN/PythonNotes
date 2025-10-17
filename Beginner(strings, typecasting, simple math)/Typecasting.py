# process of changing a variable from one datatype to another
name = "moe"
age = 21
gpa = 3.14
student = True

#Using the type() function this is how we get the type of a variable
# print(type(name))
#output: str

#if we switch out the type word with a datatype we convert it into another one see the below example
gpa = int(gpa)
print(gpa)

#name = int(name)
#print(name)

age = str(age)
print(age)

#when converting to boolean
name = bool(name)
print(name)
#will always give true UNLESS the variable is EMPTY then it would give false