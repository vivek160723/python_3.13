import datetime
start_date = datetime.datetime(2024, 1, 1)
current_date = datetime.datetime.now()
difference = current_date - start_date
number_of_days = difference.days

print(number_of_days,"Days")