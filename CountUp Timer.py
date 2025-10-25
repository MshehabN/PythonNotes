import time

#the end is first because we cant have the first value default if we are passing in arguments
#since the call has to follow the steps 
def count(end, start= 0):
    for x in range(start, end+1):
        time.sleep(1)
        print( x)
    print("done")


count(10)