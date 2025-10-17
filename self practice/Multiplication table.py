#multiplaction table game



num = int(input("enter a number to show the multiplication table for: "))

for x in range(1, 11):
    print(f"{num} x {x} = {num*x}")