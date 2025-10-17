#shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("what food would you like to buy? (q to quit)")

    if food.lower() == 'q':
        break
    else:
        price = float(input(f"enter the price of {food} $"))
        foods.append(food)
        prices.append(price)

print("youve ordered")
for food in foods:
    print(food)

print(f"your total is: {sum(prices)}")







