from datetime import datetime

time1 = datetime.strptime("10:30:00", "%H:%M:%S")
time2 = datetime.strptime("14:45:30", "%H:%M:%S")

time_difference = time2 - time1

print(time_difference)