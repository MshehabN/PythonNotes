#for loops = execute a block a code a certain amount of times
#                you can iterate over a range, string, sequence, etc
from asyncio import wait_for

# x is the counter
#range function range(start, end) STOPS AT 11 DOES NOT COUNT 11
#basically counts 1-10
for x in range(1, 11):
    print(x)

print("happy bung day")

#to do it in reverse, use the reverse() function
for x in reversed(range(1, 11)):
    print(x)

print("happy bung day")

#to add a step, and count in 2s add another comma and add ur step
for x in reversed(range(1, 11, 2)):
    print(x)

print("happy bung day")

#continue basically skips an iteration
for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)

#here we use the break keyword which leaves the loop entirely
for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)