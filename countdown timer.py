import time

mytime = int(input("how long do you want the timer to run for?(seconds): "))

for x in range(mytime, 0 , -1):
     seconds = x % 60
     minutes = int(x/60) % 60
     hours = int (x/3600)
     print(f"{hours:02}:{minutes:02}:{seconds:02}")
     time.sleep(1)
