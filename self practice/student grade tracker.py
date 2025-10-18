#student grade tracker

grades = []

while True:
   grade = input("enter a grade you would like averaged (q to quit): ")
   grade = int(grade)
   if grade not in range(0,101):
       print(f"enter a number between 1-100%, {grade} is not valid")
   elif grade in range(0,101):
       grades.append(grade)
       print("your grade has been added")
       average = sum(grades) / len(grades)
       print(f"your average is {average:.2f}")




