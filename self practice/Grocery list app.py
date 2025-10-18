#grocery list app


receipt = []

print("==========================================")
print("welcome to Moe's grocery app!")
print("==========================================")
while True:
    print("(1 to add)")
    print("(2 to remove)")
    print("(3 to show list)")
    print("(q to quit)")
    user =  input("what would you like to do?: ")
    print("===================================")
    if user == '1':
       buy = input("what would you like to buy?: ")
       receipt.append(buy)
    elif user == '2':
        buy =input("what would you like to remove?: ")
        if buy in receipt:
            receipt.remove(buy)
            print("item has been removed")
        else:
            print("Item is not in the list")
    elif user == '3':
        for things in receipt:
            print(things)
    elif user.lower() == 'q':
        break
    else:
        print("please choose from the list")

