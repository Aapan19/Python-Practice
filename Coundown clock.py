import time

myTime = int(input("Enter the time in second: "))

for x in range(myTime, 0, -1):
    seconds = x % 60  # 60 seconds a minute
    minutes = int(x/60) % 60  # 60 Minute a hour
    hours = int(x/3600) % 24  # 24 hours a day
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Times's Up! ")
