# format specifiers = {value: flags} format a value based on what
#                                 flags are inserted

price1 = 3.1234
price2 =-912.123
price3 = 12.34

price4 = 8631.12
price5 = -12398.1214
#so from what i understand here, we are following {value: flags}
#                    and we add .2f which means
# we type the . first to specify decimal point precision
# we type 2 to specify we want it to 2 decimal points
# and the f is to make it a float

print(f"Price 1 is ${price1:.2f}")
print(f"Price 2 is ${price2:.3f}")
print(f"Price 3 is ${price3:.1f}")

# to allocate space to display the output
#for example if you only want to allow price1 to have 10 spaces
#for the output you just put 10
#This gives it EXACTLY 10 spaces so if theres extra space it WILL fill the space
#with blank characters
print(f"Price 1 is ${price1:10}")
# if you precede the number with 0 the empty space that get allocated
#will be "0 padded" which just means it fills the space with 0
print(f"Price 2 is ${price2:010}")

#a left justify is when you put a "<" beside the number to make the blanks
#go on the other side, as you can see price1 in the second example has a big
#gap between the $ and the number basically this reverses this
print(f"Price 3 is ${price3:<07}")

#i wont show an example for a right justify because its just the default
#       so the price1 second example is basically a right justify by default

# to center a line its this "^" symbol, basically just places it in
#       the center of the blanks
print(f"Price 1 is ${price1:^10}")

#if you have any positives and wanna show it in the output,
#       you can just put a + sign, negatives stay negative
print(f"Price 2 is ${price2:+}")
print(f"Price 3 is ${price3:+}")

#to seperate the number by the thousands, use " , "
print(f"price 4 is ${price4:,}")
#output will be "price 4 is $8,631.12"

#can mix and match all stuff 




