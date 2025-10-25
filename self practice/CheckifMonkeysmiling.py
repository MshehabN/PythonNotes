def isSmiling(check1, check2):
    if check1 == True and check2 == True:
        smiling = True
    elif check1 == False and check2 == False:
        smiling = True
    else:
        smiling = False

    return smiling

print(isSmiling(False, False))

#can be heavily simplified

def isSmiling(check1, check2):
    return check1 == check2

print(isSmiling(False, False))


#^^^^ literally does the same thing