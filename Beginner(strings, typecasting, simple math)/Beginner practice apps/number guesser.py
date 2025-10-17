realNumber = 64

guessNumber =int(input("Guess a number between 1 - 100: "))

while guessNumber > 100:
    print("cannot be over 100")
    guessNumber = int(input("Guess a number between 1 - 100: "))

while guessNumber < 1:
    print("cannot be less than 1")
    guessNumber = int(input("Guess a number between 1 - 100: "))

while guessNumber < realNumber:
    print("Higher")
    guessNumber = int(input("Guess a number between 1 - 100: "))
while guessNumber > realNumber:
    print("Lower")
    guessNumber = int(input("Guess a number between 1 - 100: "))

if guessNumber == realNumber:
    print(f"Correct! the number was {realNumber}")

