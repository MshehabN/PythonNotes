# input() takes in user input
    # returns the entered data as a string


# assign the input function to a variable to store the response
x = input("yo how old are you: ")
#typecast into an int since the prompt returns a string
x = int(x)
if x <= 18:
    print(f"lil boyyyy LOLZ UR {x}")
elif x>18:
    print(f"ewww ur old asf how are you {x}")

#BUTTTT to make things easier we can typecast into the prompt

dicks = int(input("how many dicks?  "))
if dicks == 100:
    print("YEOOOO HUNNID DICKS")
elif dicks <= 100:
    print("shits not funny bro")


#would be better to put a float
length = int(input("enter the length of the rectangle: "))
width = int(input("enter the width of the rectangle: "))
area = length * width
print(area)

