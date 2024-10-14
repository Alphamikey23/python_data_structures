import time

currentTime = time.time() # get current time

#obtain the total seconds since midnight, Jan 1, 1970
totalSeconds = int(currentTime)

#get the current second
currentSecond = totalSeconds % 60

#obtain the toal minutes
totalMinutes = totalSeconds // 60

#compute the current minute in the hour
currentMinute = totalMinutes % 60

#obtain the total hours
totalHours = totalMinutes // 60

#compute the current hour
currentHour = totalHours % 24

#display results

print("Current time is", currentHour, ":",currentMinute,":",currentSecond,"GMT")