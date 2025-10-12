import math

x  =(input("what operation would you like to do? +, -, /, * : "))

y =float(input("what is your first number?: "))
z =float(input("what is your second number?: "))

if x == "+":
    result = y+z
    print(f"The answer is {result}")
elif x == "-":
    result = y-z
    print(f"The answer is {result}")
elif x == "/":
    result= y/z
    print(f"The answer is {result}")
elif x == "*":
    result = y*z
    print(f"The answer is {result}")
else:
    print("not valid")



