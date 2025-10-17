#indexing allows access to elements using this [] indexing operator
#     [start : end : step]

credit_number = "1234-2131-3423-2432"

# this will print out the number of the location specified,
#in this case we specified 0 which prints the first thing
print(credit_number[0])

#we use this to pick the first number all the way to 5 so basically
#1-5 but im not sure why it prints only 5 numbers since it starts at 0
#shouldn't it be 6?
print(credit_number[0 : 5])

# if you add the : and dont put an end number, python will print everything
#up till the end
print(credit_number[5 : ])

#when you start counting from negatives, it basically starts counting backwards
print(credit_number[-1])

#Step basically counts in steps so we put 2 : for start to finish
#because blanks mean python assumes its for start to finish and
#if we put 2 then it will count every second number
print(credit_number[::2])

#program to get the last 4 digits of a credit card number
print(credit_number[-4:])

#if you set step to -1 it reverses the string???
#i guess it makes sense because it will start counting backwards
revCredit = credit_number[::-1]
print(revCredit)