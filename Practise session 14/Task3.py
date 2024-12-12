from datetime import datetime

file = open("/rPractise/Task3.txt", 'a')
date2=datetime.today().date()
print(date2)
file.write(str(date2))
file.close()
