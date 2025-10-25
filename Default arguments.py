#default arguments  = a default value for certain parameters
#                       default is used when that argument is omitted
#                       make your functions more flexible, reduces # of arguments
#                       1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

#here we do a regular function to calculate sales tax
def netPrice(listPrice, discount, salesTax):
        return listPrice * (1 - discount) * (1+salesTax)

print(netPrice(500, 0, 0.13))


# but discount and sales tax is a constant value, so we can make that so in the function
def netPrice(listPrice, discount= 0, salesTax= 0.13):
    return listPrice * (1 - discount) * (1 + salesTax)

#now all we need to put in is the price
print(netPrice(500))

#but if the discount is different for example, the call will use whatever is passed in, instead of the default argument
print(netPrice(500, 10))