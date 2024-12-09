import datetime
import time
date=datetime.datetime.now()
print(date)

print("---------------------------------")

date2=datetime.date.today()
print(date2)
print("--------------------------------------")

date3=datetime.date(2012,4,5)
print(date3)

print("--------------------------------------")

time1=datetime.time(23,45,6)
print(time1)

print("---------------------------------")

now=datetime.datetime.now()

print("time:",now.time)
print("year:",now.year)
print("day:",now.day)
print("hour:",now.hour)
print("minute:",now.minute)
print("second:",now.second)

print("---------------------------------")

today=datetime.date.today()
future_date=today+datetime.timedelta(days=18)
print(future_date)


year = datetime.datetime.now()
future_date1 = year + datetime.timedelta(days=100)
print(future_date1)