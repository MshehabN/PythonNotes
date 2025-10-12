# a conditional expression is a one line shortcut for the if-else statement(ternary operator)
# print or assign one of two values based on a condition
#    the formula:   X if condition else Y

num =23

print("positive" if num == 23 else "negative")

#check for even or odd

num2 = 13

print("even" if num2 % 2 == 0 else "odd")

a = 6
b = 7

maxNum = a if a>b else b
print(maxNum)