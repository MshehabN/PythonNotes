#logical operators evaluate conditions: or, and, not

temp = 25

is_raining = False

if temp > 35 or temp < 0 or is_raining == True:
    print("event is cancelled")
else:
    print("its still on")