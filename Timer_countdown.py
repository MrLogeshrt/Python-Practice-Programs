#Timer Countdown Program

import time

def format_time(i):
    seconds = i % 60
    minutes = int(i / 60) % 60
    hours = int(i / 3600)
    return f"{hours:02} : {minutes:02} : {seconds:02}"

def countdown(mytime):
    for i in range(mytime, 0, -1):
        print(format_time(i))
        time.sleep(1)
    print("Times Up..!")


mytime = int(input("Enter the time in 'sec' format : "))
countdown(mytime)