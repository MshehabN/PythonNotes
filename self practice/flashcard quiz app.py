#quiz app

questions = ("Whats my favourite cats name?",
             "How old am i currently?(2025)",
             "Whats my favourite video game?"
            ,"What sport did i play in high school?"
            ,"What language am i practicing right now?")


options = (("A: Kobe","B: Nala","C: Coco","D: Crazy"),
           ("A: 42","B: 9","C: 21","D: 22"),
           ("A: Warhammer","B: Tarkov","C: Rimworld","D: Rust"),
           ("A: Badminton","B: Tennis","C: Wrestling","D: Hockey"),
           ("A: Java","B: Python","C: Lua","D: C++"))

answers = [("A"), ("C"), ("D"), ("C"), ("B")]
questionNum = 0
guesses = []
finalscore = 0
print("========================================")
print("      WELCOME TO SHEHAB'S QUIZ!!      ")
print("========================================")

while True:
    for question in questions: #everytime this runs
        print(question)
        for option in options[questionNum]: #we use questionNum to specify the index
            print(option)
        questionNum = questionNum +1 # we increment here ensure the index goes up by 1 each time
        guess = input("whats your guess?(A,B,C,D): ")
        if guess.upper() == answers[questionNum-1]:# since we incremented it earlier, we do -1 to ensure the increment stays the same
            print("CORRECT!")
            guesses.append(guess.upper())
            finalscore = finalscore +1
        elif guess.upper() != answers[questionNum-1]:
            guesses.append(guess.upper())
            print("INCORRECT!")
        print("========================================")
    print(f"your guesses were{guesses}")
    print(f"your score is {finalscore/len(guesses)*100}%")
    break









