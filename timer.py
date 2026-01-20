# countdown timer program
import time


my_time = int(input("Enter the time in seconds : "))

for x in range(my_time,0,-1):#this will count backwards like reversed(range())
    seconds = x%60
    minutes = int(x/60) % 60
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")# padding 0
    time.sleep(1)# code will sleep or start working after the given time in seconds


print("TIME'S UP ! ")