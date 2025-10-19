#rock paper scissors game
#variable = random.choice(list) --> picks a random element from the sequence

import random
scoreLoss = 0
scoreWin  =0
bot = ("rock", "paper", "scissors")

while True:
    botChoice = random.choice(bot)
    print(botChoice)
    user = input("pick between rock, paper, or scissors: ")

    #tied
    if user == botChoice:
        print("========================================================")
        print(f"You both picked {botChoice}! its a draw!")
        print("========================================================")

    #user rock vs paper (lose)
    elif user.lower() == 'rock' and botChoice == 'paper':
        print("========================================================")
        print(f"You lose! {botChoice} beats {user}!")
        scoreLoss = scoreLoss +1
        print("========================================================")
    # user scissors vs rock (lose)
    elif user.lower() == 'scissors' and botChoice == 'rock':
        print("========================================================")
        print(f"You lose! {botChoice} beats {user}!")
        scoreLoss = scoreLoss + 1
        print("========================================================")
    # user paper vs scissors (lose)
    elif user.lower() == 'paper' and botChoice == 'scissors':
        print("========================================================")
        print(f"You lose! {botChoice} beats {user}!")
        scoreLoss = scoreLoss + 1
        print("========================================================")
    # user paper vs rock(win)
    elif user.lower() == 'paper' and botChoice == 'rock':
        print("========================================================")
        print(f"You Win! {user} beats {botChoice}!")
        scoreWin = scoreWin + 1
        print("========================================================")
    # user rock vs scissors(win)
    elif user.lower() == 'rock' and botChoice == 'paper':
        print("========================================================")
        print(f"You Win! {user} beats {botChoice}!")
        scoreWin = scoreWin + 1
        print("========================================================")
    # user scissors vs paper(win)
    elif user.lower() == 'paper' and botChoice == 'scissors':
        print("========================================================")
        print(f"You Win! {user} beats {botChoice}!")
        scoreWin = scoreWin + 1
        print("========================================================")

    cont = input("would you like to keep playing? (y/n): ")
    if cont == 'y':
        pass
    elif cont =='n':
        print("========================================================")
        print(f"Thanks for playing, your beat the bot {scoreWin} times!")
        print(f"and you lost {scoreLoss} times!")
        break











