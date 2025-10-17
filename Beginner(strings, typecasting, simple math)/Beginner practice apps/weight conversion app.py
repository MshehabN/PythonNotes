unit = input("What unit of weight would you like to convert? kg or lbs?: ")

weight = float(input("enter the weight: "))

if unit == "kg":
    result = weight * 2.20462
    print(result)
elif unit == "lbs":
    result = weight / 2.20462
    print(result)
else :
    print("not valid")
