#consession stand program

shop = {"Popcorn":4.99
         ,"Coke": 3.99
         ,"Hotdog":4.49
         ,"Skittles":2.99
         ,"Sprite":3.99}

total = 0
receipt = []

print("===============================================")
print("          Welcome to shehabs shop!"            )
for item, price in shop.items():
    print(f"{item}: {price}")
print("===============================================")
while True:
    choice = input("What would you like to buy? (q to finish)")
    if choice == "q":
        break
    elif shop.get(choice):
        receipt.append(choice)
    elif shop.get(choice) is None:
        print("not valid")

print("===============================================")
print("You ordered: ")
for item in receipt:
    print(item, end="  ")
print()
print("===============================================")
for choice in receipt:
    total = total+shop.get(choice)

print(f"your total is: ${total}")

