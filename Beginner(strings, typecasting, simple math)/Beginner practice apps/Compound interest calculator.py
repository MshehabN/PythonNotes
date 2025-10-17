
initialBalance= float(input("what is your initial balance: "))
interestRate= float(input("what is your interestrate: "))
time = int(input("what is your how much time has passed (years): "))

finalAmount = initialBalance * pow((1+interestRate/100 ), time)


print(finalAmount)