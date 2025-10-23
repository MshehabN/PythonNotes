#invoice generator

username = input("what is your username")
amount = int(input("How much do you owe?"))
due_date = input("when do you owe this?")


def displayInvoice(username, amount, due_date):
    print(f"hello {username}")
    print(f"you owe {amount} on {due_date}")

displayInvoice(username,amount,due_date)