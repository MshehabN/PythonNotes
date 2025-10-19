#number guessing game using random

import random

num = random.randint(1, 100)
print(num)
while True:
    guess = input("Guess a number between 1 and 100! (q to quit): ")

    if guess == 'q':
        break
    elif int(guess) > 100 or int(guess) < 1:
        print(f"enter a number between 1-100! {guess} is not valid")
    elif int(guess) > num:
        print("Lower!")
    elif int(guess) < num:
        print("Higher")
    elif int(guess) == num:
        print("Congratulations you got the right number!")
        break